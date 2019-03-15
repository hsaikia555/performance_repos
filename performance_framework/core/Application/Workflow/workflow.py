# Author: Himanshu Saikia
# Date: 15/03/2019
# Different functions related to Workflow:

# Create Workflow Function:


def create_workflow(session, host, port, request_json, protocol, project_id):
    try:
        print(request_json)
        url = protocol+"://"+host+":"+port+"/bedrock-app/services/rest/projects/"+project_id+"/workflows"
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
        print(request_json)
        url = protocol+"://"+host+":"+port+"/bedrock-app/services/rest/workflows/"+str(workflow_id)+"/execute?projectIds="+str(project_id)
        print(url)
        response = session.post(url, json=request_json)
        print(response.text)
        instance_id = response.json()['result']
        return instance_id
    except Exception as e:
        print("Exception :", e)




