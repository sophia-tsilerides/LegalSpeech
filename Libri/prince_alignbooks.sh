#!/bin/bash

#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=2:00:00
#SBATCH --mem=8GB
#SBATCH --job-name=align_Libri
#SBATCH --output=align_lib.out

python SpeakerVerificationEmbedding/Libri/align_Libri.py
