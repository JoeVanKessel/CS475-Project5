#!/usr/bin/python
import os

if __name__ == "__main__":
    trials = [16*1024, 32*1024, 64*1024, 128*1024, 256*1024, 512*1024, 1000*1024]
    blockSizes = [16, 32, 64, 128]
    cudaNVCC = "/usr/local/apps/cuda/cuda-10.1/bin/nvcc"
    print("NUMTRIALS    BLOCKSIZE       MEGATRIALS/S    PROBABILITY")
    for trial in trials:
            for blockSize in blockSizes:
                cmd = f"{cudaNVCC} -o CUDAmonteCarlo CUDAmonteCarlo.cu -DNUMTRIALS={trial} -DBLOCKSIZE={blockSize}"
                os.system(cmd)
                cmdExe = "./CUDAmonteCarlo"
                os.system(cmdExe)
