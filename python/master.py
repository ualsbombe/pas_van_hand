#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:17:42 2026

@author: ualsbombe
"""

from helper_functions import submit_job
from config import recordings


subjects_to_run = \
     [
      '0002'
     ]
     
functions = \
    [
        'analysis_00_create_folders' 
    ]

for function in functions:     
    for recording in recordings:
        if recording['subject'] in subjects_to_run:
            submit_job(recording, function)
        