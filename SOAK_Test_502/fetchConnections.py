import json
import time
import SOAK_Test_502.config as cof
import csv




def fetch_connections(sessions):
    try:
        with open('json_input_file.csv') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if row[0] == "fetchConnectionsJson":
                    request=row[1]
                    URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/ingestion/filesystems/connections/search"
                    print(request)
                    requestJson=json.loads(request)
                    print(requestJson)
                    response = sessions.post(URL, json=requestJson)
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
                                    connection_id=result_list[i]['connectionInstanceId']
                                    break
                                else:
                                    connection_id=create_connection(sessions)
                    else:
                        print("Error while fetching connection details: ")
                        exit()

        return connection_id
    except Exception as e:
        print("Some Exception has been found:",e)
def create_connection(sessions):
    try:
        with open('json_input_file.csv') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if row[0] == "createConnectionJson":
                    request=row[1]
                    URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/ingestion/filesystems/"+cof.FILE_SYSTEM_ID+"/connections"
                    print(URL)
                    print(request)
                    requestJson=json.loads(request)
                    print(requestJson)
                    requestJson['fileSystemUri'] = cof.FILE_SYSTEM_URI
                    requestJson['connectionInstanceName'] = 'HDFS_Connection_'+time.strftime('%Y%m%d%H%M%S')
                    print(requestJson)
                    response=sessions.post(URL,json=requestJson)
                    print(response.text)
                    if int(response.json()['status']['responseCode']) == 200:
                        print("Successful")
                        connection_instance_id=response.json()['status']['result']
                    else:
                        print("Unsuccessful")
                        exit()

        return connection_instance_id
    except Exception as e:
        print("Some Exception has been found:",e)
