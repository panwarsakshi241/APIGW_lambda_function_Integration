from Connection import client
import os

client = client.CreateClient()
# vkl5visc07.execute-api.us-east-2.amazonaws.com


def CreateDeployment(rest_api, stage_name):
    Deployment_response = client.create_deployment(
        restApiId=rest_api,
        stageName=stage_name,
        stageDescription='SIT 01 environment',
        description='Creating and Deploying the Rest API using Python SDK',
        cacheClusterEnabled=False,
        variables={
            'url': 'vkl5visc07.execute-api.us-east-2.amazonaws.com'
        },
        tracingEnabled=False
    )
    return Deployment_response
