## FastOMA
This repo is created in order to keep track of the changes that I apply to the FastOMA algorithm and experiments that I run.

## Usage
### Array Jobs
In order to use fastoma on a folder containing rHOGs using array jobs in slurm (rHOGs would be devided between jobs equally), first change the address variable in the `fastoma_mid.py` file (`address_rhogs_folder`, `address_pickles_folder`, `address_group_xml_ortho`) then run the following command:
```bash
conda activate YOUR_ENVIRONMENT
mkdir logs
sbatch slurm_job.sh
```
The jobs will be run in parallel and the results will be stored in the `address_pickles_folder`.