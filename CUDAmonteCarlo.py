#!/usr/bin/python
import os

if __name__ == "__main__":
    trials = [16*1024, 32*1024, 64*1024, 128*1024, 256*1024, 512*1024, 1000*1024]
    blockSizes = [16, 32, 64, 128]
    # for size in blockSize:
    #     for trial in trials:

            # cmd = f"g++ -DNUMT=\"{thread}\" -DNUMTRIES=\"{tries}\" -DNUMTRIALS=\"{trial}\" -o monteCarlo monteCarlo.cpp -lm -fopenmp"
            # os.system(cmd)
            # cmd = "./monteCarlo"
            # os.system(cmd)
    
    cudaNVCC = "/usr/local/cuda-10.2/bin/nvcc"
    # cudaPATH = "/usr/local/cuda-10.2"
    # cudaBIN = "/usr/local/cuda-10.2/bin"

    # os.environ["CUDA_PATH"] = cudaPATH
    # os.environ["CUDA_BIN_PATH"] = cudaBIN
    # os.environ["CUDA_NVCC"] = cudaNVCC

    trial = 16*1024
    blockSize = 16
    cmd = f"{cudaNVCC} -o CUDAmonteCarlo CUDAmonteCarlo.cu -DNUMTRIALS={trial} -DBLOCKSIZE={blockSize}"
    os.system(cmd)
    cmdExe = "./CUDAmonteCarlo"
    os.system(cmdExe)
