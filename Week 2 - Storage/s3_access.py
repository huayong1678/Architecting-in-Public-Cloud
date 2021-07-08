import boto3
import getpass
def s3_conn():
    access_key = input("Please Provide Access Key: ")
    secret_key = getpass.getpass("Please Provide Secret Key: ")
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-2',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    print("Connection Complete.")
    return s3