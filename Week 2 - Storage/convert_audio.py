import sys
import pandas as pd
from os import path
from pydub import AudioSegment

def create_convert_list(s3):
    mpeg_list = ['file_1.mp3', 'file_2.mp3']
    # for obj in s3.Bucket('mpeg-sound').objects.all():
    #     mpeg_list.append(obj.key)
    return mpeg_list

def audio_convert(src):
    wav_list=list()
    for i in range(1, len(src)+1):
        dst = "wav-sound/file_" + str(i) + ".wav"
        wav_list.append("file_" + str(i) + ".wav")
        sound = AudioSegment.from_mp3('mpeg-sound/' + src[i-1])
        sound.export(dst, format="wav")
    return wav_list