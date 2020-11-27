#!/bin/bash

#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=1:00:00
#SBATCH --mem=8GB
#SBATCH --job-name=scochk
#SBATCH --output=scotus_check.out

python LegalUISRNN/SCOTUS/checkSCdata.py
