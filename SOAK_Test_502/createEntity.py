import requests
import json
import SOAK_Test_502.config as cof
import time
import csv


def createEntity(session,ruleId,ruleName):
    try:
        with open('json_input_file.csv') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if row[0] == "createEntityJson":
                    request=row[1]
                    print(request)
                    requestJson=json.loads(request)
                    requestJson['businessName'] = 'SOAK_Test_Entity'+time.strftime('%Y%m%d%H%M%S')
                    requestJson['technicalName'] = 'SOAK_Test_Entity'+time.strftime('%Y%m%d%H%M%S')
                    requestJson['sourcePlatform'] = 'SOAK_Test_Entity'+time.strftime('%Y%m%d%H%M%S')
                    requestJson['sourceSchema'] = 'SOAK_Test_Entity'+time.strftime('%Y%m%d%H%M%S')
                    requestJson['tableName'] = 'SOAK_Test_Entity'+time.strftime('%Y%m%d%H%M%S')
                    requestJson['targetSchema'] = 'SOAK_Test_Entity'+time.strftime('%Y%m%d%H%M%S')
                    print("Fields-----")
                    fields_list=requestJson['fields']
                    for i in range(len(fields_list)):
                        if len(fields_list[i]['ruleMappings']) != 0:
                            rule_list=fields_list[i]['ruleMappings']
                    rule_list[0]['ruleId']=ruleId
                    rule_list[0]['ruleName']=ruleName
                    print(requestJson)
                    URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/projects/"+cof.project+"/entities"
                    response=session.post(URL,json=requestJson)
                    print(response.text)
                    entityTypeId=response.json()["result"]["entityTypeId"]
                    version=response.json()["result"]["version"]
                    entityName=response.json()["result"]["technicalName"]
        return entityTypeId,version,entityName
    except Exception as e:
        print("Some Exception has been found:",e)

