import os

"""This script points to the location of all speaker files and checks the size of each .wav file. Any audio files <40KB and their corresponding .txt file 
are removed from the directory because either one or less words are spoken in the segment, or the speech is undetectable and will not be picked up by VAD."""

path = "./icsi_files/"
folders = os.listdir(path)

for folder in os.listdir(path):
    for file in os.listdir(path+folder+'/'):
        if '.wav' in file:
            if os.path.getsize(path+folder+'/'+file)<40000:
                os.remove(path+folder+'/'+file)
                os.remove(path+folder+'/'+file.strip('.wav')+'.txt')
