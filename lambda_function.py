import json

def lambda_handler(event, context):
    name = event.get("name", "Student")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Hello, {name}! AWS Lambda жұмыс істеп тұр."
        })
    }