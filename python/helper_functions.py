#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:24:02 2026

@author: ualsbombe
"""

from config import slurm_parameters, fname
from subprocess import run
from os import environ ## do we need this for SUBJECTS_DIR later?

def submit_job(recording, function_name):
    
    
    ## get the recording
    subject = recording['subject']
    date    = recording['date']
    
    ## write the sbatch command
    
    sbatch_command = \
        f'#! /bin/bash\n' + \
        f'# SBATCH --name {function_name}\n' + \
        f'# SBATCH --account pas_van_hand\n' + \
        f'# SBATCH -c {slurm_parameters[function_name]['cores']}\n' + \
        f'# SBATCH --mem {slurm_parameters[function_name]['mem']}\n' + \
        f'python {fname.python_path}/{function_name}.py {subject} {date}'
        
    ##  write a temp file to be submitted    
    
    filename = f'{fname.slurm_path}/{function_name}.sh'
        
    with open(filename, 'w') as file:
        file.write(sbatch_command)
        
    ## submit using bash
    
    # environment = environ.copy()
    result = run(['sbatch', filename], cwd=fname.slurm_path,
                   capture_output=True, text=True, timeout=10)
    print(result.stdout)
    print(result.stderr)
    
    # clean a little
    run(['rm', filename], cwd=fname.slurm_path)

    
        
    