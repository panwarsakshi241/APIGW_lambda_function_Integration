from Connection import client

client = client.CreateClient()


def Check_rest_api(RestAPI):
    getAPIs = client.get_rest_apis(limit=15)
    APIs = getAPIs['items'] 
    id=''
    for items in APIs:
        if items['name'] == RestAPI:
            id=items['id']
            return id    
    CreateRestAPI(RestAPI)

def CreateRestAPI(RestAPI):   
    try:
        response = client.create_rest_api(
            name=RestAPI,
            description="RestAPI",
            apiKeySource='HEADER',
            endpointConfiguration={
                'types': [
                    'REGIONAL',
                ],
                'vpcEndpointIds': []
            },
            disableExecuteApiEndpoint=False
        )
        return response['id']
    except Exception as ex:
        return f"exception occurred- {ex}"
