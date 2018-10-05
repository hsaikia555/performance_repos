import json
import config as cof
import time
import csv
def createFilePattern(session,lzDirId,wfId,connection_id):
    try:
        with open('json_input_file.csv') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if row[0] == "createFilePatternJson":
                    request=row[1]
                    print("LZ Dir ID.....",lzDirId,"Workflow ID....",wfId,"HDFS Connection ID...",connection_id)
                    print(request)
                    requestJson=json.loads(request)
                    print(requestJson)
                    requestJson['destination']=cof.WF_BASE_PATH+"Ingestion_destination_"+time.strftime('%Y%m%d%H%M%S')
                    requestJson['workflowId']=wfId
                    requestJson['fileSystemConnectionInstanceId']=connection_id
                    lzDirList=requestJson['lzDirectories']
                    lzDirList[0]['lzDirId']=lzDirId
                    print(requestJson)
                    URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/projects/"+cof.project+"/filePatterns"
                    print(URL)
                    response=session.post(URL,json=requestJson)
                    print(response.text)
        filePatternID=response.json()['result']
        return filePatternID
    except Exception as e:
        print("Some Exception has been found:",e)








