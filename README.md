# evaluation-performance

Three simple steps to use it
### 1 copy the folder evaluation-performance to the directory where you run your job
```bash
cp -r evaluation-performance .
```
### 2 add the lines to job scripts
add them before your executives; 
if you're unsure, simply after the slurm headlines beginning with #SBATCH
```bash
#########performance evaluation########
wk_dir=$(pwd)
bash $wk_dir/evaluation-performance/evaluation-performance.sh $wk_dir/evaluation-performance/
############end########################
```
### 3. check the real-time memory usage
after the job was completed or failed, go to the folder and then
```bash
bash plot_usage_gpu_cpu.sh
```
