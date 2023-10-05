#!/bin/bash

arr_file=`find $PWD -maxdepth 1 -name "*-usages.log" -print`
module load python/intel/3.8.6
python process-gpu-cpu-usages_v2.py $arr_file

