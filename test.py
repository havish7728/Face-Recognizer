from dotenv import load_dotenv
import os
import boto3

load_dotenv()

region = os.getenv('AWS_REGION')
access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

rekognition = boto3.client(
    'rekognition',
    region_name=region,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)
s3 = boto3.client('s3', region_name='ap-south-1', 
                  aws_access_key_id=access_key, 
                  aws_secret_access_key=secret_key)
try:
    response = s3.head_object(Bucket='face-recognizer-heruko', Key='test/elon_test.jpg')
    print("Metadata found:", response['Metadata'])
except Exception as e:
    print("Error accessing object:", e)

