import json
import SOAK_Test_502.config as cof
import time

def createFilePattern(session,lzDirId,wfId,connection_id):
    URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/projects/"+cof.project+"/filePatterns"
    print(URL)
    requestJson={
	"patternPrefix": "post_[0-9]+",
	"otherFiles": "",
	"patternSuffix": ".txt",
	"description": "",
	"destination": cof.WF_BASE_PATH+"Ingestion_destination_"+time.strftime('%Y%m%d%H%M%S'),
	"retryAttempts": 0,
	"triggerFileSuffix": ".done",
	"deleteAfterIngestion": True,
	"globalParameter": ",,,,,,,,",
	"lzDirectories": [{
		"lzDirId": lzDirId
	}],
	"filePatternAttributes": [],
	"frequency": "",
	"wfLevelParamList": "",
	"wfNamespaceList": [],
	"delimiter": None,
	"destinationFileSystemUri": "",
	"destinationFileSystemProperties": {
		"": ""
	},
	"entityId": None,
	"entityVersion": None,
	"partitionEntityId": None,
	"partitionEntityVersion": None,
	"workflowId": wfId,
	"controlFileSuffix": "",
	"metaFileSuffix": "",
	"checksumFileSuffix": "",
	"dataFileFormatId": 0,
	"byPassIngestion": False,
	"scriptTimeout": 0,
	"preIngestionScriptArgs": "${INPUT_FILE} ${ADDITIONAL_FILES} ${FILE_PATTERN_ID} ${ENTITY_ID} ${ENTITY_VERSION} ${LZ_DIRECTORY} ${PARTITION_ENTITY_ID} ${PARTITION_ENTITY_VERSION}",
	"adminCapacityQueues": None,
	"flAgents": [],
	"batchedIngestionFlag": False,
	"ingestionBatchSize": 0,
	"ingestionBatchWindow": 0,
	"fileSystemConnectionInstanceId": connection_id,
	"ingestAs": ""
}
    response=session.post(URL,json=requestJson)
    print(response.text)
    filePatternID=response.json()['result']
    return filePatternID








