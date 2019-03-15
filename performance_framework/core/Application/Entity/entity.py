# Author: Himanshu Saikia
# Date: 15/03/2019
# Different functions related to Entity:

# Create Entity Function:


def create_entity(protocol, host, port, session, request_json, project_id):
    try:
        print(request_json)
        url = protocol+"://"+host+":"+port+"/bedrock-app/services/rest/projects/"+project_id+"/entities"
        response = session.post(url, json=request_json)
        print(response.text)
        entity_type_id = response.json()["result"]["entityTypeId"]
        version = response.json()["result"]["version"]
        entity_name = response.json()["result"]["technicalName"]
        return entity_type_id, version, entity_name
    except Exception as e:
        print("Exception :", e)


# Delete Entity Function:


def delete_entity(protocol, host, port, session, entity_id, project_id):
    try:
        url=protocol+"://"+host+":"+port+"bedrock-app/services/rest/entities/"+entity_id+"?projectIds="+project_id+""
        response = session.delete(url)
    except Exception as e:
        print("Exception :", e)
