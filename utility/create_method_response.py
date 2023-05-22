from Connection import client

client = client.CreateClient()

def MethodResponse(rest_api,resource_id, Method):
    response = client.put_method_response(
        restApiId=rest_api,
        resourceId=resource_id,
        httpMethod=Method,
        statusCode='200',
        responseModels={
            'application/json': 'Empty'
            }
        )
    return response