from Functionality import CreateProxy, create_lambda_function
from Deployment import deployment
from Config import config


def SampleAPI():
    response = CreateProxy.CreateProxy(config.RESTAPI_NAME,
                                       config.SAMPLE_RESOURCE_PATH,
                                       config.SAMPLE_URI)
    print(response)
    deploy = deployment.CreateDeployment(response['RestAPI_ID'],
                                         config.STAGE) 
    return response