import os,sys
import soundfile as sf
path = "/Users/chiragmandot/Downloads/ESCMaster/"
for i in os.listdir(path):
    os.mkdir('/Users/chiragmandot/AtntHackathon/data/fulldata/'+i.split('-')[1].replace(' ',''))
    new_dir = '/Users/chiragmandot/AtntHackathon/data/fulldata/'+i.split('-')[1].replace(' ','')+'/'
    for j in os.listdir(path+i):
        data, samplerate = sf.read(path+i+'/'+j)
        sf.write(new_dir+j.split('.')[0]+'.wav', data, samplerate)

