from Connection import client

client = client.CreateClient()

def put_integration_response(rest_api,resource_id, Method):
    response = client.put_integration_response(
        restApiId=rest_api,
        resourceId=resource_id,
        httpMethod=Method,
        statusCode='200'
    )

    return response