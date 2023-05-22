from Connection import client

client = client.CreateClient() 

def check_resources(api_id,path_lst):
    get_resource = client.get_resources(restApiId=api_id)
    resources =get_resource['items']
    PARENT_ID =''
    PATH='/'
    Root_resource_id=''
    for path_part in path_lst:
        fg=0
        PATH=f"{PATH}{path_part}"
        print(PATH)
        for items in resources:
            if items['path']==PATH:
                fg=1
                PARENT_ID = items['id']
                PATH=f"{PATH}/"
            if items['path']=='/':
                Root_resource_id=items['id']
        if fg==0:
            if PARENT_ID=='':
                PARENT_ID=Root_resource_id
                print("Root_ID: ",Root_resource_id)
            else:
                index=path_lst.index(path_part)
                print(path_part)
                print(index)
                path_lst=path_lst[index:]
                print("path_lst: ",path_lst)
            break
    
    if fg==1:
        response={
            "Status":400,
            "Message":"Already Exists"
        }
        print(response)
    else:
        for path_part in path_lst:
           ID=CreateResource(api_id,PARENT_ID,path_part)
           PARENT_ID=ID
        response = {
            "Status":200,
            "PARENT_ID":PARENT_ID
        }
    return response

def CreateResource(restApi,parentId,path): 
    cr_response=client.create_resource(
        restApiId=restApi,
        parentId=parentId,
        pathPart=path
    )
    resource_id= cr_response['id']
    return resource_id