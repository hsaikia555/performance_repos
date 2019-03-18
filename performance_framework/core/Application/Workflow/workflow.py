# Author: Himanshu Saikia
# Date: 15/03/2019
# Different functions related to Workflow:

# Create Workflow Function:
import test_repo.performance_framework.core.Application.ZDP_API_LIST.ZDP_API as API


def create_workflow(session, host, port, request_json, protocol, project_id):
    try:
        create_workflow_base_url = API.create_workflow
        create_workflow_base_url = str(create_workflow_base_url.format(str(project_id)))
        print(request_json)
        print(create_workflow_base_url)
        url = protocol+"://"+host+":"+port+create_workflow_base_url
        print(url)
#        url = protocol+"://"+host+":"+port+"/bedrock-app/services/rest/projects/"+project_id+"/workflows"
        response = session.post(url, json=request_json)
        print(response.text)
        wf_id = response.json()['result']['wfId']
        wf_name = response.json()['result']['wfName']
        return wf_id, wf_name
    except Exception as e:
        print("Exception :", e)


# Execute Workflow Function:


def execute_workflow(protocol, host, port, workflow_id, project_id, request_json, session):
    try:
        execute_workflow_base_url = API.execute_workflow
        execute_workflow_base_url = str(execute_workflow_base_url.format(str(workflow_id),str(project_id)))
        print(execute_workflow_base_url)
        print(request_json)
        url = protocol+"://"+host+":"+port+execute_workflow_base_url
#        url = protocol+"://"+host+":"+port+"/bedrock-app/services/rest/workflows/"+str(workflow_id)+"/execute?projectIds="+str(project_id)
        print(url)
        response = session.post(url, json=request_json)
        print(response.text)
        instance_id = response.json()['result']
        return instance_id
    except Exception as e:
        print("Exception :", e)




