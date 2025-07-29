from flask import Flask, request
import boto3
import os

app = Flask(__name__)
s3 = boto3.client('s3')
bucket_name = os.environ.get('UPLOADS_BUCKET')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    s3.upload_fileobj(file, bucket_name, file.filename)
    return f"Uploaded {file.filename} to S3 bucket {bucket_name}", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
