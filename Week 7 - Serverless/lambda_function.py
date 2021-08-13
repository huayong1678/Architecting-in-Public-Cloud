import boto3
import sound_etl as runner

def lambda_handler(event, context):
    # TODO implement
    
    runner.sound_etl()