#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import os
import librosa
import numpy as np
from hparam import hparam as hp

"""This script points to the location of the unprocessed data files, and lists each speaker folder with its assigned speaker #.
The unprocessed data consists of folders for each speaker. During data_preprocess.py, numpy files are created for each speaker,
and placed in train_tisv and test_tisv folders. Once this occurs, the original speaker name is lost and replaced by a speaker #
that was assigned during preprocessing. The purpose of this script is to determine which original speaker name corresponds with 
the speaker #. This is useful in determining which speakers had 0 length numpy files. These speaker files can then be discarded."""

# downloaded dataset path
audio_path = glob.glob(os.path.dirname(hp.unprocessed_data))                                        

for i, folder in enumerate(audio_path):
    print(i, folder)
    
