import config as cof
import json
import time
import csv
import logInToZDP
import sys
csv.field_size_limit(2147483647)





def createDelimitedEntity(session):
  #  maxInt = sys.maxsize
   # decrement = True
   # while decrement:
    #    decrement = False
     #   try:
      #      csv.field_size_limit(maxInt)
            with open('createEntityJson.csv') as csv_file:
                csv_reader=csv.reader(csv_file,delimiter=',')
                for row in csv_reader:
                    if row[0] == "createDelimitedEntity":
                        request=row[1]
                        print("Printing Request Json")
                        print(request)
                        requestJson=json.loads(request)
                        print(requestJson)
                        for x in range(cof.DelimitedEntityCount):
                            print(x)
                            requestJson['businessName'] = 'Delimited_Automation_en_500_field'+str(int(time.time()))
                            requestJson['technicalName'] = 'Delimited_Automation_en_500_field'+str(int(time.time()))
                            requestJson['sourcePlatform'] = 'Delimited_Automation_en_500_field'+str(int(time.time()))
                            requestJson['sourceSchema'] = 'Delimited_Automation_en_500_field'+str(int(time.time()))
                            requestJson['tableName'] = 'Delimited_Automation_en_500_field'+str(int(time.time()))
                            requestJson['targetSchema'] = cof.targetSchema
                            requestJson['externalDataPath'] = cof.DelimitedExternalDataPath
                            requestJson['externalDataPathValue'] = cof.DelimitedExternalDataPath
                            requestJson['externalDataPathCurrent'] = cof.DelimitedExternalDataPath
                            print(requestJson)
                            URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/projects/"+cof.project+"/entities"
                            print(URL)

                            response=session.post(URL,json=requestJson)
                            print(response.text)
                    #entityTypeId=response.json()["result"]["entityTypeId"]
                    #version=response.json()["result"]["version"]
                    #entityName=response.json()["result"]["technicalName"]
       # except OverflowError:
        #    maxInt = int(maxInt/10)
         #   decrement = True
            return

session=logInToZDP.logIn()
createDelimitedEntity(session)

#print("Entity ID:",entityTypeId)
#print("Entity Version",version)
#print("Entity Name",entityName)

