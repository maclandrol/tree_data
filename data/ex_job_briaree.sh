#!/bin/bash
#PBS -l nodes=1:ppn=6
#PBS -l walltime=1:00:00
#PBS -o AAE_out
#PBS -j oe
#PBS -r n
#PBS -V
#PBS -N AAE
#PBS -m bea
#PBS -M fmr.noutahi@umontreal.ca


cd test

./run_phyml AAE
