import sys
from os import path
from pydub import AudioSegment

def create_convert_list(s3, mpeg_bucket):
    """
    ใช้สร้างลิสท์ที่ใช้ในการเก็บชื่อไฟล์ mpeg ที่อยู่ใน s3 ทั้งหมด

    Args:
        s3: เป็น object ที่คืนค่ามาจากฟังก์ชั่น s3_access ใช้ฝนการเชื่อมต่อกับ AWS S3

    Notes:
        - ฟังก์ชั่นจะดึงข้อมูลเฉพาะไฟล์ที่มีสกุลลงท้ายด้วย .mp3 เท่านั้น
        - ถ้าใช้ OSX หรือ MacOS จะเกิด error ขึ้นเนื่องจากหา package ffmpeg ไม่เจอให้ดูเพิ่มเติมจากในนี้ครับ
            https://stackoverflow.com/questions/56739322/pydub-cant-find-ffmpeg-although-its-installed-and-in-path
        - สำหรับบน EC2 ที่เป็น AMI ดูเพิ่มเติมได้ที่
            https://maskaravivek.medium.com/how-to-install-ffmpeg-on-ec2-running-amazon-linux-451e4a8e2694
    """
    mpeg_list = list()
    for obj in s3.Bucket(mpeg_bucket).objects.all():
        obj_name=obj.key
        if obj_name.find(".mp3")!=-1:
            mpeg_list.append(obj_name)
    return mpeg_list

def audio_convert(src):
    """
    ใช้ในการแปลงไฟล์ที่มีสกุล .mp3 ไฟเฟ็น .wav แล้วทำการรันชื่อไฟล์ตามลำดับ พร้อมเซฟลง storage

    Args:
        src: เป็นรายชื่อของไฟล์ที่ต้องการจะแปลง
    """
    wav_list=[]
    for i in range(1, len(src)+1):
        dst = "wav-sound/file_" + str(i) + ".wav"
        wav_list.append("file_" + str(i) + ".wav")
        sound = AudioSegment.from_mp3('mpeg-sound/' + src[i-1])
        sound.export(dst, format="wav")
    return wav_list