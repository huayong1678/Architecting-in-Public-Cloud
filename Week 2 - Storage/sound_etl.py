import convert_audio as ca
import s3_access as s3a
import botocore
import logging
import boto3
from botocore.exceptions import ClientError
def sound_etl():
    # Create connection to s3
    s3 = s3a.s3_conn()
    # Extract audio files from S3
    def extract_audio():
        mpeg_list = ca.create_convert_list(s3)
        try:
            print("Downloading file(s)...")
            for i in range(len(mpeg_list)):
                des, src = "mpeg-sound/" + mpeg_list[i], mpeg_list[i]
                s3.Bucket('mpeg-sound').download_file(src, des)
            print("Download Completed.")
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise
        transform_audio(mpeg_list)
    # Transform audio files
    def transform_audio(mpeg_list):
        try:
            print("Converting file(s)...")
            wav_list = ca.audio_convert(mpeg_list)
            print("Convert Completed.")
        except:
            print("Convert Error.")
        load_audio(wav_list)
    # Load audio files to S3
    def load_audio(wav_list):
        try:
            print("Uploading file(s)...")
            for i in range(len(wav_list)):
                src = "wav-sound/" + wav_list[i]
                s3.Bucket('wav-sound').upload_file(src, wav_list[i])
            print("Upload Completed.")
        except ClientError as e:
            print("Upload Error.")
            print(logging.error(e))
            return False
        return True
    extract_audio()
sound_etl()
