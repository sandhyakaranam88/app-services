from flask import Flask, request
import boto3
import os

app = Flask(__name__)
sqs = boto3.client('sqs')
queue_url = os.environ.get('QUEUE_URL')

@app.route('/send', methods=['POST'])
def send():
    msg = request.form['message']
    sqs.send_message(QueueUrl=queue_url, MessageBody=msg)
    return f"Message sent to SQS: {msg}", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
