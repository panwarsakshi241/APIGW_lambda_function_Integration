import boto3
import uuid

_client = boto3.client('lambda', 'us-east-2')

# ZIPNAME = f"code/{functionName}.zip"
#service-role/MySampleFunction-role-l35ez301'

def aws_file(functionName):
    ZIPNAME = f"code/{functionName}.zip"
    with open(ZIPNAME, 'rb') as file_data:
        bytes_content = file_data.read()
    return bytes_content

def CreateFunction(functionName):
    Handler=f"{functionName}.lambda_handler"
    try:
        response = _client.create_function(
            FunctionName=functionName,
            Runtime='python3.9',
            Role=f'arn:aws:iam::674820262647:role/service-role/MySampleFunction-role-l35ez301',
            Handler=Handler,
            Code={
                'ZipFile': aws_file(functionName)
            },
            Description='Lambda Function using boto3',
            Timeout=3,
            Publish=True,
        )
        arn=response['FunctionArn']
        try:
            addP=AddPermission(functionName)
        except Exception as apex:
            return f"Exception Occurred while adding the permission: {apex}"
    except Exception as c:
        response = _client.update_function_code(
            FunctionName=functionName,
            ZipFile=aws_file(),
            Publish=True,
            Architectures=[
                'x86_64',
            ]
        )
        arn=response['FunctionArn']
        l=arn.rfind(":")
        arn=arn[:l]
    print(response)
    print("Funcition ARN : ",arn)
    return arn

def AddPermission(functionName):
    try:
        pr_response = _client.add_permission(
            FunctionName=functionName,
            StatementId= uuid.uuid1().hex,
            Action='lambda:InvokeFunction',
            Principal='apigateway.amazonaws.com'
        )
        print("Permission Response: ",pr_response)
    except Exception as ex:
        return f"Exception occurred while adding permission to lambda function: {ex}"
    return pr_response