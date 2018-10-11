import requests
import logInToZDP
import config


def executeWorkflow(session,workflowId,workflowName):
    URL=config.PROTOCOL+'://'+config.HOST+':'+config.PORT+'/bedrock-app/services/rest/workflows/'+workflowId+'/execute?projectIds='+config.project
    print(URL)
    requestJson={
  "wfName": workflowName,
  "globalParameter": "",
  "executedBy": "zaloni",
  "wfLevelParameterList": [],
  "wfNamespaceList": [],
  "clusterId": ""
}

    responseJson=session.post(URL,json=requestJson)
    #print(responseJson.text)
    instnceId=responseJson.json()['result']
    return instnceId

session=logInToZDP.logIn()
for i in range(1,5000):
    instnceId=executeWorkflow(session,'7','Test_Shell_1')
    print("For workflow Test_Shell_1 increment....",i,instnceId)
    instnceId=executeWorkflow(session,'8','Test_Shell_2')
    print("For workflow Test_Shell_2 increment....",i,instnceId)

