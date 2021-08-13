import boto3

def s3_conn():
    """
    เชื่อมต่อกับ AWS Resource ผ่าน module boto3 โดยจะต้องมีการระบุ Access key และ Secret key และมีการระบุ region us-east-2 เป็นค่าเริ่มต้น
    แล้วจะทำการคืนค่าออกมาเป็น s3 ซึ่งประกอบไปด้วย credentials สำหรับใช้ในการเชื่อมต่อกับ AWS

    Returns:
        s3: เป็น boto3.resource ประกอบไปด้วย service_name, region_name, aws_access_key_id, aws_secret_access_key

    Notes:
        ดูข้อมูลเพิ่มเติมได้ที่ https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html
    """
    region = "us-east-1"
    s3 = boto3.resource(
        service_name='s3',
        region_name=region
    )
    print("Connection Complete.")
    return s3