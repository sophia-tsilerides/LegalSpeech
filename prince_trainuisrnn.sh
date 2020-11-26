#!/bin/bash

#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=2:00:00
#SBATCH --gres=gpu:1
#SBATCH --mem=8GB
#SBATCH --job-name=uis_samp
#SBATCH --output=uisrnn_samp.out

python LegalUISRNN/SCOTUS/SCOTUS.py
