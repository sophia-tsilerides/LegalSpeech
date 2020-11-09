import os

path = "./icsi_files/"
folders = os.listdir(path)

for folder in os.listdir(path):
    for file in os.listdir(path+folder+'/'):
        if '.wav' in file:
            if os.path.getsize(path+folder+'/'+file)<40000:
                os.remove(path+folder+'/'+file)
                os.remove(path+folder+'/'+file.strip('.wav')+'.txt')