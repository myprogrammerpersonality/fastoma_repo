#!/bin/bash

#SBATCH --nodes 1
#SBATCH --ntasks 1
#SBATCH --job-name fastoma-array-jobs
#SBATCH --cpus-per-task 1
#SBATCH --mem 10G
#SBATCH --time 10:00:00

#SBATCH --output=logs/mid_adjustedfamily_40_1_%A_%a.out

#SBATCH --array=0-399
N_WORKERS=400

export PYTHONUNBUFFERED=1

echo "started"

python fastoma_mid.py $SLURM_ARRAY_TASK_ID $N_WORKERS

if [ $? != 0 ];
then
    echo "EXIT 1"
else
    echo "EXIT 0"
fi

echo "finished"