#!/bin/bash

#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=1:00:00
#SBATCH --mem=8GB
#SBATCH --job-name=align_SCOTUS
#SBATCH --output=align.out

python SpeakerVerificationEmbedding/src/SCOTUS/align_SCOTUS.py
