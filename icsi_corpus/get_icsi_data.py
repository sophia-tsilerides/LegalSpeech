import os

"""Script to download ICSI Meeting Corpus - transcripts and audio files"""

path = './icsi_data'

#create new directories to store raw files
os.makedirs(path+'/raw_transcripts')
os.makedirs(path+'/raw_audio')

#download raw transcripts
wget -P ./icsi_data/raw_transcripts http://groups.inf.ed.ac.uk/ami/ICSICorpusAnnotations/ICSI_original_transcripts.zip

import zipfile
with zipfile.ZipFile(path+'/raw_transcripts/ICSI_original_transcripts.zip','r') as zip_ref:
    zip_ref.extractall('./icsi_data/raw_transcripts/')

#download raw audio files

files = os.listdir(path+'/raw_transcripts/transcripts')
for i in files:
    i=i.strip('.mrt')
    os.system('wget -P ./icsi_data/raw_audio http://groups.inf.ed.ac.uk/ami//ICSIsignals/NXT/%s.interaction.wav'%i)
