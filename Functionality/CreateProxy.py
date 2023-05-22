from utility import create_restAPI, create_integration_response, create_integration, create_method, create_method_response, create_resource
from Config import config
from Functionality import create_lambda_function


def CreateProxy(RestAPI, resourcePath, PROXY_URI):
    if PROXY_URI == '':
        # 3. Create Function
        try:
            functionName = resourcePath[-1]
            createFunc = create_lambda_function.CreateFunction(functionName)
            print("Function ARN: ", createFunc)
            PROXY_URI = createFunc
        except Exception as ae:
            return f"Exception occurred while creating the Lambda function- {ae}"
    try:
        # 1. createResource
        try:
            API_ID = create_restAPI.Check_rest_api(RestAPI)
            response = create_resource.check_resources(API_ID,
                                                       resourcePath
                                                       )
            print("Resource Response:", response)
            print(response["Status"])

            if response["Status"] == 400:
                response = {
                    "Status": 400,
                    "RestAPI_ID": API_ID
                }
                return response
            else:
                try:
                    # 2. CreateMethod
                    method = create_method.CreateMethod(API_ID,
                                                        response['PARENT_ID'],
                                                        config.METHOD,
                                                        config.AUTHORIZATION
                                                        )
                    print("Create Method Response:", method)
                    try:
                        # # 3. Create Function
                        # createFunc= create_lambda_function.CreateFunction()
                        # print("Function ARN: ",createFunc)
                        # PROXY_URI=createFunc
                        # 4. CreateIntegration
                        integration = create_integration.createIntegration(API_ID,
                                                                           response['PARENT_ID'],
                                                                           PROXY_URI,
                                                                           config.METHOD
                                                                           )
                        print("Create Integration Response: ", integration)

                        try:
                            # 4 CreateResponse
                            methodResponse = create_method_response.MethodResponse(API_ID,
                                                                                   response['PARENT_ID'],
                                                                                   config.METHOD
                                                                                   )
                            print("Method Response:", methodResponse)
                            # return response
                            # Create Integration Response
                            try:
                                integrationResponse = create_integration_response.put_integration_response(API_ID,
                                                                                                           response['PARENT_ID'],
                                                                                                           config.METHOD
                                                                                                           )
                                print("Integration response: ",
                                      integrationResponse)
                                response = {
                                    "Status": 200,
                                    "RestAPI_ID": API_ID
                                }
                                return response
                            except Exception as intex:
                                return f"Exception Occurred while putting integration response: {intex}"
                        except Exception as mrex:
                            return f"Exception Occurred while creating Response: {mrex}"
                    except Exception as inex:
                        return f"Exception Occurred while creating Integration: {inex}"
                except Exception as mex:
                    return f"Exception Occurred while creating Method: {mex}"
        except Exception as rex:
            return f"Exception Occurred while creating Resource: {rex}"
    except Exception as ex:
        return f"Exception Occurred: {ex}"
