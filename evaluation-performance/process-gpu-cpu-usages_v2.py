import matplotlib.pyplot as plt
import datetime
import numpy as np
from datetime import datetime

'''no data of time information is shared; version 1, time for max_mem is shared among files'''

def plot_time_series(x,y,label):
  #x = np.array([datetime.datetime(2013, 9, 28, i, 0) for i in range(24)])
  #y = np.random.randint(100, size=x.shape)
  if label=="CPU":
    maxMem=np.max(y)
    label +="__maxMem_"+str(round(maxMem,9))+"GB"
    y/=maxMem
    y*=100
  plt.plot(x,y,label=label)
  plt.xlabel("time"),plt.ylabel("usage (%)")
  plt.legend()
  #plt.savefig("gpu_cpu_usage.png",dpi=300)
  #plt.show()
def read_gpu_data(fn,skip_header):
  time_series, usage=[],[]
  i=0
  with open(fn) as fil:
      for line in fil:
        if i>=skip_header:
          line=line.strip('\n')
          line=line.split(", ")
          #line[-2]=float(line[-2])
          #print(line)
          tim=datetime.strptime(line[1],"%Y/%m/%d %H:%M:%S.%f")
          time_series.append(tim),usage.append(float(line[-1])) #][-2])
        i +=1
  return time_series, usage
def read_cpu_data(fn,skip_header):
  time_series, usage=[],[]
  if "cpu" in fn and "max" not in fn:
    label="CPU"
    i=0
    with open(fn) as fil:
      for line in fil:
        if i>=skip_header:
          line=line.strip('\n')
          line=line.split(" ")
          tim=line[1]+" "+line[2]+" "+line[3]+" "+line[6]
          tim=datetime.strptime(tim,"%b %d %H:%M:%S %Y")
          used=0
          for i in range(9,len(line),2):
            used +=float(line[i])/1e9 # MiB=1024.0**2; MB=1e6
          time_series.append(tim),usage.append(used)
        i +=1
    return time_series, usage, label
  if "cpu" in fn and "max" in fn:
    i=0
    with open(fn) as fil:
      for line in fil:
        if i>=skip_header+1:
          line=line.strip('\n')
          line=line.split(" ")
          tim=line[1]+" "+line[2]+" "+line[3]+" "+line[6]
          tim=datetime.strptime(tim,"%b %d %H:%M:%S %Y")
          used=float(line[-1])/1e9
          time_series.append(tim),usage.append(round(used,3))
        i +=1
      label="CPU_max_mem_"+str(np.max(usage))+"GB (true)"
    return time_series, usage, label
  ##------get max cpu memory used------------
  #usage1=np.genfromtxt(sys.argv[2],skip_header=1)
  #min_ID=len(time_series)
  #if min_ID>len(usage1): min_ID=len(usage1)
  ##print("check here: ",time_series[0:100],len(usage1))
  ##min_ID=np.min(len(time_series),len(usage1))
  ##print("min_ID ",min_ID)
  #time_series_max=np.copy(time_series[0:min_ID])
  #usage_max=np.copy(usage1[0:min_ID])/1e9
  #return time_series, usage, time_series_max, usage_max
def plot_file(fn):
    print(fn)
    if "gpu" in fn:
      time_series, usage = read_gpu_data(fn,skip_header=1)
      label="GPU"
      plot_time_series(time_series, usage, label)
    if "cpu" in fn: # and "max" not in fn:
      #label="CPU"
      time_series, usage, label = read_cpu_data(fn,skip_header=0)
      plot_time_series(time_series, usage, label)
    #if "cpu" in fn and "max" in fn:
    #  time_max,usage_max = read_cpu_data(fn,skip_header=0)
    #  label="CPU_max_mem_"+str(np.max(usage_max))
    #  plot_time_series(time_max, 100*usage_max/np.max(usage_max), label)
if __name__=="__main__":

    import sys
  #if len(sys.argv)==2 or (len(sys.argv)==3 and "cpu" in sys.argv[1]):
  #  fn=sys.argv[1]
  #  plot_file(fn)
  #if len(sys.argv)==3 and ("cpu" not in sys.argv[1]):
    for i in range(1,len(sys.argv)): #(1,3):
      fn=sys.argv[i]
      print("file: ",fn)
      #if "cpu" not in sys.argv[i]:
      #  plot_file(fn)
      plot_file(fn)
    plt.savefig("gpu_cpu_usage.png",dpi=300)
    plt.show()
