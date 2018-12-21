Install Ubuntu, say, 16.04
Install gcc:
$ sudo apt install gcc

https://askubuntu.com/questions/799184/how-can-i-install-cuda-on-ubuntu-16-04

https://stackoverflow.com/questions/22360771/missing-recommended-library-libglu-so

Adding the following into the bashrc:
$ sudo nano ~./bashrc
export PATH=${PATH}:/usr/local/cuda-10.0/bin
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/cuda-10.0/lib64

$ sudo apt-get install lsb-core

pgi accelerator
https://www.pugetsystems.com/labs/hpc/Install-CUDA-and-PGI-Accelerator-with-OpenACC-577/
