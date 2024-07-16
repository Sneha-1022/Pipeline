import logging
import json

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Lambda function invoked")
    return {
        'statusCode': 200,
        'body': json.dumps("Hello, World!")
    }

