from Connection import client
import os

client = client.CreateClient() 

def CreateMethod(restApi, resource_id, Method, Authorization):
    response = client.put_method(
        restApiId=restApi,
        resourceId=resource_id,
        httpMethod=Method,
        authorizationType=Authorization,
        apiKeyRequired=False
    )

    return response