#!/bin/bash
#SBATCH -J Project5
#SBATCH -A cs475-575
#SBATCH -p class
#SBATCH --gres=gpu:1
#SBATCH -o Project5.out
#SBATCH -e Project5.err
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=vankessj@oregonstate.edu
python3 CUDAmonteCarlo.py
