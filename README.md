# Face Recognition using AWS Rekognition

A Python project that uses AWS Rekognition to detect and compare faces in images stored in an S3 bucket.

---

## Features

- Detect faces in an image using AWS Rekognition.
- Compare faces between two images to find matches.
- Uses `boto3` for AWS SDK integration.
- Loads AWS credentials securely from a `.env` file.

---

## Prerequisites

- Python 3.x
- AWS account with Rekognition and S3 access
- AWS credentials with Rekognition and S3 permissions
- Python packages: `boto3`, `python-dotenv`

---

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/face-recognition-aws.git
   cd face-recognition-aws
    ````

2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up AWS credentials**

   Create a `.env` file in the project root:

   ```env
   AWS_ACCESS_KEY_ID=your_access_key_id
   AWS_SECRET_ACCESS_KEY=your_secret_access_key
   AWS_REGION=your_aws_region
   ```

5. **Upload images to your S3 bucket**

   Ensure your images are uploaded to the specified bucket, and update the image paths in `face_recognizer.py`.

---

## Usage

Run the script to detect and compare faces:

```bash
python face_recognizer.py
```

Example output:

```
Faces detected in source image: 1
Number of face matches found: 1
Face matched with 98.75% similarity
```

---

## Troubleshooting

* **InvalidS3ObjectException**: Check your bucket name, image keys, and permissions.
* **NoCredentialsError**: Ensure AWS credentials are correctly set in `.env` and loaded.
* Verify IAM user permissions for Rekognition and S3 (`rekognition:*`, `s3:GetObject`).

---


## Acknowledgments

* AWS Rekognition documentation: [https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html)
* boto3 AWS SDK: [https://boto3.amazonaws.com/v1/documentation/api/latest/index.html](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

```