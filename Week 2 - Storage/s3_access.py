import boto3

def s3_conn():
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-2',
        aws_access_key_id='AKIA3X5D7TSZBLERDV44',
        aws_secret_access_key='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'
    )
    return s3
