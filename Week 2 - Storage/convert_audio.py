import sys
from os import path
from pydub import AudioSegment

# ในกรณีที่ต้องการเปลี่ยนชื่อ bucket
mpeg_bucket, wav_bucket = 'mpeg-sound', 'wav-sound'

def create_convert_list(s3):
    """
    ใช้สร้างลิสท์ที่ใช้ในการเก็บชื่อไฟล์ mpeg ที่อยู่ใน s3 ทั้งหมด

    Args:
        s3: เป็น object ที่คืนค่ามาจากฟังก์ชั่น s3_access ใช้ฝนการเชื่อมต่อกับ AWS S3

    Notes:
        ใน S3 จำเป็นต้องเป็นไฟล์สกุล mpeg ทั้งหมดเท่านั้น !!!เพราะไม่ได้เขียนดักเคสเอาไว้!!!
    """
    mpeg_list = list()
    for obj in s3.Bucket(mpeg_bucket).objects.all():
        mpeg_list.append(obj.key)
    return mpeg_list

def audio_convert(src):
    """
    ใช้ในการแปลงไฟล์ที่มีสกุล .mp3 ไฟเฟ็น .wav แล้วทำการรันชื่อไฟล์ตามลำดับ พร้อมเซฟลง storage

    Args:
        src: เป็นรายชื่อของไฟล์ที่ต้องการจะแปลง
    """
    wav_list=list()
    for i in range(1, len(src)+1):
        dst = "wav-sound/file_" + str(i) + ".wav"
        wav_list.append("file_" + str(i) + ".wav")
        sound = AudioSegment.from_mp3('mpeg-sound/' + src[i-1])
        sound.export(dst, format="wav")
    return wav_list