import config as cof
import json
import time
import csv
import logInToZDP


def createAvroEntity(session):
        with open('createEntityJson.csv') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if row[0] == "createAvroEntity":
                    request=row[1]
                    print(request)
                    requestJson=json.loads(request)
                    print(requestJson)
                    for x in range(cof.AvroEntityCount):
                        print(x)
                        requestJson['businessName'] = 'Avro_Automation_en_500_field'+str(int(time.time()))
                        requestJson['technicalName'] = 'Avro_Automation_en_500_field'+str(int(time.time()))
                        requestJson['sourcePlatform'] = 'Avro_Automation_en_500_field'+str(int(time.time()))
                        requestJson['sourceSchema'] = 'Avro_Automation_en_500_field'+str(int(time.time()))
                        requestJson['tableName'] = 'Avro_Automation_en_500_field'+str(int(time.time()))
                        requestJson['targetSchema'] = cof.targetSchema
                        requestJson['tableProperties']['avro.schema.url'] = cof.avrSchemaPath
                        requestJson['externalDataPath'] = cof.avrExternalDataPath
                        requestJson['externalDataPathValue'] = cof.avrExternalDataPath
                        requestJson['externalDataPathCurrent'] = cof.avrExternalDataPath
                        print(requestJson)
                        URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/projects/"+cof.project+"/entities"
                        print(URL)

                        response=session.post(URL,json=requestJson)
                        print(response.text)
                    #entityTypeId=response.json()["result"]["entityTypeId"]
                    #version=response.json()["result"]["version"]
                    #entityName=response.json()["result"]["technicalName"]
        return

session=logInToZDP.logIn()

createAvroEntity(session)

#print("Entity ID:",entityTypeId)
#print("Entity Version",version)
#print("Entity Name",entityName)

