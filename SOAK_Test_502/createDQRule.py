import json
import time
import csv
import SOAK_Test_502.config as cof
import SOAK_Test_502.logger


logger=SOAK_Test_502.logger.logger()
def createDQRule(session):
    try:
        logger.debug("Opening the Input CSV File for CreteDQRule")
        with open('json_input_file.csv') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if row[0] == "createDQRuleJson":
                    request=row[1]
                    print(request)
                    logger.debug("request:"+str(request))
                    requestJson=json.loads(request)
                    ruleName='DQ_Not_Null_'+time.strftime('%Y%m%d%H%M%S')
                    requestJson['ruleName']=ruleName
                    print(requestJson)
                    logger.debug("Request Json:",requestJson)
                    URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/dq/rules/add"
                    logger.debug("URL:"+str(URL))
                    responseJson=session.post(URL,json=requestJson)
                    print("Hello")
                    print(responseJson.text)
                    logger.debug("Response message:",requestJson)
                    ruleId=responseJson.json()['status']['result']
                    logger.debug("Rule ID :"+str(ruleId))
                    break
                else:
                    print("Item not found")
                    logger.debug("Item not found")



        return ruleId,ruleName
    except Exception as e:
        print("Some Exception has been found:"+str(e))
        logger.error("Exception:"+str(e))

