#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Modified from https://github.com/JanhHyun/Speaker_Verification
import glob
import os
import librosa
import numpy as np
from hparam import hparam as hp

# downloaded dataset path
audio_path = glob.glob(os.path.dirname(hp.unprocessed_data))                                        

for i, folder in enumerate(audio_path):
    print(i, folder)
    