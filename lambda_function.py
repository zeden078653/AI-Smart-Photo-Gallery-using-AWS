import boto3
import base64
import uuid
import json

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')

UPLOAD_BUCKET = "photo.gallery.upload"
FRONTEND_BUCKET = "photo.gallery.frontend"

def lambda_handler(event, context):
    try:
        # Get the base64-encoded image from 'image' field
        body = json.loads(event['body'])
        image_data_base64 = body['image']
        image_bytes = base64.b64decode(image_data_base64)

        # Save to S3
        image_id = str(uuid.uuid4())
        image_key = f"uploads/{image_id}.jpg"

        s3.put_object(Bucket=UPLOAD_BUCKET, Key=image_key, Body=image_bytes, ContentType="image/jpeg")

        # Rekognition label detection
        response = rekognition.detect_labels(
            Image={'Bytes': image_bytes},
            MaxLabels=5
        )

        labels = [label['Name'] for label in response['Labels']]
        caption = ", ".join(labels)

        # Save caption to frontend bucket
        caption_key = f"captions/{image_id}.txt"
        s3.put_object(Bucket=FRONTEND_BUCKET, Key=caption_key, Body=caption)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Upload and analysis successful',
                'labels': labels,
                'image_s3_url': f"https://{UPLOAD_BUCKET}.s3.amazonaws.com/{image_key}",
                'caption_s3_url': f"https://{FRONTEND_BUCKET}.s3.amazonaws.com/{caption_key}"
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
