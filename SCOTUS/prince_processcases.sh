#!/bin/bash

#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=2:00:00
#SBATCH --gres=gpu:1
#SBATCH --mem=8GB
#SBATCH --job-name=dvec_SCOTUS
#SBATCH --output=dvec.out

python SpeakerVerificationEmbedding/src/SCOTUS/dvector_SCOTUS.py
