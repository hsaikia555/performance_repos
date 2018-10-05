import requests
import json
import config as cof
import time
import csv


def fetchLZServers(session):
    URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/ingestion/publish/retrieveLandingZoneServers"
    print(URL)
    response=session.get(URL)
    print(response.text)
    result_list=response.json()['result']['data']
    print(result_list)
    for i in range(len(result_list)):
        if result_list[i]['ipAddress'] == cof.HOST:
            serverId=result_list[i]['serverId']
            print(serverId)
            break
        else:
            print("LZ server not found:")
    return serverId

def createLZDir(session,serverId):
    try:
        with open('json_input_file.csv') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if row[0] == "createLZServerJson":
                    request=row[1]
                    print(serverId,"Server ID.....")
                    print(request)
                    requestJson=json.loads(request)
                    print(requestJson)
                    requestJson['serverId']=serverId
                    requestJson['dirPath']=cof.LOCAL_BASE_DIRECTORY+"LZ_"+time.strftime('%Y%m%d%H%M%S')
                    print(requestJson)
                    URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/ingestion/saveLZDirectories"
                    print(URL)
                    print(requestJson['dirPath'])
                    response=session.post(URL,json=requestJson)
                    print(response.text)
                    lzDirId=response.json()['status']['result']
        return lzDirId
    except Exception as e:
        print("Some Exception has been found:",e)


