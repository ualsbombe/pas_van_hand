#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:56:41 2026

@author: ualsbombe
"""

#%% IMPORTS

from fnames import FileNames

#%% GENERAL

fname = FileNames()

fname.add('project_path', '/home/ualsbombe/pas_van_hand')
fname.add('raw_path', '{project_path}/data')
fname.add('deriv_path', '{project_path}/deriv')
fname.add('script_path', '{project_path}/scripts')
fname.add('python_path', '{script_path}/python')
fname.add('slurm_path', '{script_path}/slurm')
fname.add('MEG_path', '{deriv_path}/MEG')

slurm_parameters = dict()

slurm_parameters['analysis_00_create_folders'] = dict(cores=1, mem=0.5)

#%% RECORDINGS

recordings = \
    [
     dict(subject='0002', date='20120829_000000')
    ]




#%% SUBJECT SPECIFIC SETTINGS

fname.add('subject_path', '{MEG_path}/{subject}/{date}', )

#%% EVOKED ANALYSIS

## filtering

## epoching

## averaging

#%% SENSOR CLASSIFICATION

#%% FORWARD MODELLING

#%% SOURCE MODELLING