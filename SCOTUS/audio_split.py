#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import os

def getMeta(docket, data):
    
    #get meta data as well as rearrange to desirable formal
    transcript, speakers, speaker_roles, times = data[docket]
    
    # Flatten times list
    times_new = []
    for t in times:
        flatten = [item for sublist in t for item in sublist]
        times_new.append(flatten)  
    # Last element of list is a 0 - cleanup    
    del times_new[-1][-1]
    
    # Flatten speaker_roles list and replace nulls with "Other"
    speaker_roles_clean = []
    for i in speaker_roles:
        if not i:
            speaker_roles_clean.append('Other')
        else:
            speaker_roles_clean.append(i[0])
            
    # Remove all non-word characters in speakers' names
    speakers =[re.sub(r"[^\w\s]", '', s) for s in speakers]
    # Replace all runs of whitespace with underscorei in speakers' names
    speakers =[re.sub(r"\s+", '_', s) for s in speakers]
    
    return transcript, speakers, speaker_roles_clean, times_new

def getSpeakerDict(transcript, speakers, speaker_roles, times_new):
    speaker_dict = {}
    
    # Create a dictionary with all the parsed data from getMeta()
    for i in range(len(speakers)):
        speaker_dict[speakers[i] + '_' + speaker_roles[i] + '_' + str(i)] = times_new[i][0], times_new[i][-1], transcript[i]
        
    return speaker_dict

def createFolders(docket, speakers, speaker_roles, times, data, commands = False):
    if commands is False:
        os.mkdir(os.getcwd() + '/SCOTUS/' + str(docket) + '_SCOTUS')
    
    folders = []
    for i in range(len(speakers)):
        folders.append(speakers[i] + '_' + speaker_roles[i])
    folders = list(dict.fromkeys(folders))
    
    if commands is False:
        for f in folders:
            os.mkdir(os.getcwd() + '/SCOTUS/' + str(docket) + '_SCOTUS/'+f)
    else:
        return folders
        
def getSplittingAndWriteCommands(docket, speaker_dict):
    for k,v in speaker_dict.items():

        # Establish folder
        folder = '_'.join(k.split('_')[0:-1])
        file_path_out = os.getcwd() + '/SCOTUS/'+docket+'_SCOTUS/'+folder+'/'+k+'.wav'

        # Split wav and put in the right folder
        command = 'ffmpeg -ss '+ str(v[0])+' -t '+ str(str(v[1] - v[0]))+' -i '+ docket+'.wav ' + file_path_out
        os.system(command)
        
        # Create .txt 
        text = v
        start = str(v[0])
        stop = str(v[1])
        # Turn the list of speaker's speech into a string and put it back in the tuple
        speaker_text = v[2]
        speaker_text = ' '.join(speaker_text)

        # Write .txt
        with open(os.getcwd() + '/SCOTUS/'+docket+'_SCOTUS/'+folder+'/'+k+'.txt', "w") as outfile:
            outfile.write(start + ' ' + stop + ' ' + speaker_text)
        
def getSharingCommands(users, data):
    if not users:
        print('No users were selected to share SCOTUS folders with, commands not made')
    else:
        with open(os.getcwd() +'/SCOTUS/sharing_commands.txt', 'w') as sc:
            for user in users:
                for docket in data:
                    sc.write('setfacl -m u:{}:r-x '.format(user)+ os.getcwd() + '/SCOTUS/{}_SCOTUS\n'.format(docket))
                    
                    #get meta data
                    transcript, speakers, speaker_roles, times = getMeta(docket,data)

                    #create speaker dict
                    speaker_dict = getSpeakerDict(transcript, speakers, speaker_roles, times)

                    #create folder for docket and then sub folders (speaker + speaker_role) for each speaker in docket 
                    folders = createFolders(docket, speakers, speaker_roles, times, data, commands = True)
                    
                    for folder in folders:
                        sc.write('setfacl -m u:{}:r-x '.format(user)+ os.getcwd() + '/SCOTUS/{}_SCOTUS/{}/\n'.format(docket, folder))
        print('sharing_commands.txt can be found in SCOTUS, copy and paste all sharing commands in terminal')

def main_script(users, file_path = '/oyez_metadata.json'):
    
    with open(os.getcwd() + file_path) as f:
        data = json.load(f)

    for docket in data:
        #get meta data
        transcript, speakers, speaker_roles, times_new = getMeta(docket,data)

        #create speaker dict
        speaker_dict = getSpeakerDict(transcript, speakers, speaker_roles, times_new)

        #create folder for docket and then sub folders (speaker + speaker_role) for each speaker in docket 
        createFolders(docket, speakers, speaker_roles, times_new, data)

        #split and move to correct folder 
        getSplittingAndWriteCommands(docket, speaker_dict)

    getSharingCommands(users,data)

#update users with netid of those you'd like to have read and execute access
main_script(users = ['igw212', 'anr431'])
