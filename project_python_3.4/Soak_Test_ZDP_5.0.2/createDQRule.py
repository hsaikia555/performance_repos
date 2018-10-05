import json
import time
import csv
import SOAK_Test_502.config as cof



def createDQRule(session):
    try:
        with open('json_input_file.csv') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if row[0] == "createDQRuleJson":
                    request=row[1]
                    print(request)
                    requestJson=json.loads(request)
                    ruleName='DQ_Not_Null_'+time.strftime('%Y%m%d%H%M%S')
                    requestJson['ruleName']=ruleName
                    print(requestJson)
                    URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/dq/rules/add"
                    responseJson=session.post(URL,json=requestJson)
                    print("Hello")
                    print(responseJson.text)
                    ruleId=responseJson.json()['status']['result']
                    break
                else:
                    print("Item not found")



        return ruleId,ruleName
    except Exception as e:
        print("Some Exception has been found:",e)

