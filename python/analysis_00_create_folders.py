#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:24:34 2026

@author: ualsbombe
"""

from config import fname
from os import makedirs
from sys import argv

# make these into a function that is in helper functions

subject = argv[1]
date = argv[2]


makedirs(fname.subject_path(subject=subject,
                                date=date), exist_ok=True)