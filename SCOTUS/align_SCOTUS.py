#!/usr/bin/env python3

import glob
import csv
import os
import numpy as np
import sys
sys.path.append("./SpeakerVerificationEmbedding/src")
from hparam import hparam_SCOTUS as hp

 
case_path = glob.glob(os.path.dirname(hp.data.save_path+'*/*'))
verbose = hp.data.verbose
  
# Reconstructs alignments and labels in order
for i, folder in enumerate(case_path):
    case = folder.split('/')[-1]

    '''
    #Skip case if already aligned
    if os.path.exists(folder+'/'+case[:-7]+'_sequence.npy'):
        if verbose:
            print("Skipped case:", case)
        continue
    '''
        
    if verbose:
        print("Aligning case ", case[:-7])
      
    with open(folder+'/'+case+'_info.csv') as f:
        reader = csv.reader(f)
        path = list(reader)
    
    srtlst = sorted(path, key=lambda x: x[0])
    temp_sequence = np.load(folder+'/'+case+'_embarr.npy', allow_pickle=True)
    temp_cluster_id = np.load(folder+'/'+case+'_labelarr.npy', allow_pickle=True)
    
    sizetemp=0
    temp_lst = []
    temp_id_lst = []
    for t0,t1,s,i,j in srtlst:
        sizetemp+=int(s)
        temp_lst.append(temp_sequence[int(j)][int(i)])
        temp_id_lst.append(temp_cluster_id[int(j)][int(i)])
    

    case_emb = np.asarray(temp_lst)
    case_label = np.asarray(temp_id_lst)
    #case_emb = np.concatenate(temp_lst, axis=0)
    #case_label = np.concatenate(temp_id_lst, axis=0)
      
    if verbose:
        print("Expected Sequence Shape:", sizetemp, " X ", hp.model.proj)
        print("Expected ID Shape:", sizetemp, " X ", '')
        print("Sequence Shape:", np.shape(case_emb))
        print("ID Shape:", np.shape(case_label))
        
    np.save(folder+'/'+case[:-7]+'_sequence.npy', case_emb)
    np.save(folder+'/'+case[:-7]+'_cluster_id.npy', case_label)

  
  
  
  
  