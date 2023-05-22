from Connection import client
import os

client = client.CreateClient()

def createIntegration(rest_api, resource_id, URI, Method):
    if URI[:3]=='arn':
        Type= 'AWS'
        Uri=f"arn:aws:apigateway:us-east-2:lambda:path/2015-03-31/functions/{URI}/invocations"
        print("Uri: ",Uri)
    else:
        Type= 'HTTP_PROXY'
        Uri=URI
    #'HTTP_PROXY'
    # URI = 'arn:aws:lambda:us-east-2:674820262647:function:lambda_function'
    # #arn:aws:lambda:us-east-2:674820262647:function:lambda_function:3
    # # Type= 'AWS'
    # Uri=f"arn:aws:apigateway:us-east-2:lambda:path/2015-03-31/functions/{URI}/invocations"

    integration_r = client.put_integration(
        restApiId=rest_api,
        resourceId= resource_id,
        httpMethod=Method,
        type=Type,
        integrationHttpMethod='POST',
        uri= Uri,
        timeoutInMillis=29000
    )
    return integration_r