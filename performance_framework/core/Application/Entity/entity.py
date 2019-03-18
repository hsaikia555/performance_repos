# Author: Himanshu Saikia
# Date: 15/03/2019
# Different functions related to Entity:

# Create Entity Function:
import test_repo.performance_framework.core.Application.ZDP_API_LIST.ZDP_API as API


def create_entity(protocol, host, port, session, request_json, project_id):
    try:
        create_entity_base_url = API.create_entity
        create_entity_base_url = str(create_entity_base_url.format(str(project_id)))
        print(create_entity_base_url)
#        url = protocol+"://"+host+":"+port+"/bedrock-app/services/rest/projects/"+project_id+"/entities"
        url = protocol+"://"+host+":"+port+create_entity_base_url
        print(url)
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
        delete_entity_base_url = API.delete_entity
        delete_entity_base_url = str(delete_entity_base_url.format(str(entity_id), str(project_id)))
        print(delete_entity_base_url)
        url = protocol+"://"+host+":"+port+delete_entity_base_url
        print(url)
#        url=protocol+"://"+host+":"+port+"bedrock-app/services/rest/entities/"+entity_id+"?projectIds="+project_id+""
        response = session.delete(url)
    except Exception as e:
        print("Exception :", e)
