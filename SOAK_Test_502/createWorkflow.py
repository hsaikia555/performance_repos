import requests
import json
import SOAK_Test_502.config as cof
import time


def createWorkflow(session,entityTypeId,version,entityName):



    URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/projects/"+cof.project+"/workflows"
    requestJson={
	"wfId": 0,
	"categoryId": 1,
	"wfLevelParameterList": [],
	"wfNamespaceList": [],
	"stepList": [{
		"actionId": "1",
		"stepName": "Start",
		"stepId": 0,
		"shapeCoordinates": "249,130",
		"pairConnectionId": 0,
		"pairConnectionName": "",
		"stepParamList": [],
		"stepConnectionList": [{
			"nextStepName": "WM"
		}],
		"subWorkflowId": 0
	}, {
		"actionId": "5",
		"stepName": "Stop",
		"stepId": 0,
		"shapeCoordinates": "509,135",
		"pairConnectionId": 0,
		"pairConnectionName": "",
		"stepParamList": [],
		"stepConnectionList": [],
		"subWorkflowId": 0
	}, {
		"actionId": "14",
		"stepName": "WM",
		"stepId": 0,
		"shapeCoordinates": "370,157",
		"pairConnectionId": 0,
		"pairConnectionName": "",
		"stepParamList": [{
			"valueText": False,
			"key": "proceedOnFailure"
		}, {
			"key": "description"
		}, {
			"valueText": "",
			"key": "extraJobConfig"
		}, {
			"key": "numReduceTaskWatermark"
		}, {
			"valueText": cof.WF_BASE_PATH+"WM_Output_Path_"+time.strftime('%Y%m%d%H%M%S'),
			"key": "dfsOutputPath"
		}, {
			"key": "fieldDelim"
		}, {
			"valueText": "$TODAY",
			"key": "effectiveDate"
		}, {
			"valueText": "1",
			"key": "dataFormatWatermark"
		}, {
			"valueText": entityName+"("+str(entityTypeId)+"."+str(version)+")",
			"key": "entityTypeAndVersion"
		}, {
			"valueText": cof.WF_BASE_PATH+"WM_Input_Path_"+time.strftime('%Y%m%d%H%M%S'),
			"key": "dfsInputPath"
		}],
		"stepConnectionList": [{
			"nextStepName": "Stop"
		}],
		"subWorkflowId": 0
	}],
	"notificationDetails": [],
	"logLevel": "DEBUG",
	"globalParameter": ",,,,,,,,",
	"description": "",
	"overwritable": False,
	"wfName": "Test_WF"+"_"+time.strftime('%Y%m%d%H%M%S')
}
    response=session.post(URL,json=requestJson)
    print(response.text)
    wfId=response.json()['result']['wfId']
    return wfId




