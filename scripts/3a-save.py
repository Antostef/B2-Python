#!/usr/local/bin/python3
# 3a-save.py
# Script that makes a savefile
# Stefanaggi Antoine-Dominique
# 11/11/18
import os
from shutil import make_archive

if not os.path.exists('~/Downloads/data'):
    os.makedirs('~/Downloads/data')

archive_name = os.path.expanduser(os.path.join('~/Downloads/data/', 'archive'))

