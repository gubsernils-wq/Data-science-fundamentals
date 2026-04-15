#!/bin/bash
#SBATCH --job-name=dsf_training
#SBATCH --output=dsf_training.out
#SBATCH --error=dsf_training.err
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --partition=epyc2

source /software/Modules/current/init/bash
module load Anaconda3/2024.02-1
source $(conda info --base)/etc/profile.d/conda.sh
conda activate dsf_mtp

cd /storage/homefs/ng24z037/ml_kinase2

python training_aufgabe9.py
