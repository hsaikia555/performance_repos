import json
import time
import SOAK_Test_502.config as cof




def fetch_connections(sessions):
    URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/ingestion/filesystems/connections/search"
    request_json={
        "currentPage": 1,
        "chunkSize": 10,
        "sortBy": "modifiedTime",
        "orderBy": "DESC",
        "searchCriteria": []
}
    response = sessions.post(URL, json=request_json)
    print(response.text)
    if int(response.status_code) == 200:
        print("Status code: 200")
        result_list = response.json()["result"]["resultList"]
        print(result_list)
        if len(result_list) == 0:
            print("List is empty: ")
            connection_id=create_connection(sessions)
        else:
            for i in range(len(result_list)):
                if result_list[i]['fileSystemUri'] == cof.FILE_SYSTEM_URI and int(result_list[i]['fileSystemId']) == int(cof.FILE_SYSTEM_ID):
                #print(result_list[i]['fileSystemUri'])
                #print(result_list[i]['fileSystemId'])
                #print(cof.FILE_SYSTEM_URI)
                #print(cof.FILE_SYSTEM_ID)
                    connection_id=result_list[i]['connectionInstanceId']
                    break
                else:
                    connection_id=create_connection(sessions)
        #print(result_list[1]['connectionInstanceId'])
        #print(result_list)
    else:
        print("Error while fetching connection details: ")
        exit()

    return connection_id
def create_connection(sessions):
    URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/ingestion/filesystems/"+cof.FILE_SYSTEM_ID+"/connections"
    print(URL)
    request_json={
        "connectionInstanceId":0 ,
        "fileSystemUri": cof.FILE_SYSTEM_URI,
        "connectionInstanceName": "test_connection123",
        "fileSystemProperties": [],
        "scope": "PUBLIC",
        "description": "This is a test connection."
}
    response=sessions.post(URL,json=request_json)
    print(response.text)
    if int(response.json()['status']['responseCode']) == 200:
        print("Successful")
    else:
        print("Unsuccessful")
        exit()
    connection_instance_id=response.json()['status']['result']
    return connection_instance_id
