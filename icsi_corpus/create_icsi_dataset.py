import os
import re
from pydub import AudioSegment

"""This script points to the location of the ICSI Meeting transcripts and raw audio files. For each single line of speech in a transcript, the script 
extracts a list of start/end times of speaking, speaker name, and speech transcript. Folders are created for each speaker. Within each folder, a .txt file 
is saved for a single line of speech belonging to the speaker. The .txt file contains start/end speaking time, concatenated with speech transcript. 
Corresponding audio files of the speech segment are saved as .wav files in the speaker folder, with the same name as the corresponding .txt file."""

path = "./icsi_data/raw_transcripts/transcripts"

transcripts = os.listdir(path)

files = []
for file in transcripts:
    if '.mrt' in file:
        if 'preambles' in file:
            continue
        files.append(file)

os.makedirs('./icsi_data/icsi_files')

for file in files:
    path = "./icsi_data/raw_transcripts/transcripts"
    f = open(path+'/'+file, "r")
    #create list of lines that contain start/end times with speaker
    data = []
    for line in f:
        if "StartTime" in line:
            data.append(re.findall('"([^"]*)"',line))
    #remove first entry which states span of entire clip
    data.pop(0)
    
    #convert times from string to float
    for t in data:
        t[0]=float(t[0])
        t[1]=float(t[1])
        
    #get transcripts out by getting data between segment tags
    segment = []
    with open(path+'/'+file) as f:
        for line in f:
            if "<Segment" in line.rstrip():
                for line in f:
                    if "</Segment>" in line.rstrip():
                        break
                    segment.append(line.rstrip())
                    
    #strip out text from transcript segments removing anything inside tags
    transcript = []
    for s in segment:
        if (re.findall(r'(.*?)\<.*?\>', s))==[]:
            script = s
        else:
            script = re.findall(r'(.*?)\<.*?\>', s)
        script = ''.join(script)
        script = script.strip()
        transcript.append(script)
        
    text = []
    #concatenate speaking start time, end time and transcript
    for i in range(len(transcript)):
        text.append([data[i][0],data[i][1],transcript[i]])
        
    #save separate .txt files of concatenation in speaker folders
    path = './icsi_data/icsi_files/'
    for i in range(len(data)):
        
        #ignore empty transcripts 
        if text[i][2]!='':
            
            #if no speaker folder, create it
            if data[i][2] not in os.listdir(path):
                os.makedirs(path+data[i][2])  
                
            #create file number 
            file_num = len(os.listdir(path+data[i][2]))
            file_num = int(file_num - file_num/2)

            #save start time, end time, transcript as .txt file in speaker folder
            with open(path+data[i][2]+'/'+file.strip('.mrt')+'_{}.txt'.format(file_num),'w') as output:
                output.write(str(text[i][0])+' '+ str(text[i][1]) +' ' + text[i][2])

            #open corresponding audio file
            audio_file = './icsi_data/raw_audio/'+file.strip('.mrt')+'.interaction.wav'
            audio = AudioSegment.from_wav(audio_file)
            
            #split audio file based on start, end times
            start = data[i][0]*1000
            end = data[i][1]*1000
            split = audio[start:end]
            
            #save audio file in speaker folder with same file number
            split.export(path+data[i][2]+'/'+file.strip('.mrt')+'_{}.wav'.format(file_num),format='wav')
            
    print('Done ' + file)

