import convert_audio as ca
import s3_access as s3a
import botocore
import logging
import boto3
from botocore.exceptions import ClientError

# ในกรณีที่ต้องการเปลี่ยนชื่อ bucket
mpeg_bucket, wav_bucket = 'mpeg-sound', 'wav-sound'


def sound_etl():
    """
    ใช้ในการดึง แปลง และโหลดข้อมูล จาก S3
    """
    # Create connection to s3
    s3 = s3a.s3_conn()

    def extract_audio():
        """
        ใช้ในการดึงข้อมูลจาก S3 ที่ใช้เก็บไฟล์ mpeg เพื่อนำมาเซฟไว้ใน EBS ของ EC2 โดยจะทำการสร้าง list ของชื่อไฟล์ไว้ก่อนเป็น mpeg_list

        Raises:
            try: ลองดึง objects ทุกตัวที่อยู่ใน S3 bucket ชื่อ mpeg-sound
            except: ถ้าหา object ไม่เจอจะมี response กลับมาเป็น 404

        Notes:
            ดูข้อมูลเพิ่มเติมได้ที่ https://boto3.amazonaws.com/v1/documentation/api/1.9.42/guide/s3-example-download-file.html
        """
        mpeg_list = ca.create_convert_list(s3)
        try:
            print("Downloading file(s)...")
            for i in range(len(mpeg_list)):
                des, src = "mpeg-sound/" + mpeg_list[i], mpeg_list[i]
                # บรรทัดนี้จะเป็นคำสั่งในการโหลดไฟล์จาก S3
                s3.Bucket(mpeg_bucket).download_file(src, des)
            print("Download Completed.")
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise
        transform_audio(mpeg_list)

    def transform_audio(mpeg_list):
        """
        ใช้ในการแปลงไฟล์เสียงจาก mpeg ไปเป็น wav โดยจะทำการเรียกฟังก์ชั่น Convert_audio มาใช้

        Args:
            mpeg_list: เป็น list ที่ถูกสร้างขึ้นมาจากการดึงชื่อไฟล์สกุล mpeg บน S3

        Raise:
            try: ลองแปลงไฟล์เสียงโดยเจาะจงให้ไฟล์เสียงที่จะแปลงต้องเป็น .mp3
            except: เมื่อมีความผิดพาดขึ้นจะส่งข้อความเตือนออกมา เช่น สกุลไฟล์ผิดประเภท
        
        Notes:
            ดูฟังก์ชั่นในการแปลงไฟล์ได้ที่ convert_audio.py
        """
        try:
            print("Converting file(s)...")
            wav_list = ca.audio_convert(mpeg_list)
            print("Convert Completed.")
        except:
            print("Convert Error.")
        load_audio(wav_list)

    def load_audio(wav_list):
        """
        ใช้ในการอัพโหลดไฟล์ wav ที่แปลงและเก็บไว้ใน EBS ขึ้นไปบน S3

        Args:
            wav_list: เป็นลิสต์รายชื่อของไฟล์ที่ทำการแปลงแล้ว

        Raises:
            try: ลองอัพโหลดไฟล์ขึ้น S3
            except: เมื่อมีข้อผิดพลาดจะมีข้อความเตือนและส่ง logging เข้าระบบ
        
        Notes:
            ดูเพิ่มเติมได้ที่ https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
        """
        try:
            print("Uploading file(s)...")
            for i in range(len(wav_list)):
                src = "wav-sound/" + wav_list[i]
                # บรรทัดนี้จะเป็นคำสั่งในการโหลดไฟล์ขึ้น S3
                s3.Bucket(wav_bucket).upload_file(src, wav_list[i])
            print("Upload Completed.")
        except ClientError as e:
            print("Upload Error.")
            print(logging.error(e))
            return False
        return True
    extract_audio()

sound_etl()
