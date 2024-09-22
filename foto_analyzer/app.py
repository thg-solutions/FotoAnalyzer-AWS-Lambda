import json
import base64
import io
from exif import get_image_data


def lambda_handler(event, context):

    print('FotoAnalyzer')
    body = event['body']
    enc = event['isBase64Encoded']
    print('isBase64Encoded: ' + str(enc))

    body_decoded = base64.b64decode(body)
    # die folgenden zwei Zeilen sind völlig überflüssig, scheinen aber eine
    # Sychronisation auszulösen
    print('len(body_decoded): ' + str(len(body_decoded)))
    bytestream = io.BytesIO(body_decoded)
 
    image_data = get_image_data(bytestream)
    assert isinstance(image_data, dict)

    return {
        "statusCode": 200,
        "body": json.dumps(image_data)
    }