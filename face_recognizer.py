import boto3
import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")

rekognition = boto3.client(
    'rekognition',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

bucket = 'face-recognizer-heruko'
source_image = 'faces/elon_face.jpeg'
target_image = 'test/elon_test.jpg'

def detect_faces(bucket, image_key):
    response = rekognition.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': image_key,
            }
        },
        Attributes=['ALL']
    )
    return response['FaceDetails']

def compare_faces(bucket, source_key, target_key):
    response = rekognition.compare_faces(
        SourceImage={'S3Object': {'Bucket': bucket, 'Name': source_key}},
        TargetImage={'S3Object': {'Bucket': bucket, 'Name': target_key}},
        SimilarityThreshold=80
    )
    return response['FaceMatches']

faces = detect_faces(bucket, source_image)
print(f"Faces detected in source image: {len(faces)}")

matches = compare_faces(bucket, source_image, target_image)
print(f"Number of face matches found: {len(matches)}")

for match in matches:
    similarity = match['Similarity']
    print(f"Face matched with {similarity:.2f}% similarity")