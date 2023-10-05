#!/bin/bash

wk_dir=$1
#--------record memory----------
#root_dir=$PWD
#cd $wk_dir #${root_dir}
#----------cpu--------------
#cpu_usages_log="${root_dir}-${SLURM_JOB_ID}-cpu-usages.log"
cpu_usages_log="${SLURM_JOB_ID}-cpu-usages.log"
if [ -f "${cpu_usages_log}" ]; then
        mv ${cpu_usages_log} "${cpu_usages_log}_${SLURM_JOB_ID}"
fi
#while true; do echo `date; ps -u$USER -o %cpu,rss |head -n 4` >> ${cpu_usages_log}; sleep 5; done
while true; do echo `date; ps -u$USER -o %cpu,rss` >> ${wk_dir}/${cpu_usages_log}; sleep 5; done &
#----------cpu max----------
#max_cpu_usages_log="${root_dir}-${SLURM_JOB_ID}-max-cpu-usages.log"
max_cpu_usages_log="${SLURM_JOB_ID}-max-cpu-usages.log"
echo "time max_mem_used" > ${wk_dir}/${max_cpu_usages_log}
while true; do max_mem=`cat /sys/fs/cgroup/memory/slurm/uid_${UID}/job_${SLURM_JOB_ID}/memory.max_usage_in_bytes`; echo `date; echo ${max_mem}` >> ${wk_dir}/${max_cpu_usages_log}; sleep 5; done &
#--------end memory recording--------

