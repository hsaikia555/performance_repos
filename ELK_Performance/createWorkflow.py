import requests
import json
import ELK_Performance.config as cof
import time
import csv


def createWorkflow(session,entityTypeId,version,entityName,connection_id):
    try:
        timestamp=time.strftime('%Y%m%d%H%M%S')
        with open('json_input_file.csv') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if row[0] == "createWorkflowJson":
                    request=row[1]
                    print(request)
                    requestJson=json.loads(request)
                    requestJson['wfName']='WF_SOAK_Automation'+timestamp
                    stepList_list=requestJson['stepList']
                    print(stepList_list)
                    for i in range(len(stepList_list)):
                        if stepList_list[i]['stepName']=='FDQ':
                            stepParamList_list=stepList_list[i]['stepParamList']
                            print(stepParamList_list)
                            for j in range(len(stepParamList_list)):
                                if stepParamList_list[j]['key'] == 'validDataPath':
                                    stepParamList_list[j]['valueText'] = cof.WF_BASE_PATH+'SOAK_Test_FDQ_Good_data_Path_automation_'+timestamp
                                if stepParamList_list[j]['key']=='badDataOPLocation':
                                    stepParamList_list[j]['valueText'] = cof.WF_BASE_PATH+'SOAK_Test_FDQ_Bad_data_Path_automation_'+timestamp
                                if stepParamList_list[j]['key']=='entityTypeAndVersion':
                                    stepParamList_list[j]['valueText'] = entityName+'('+str(entityTypeId)+'.'+str(version)+')'
                        if stepList_list[i]['stepName']=='TM':
                            stepParamList_list=stepList_list[i]['stepParamList']
                            print(stepParamList_list)
                            for j in range(len(stepParamList_list)):
                                if stepParamList_list[j]['key']=='storeOutputDirectory':
                                    stepParamList_list[j]['valueText'] = cof.WF_BASE_PATH+'SOAK_Test_TM_Store_data_Path_automation_'+timestamp
                                if stepParamList_list[j]['key']=='secureOutputDirectory':
                                    stepParamList_list[j]['valueText'] = cof.WF_BASE_PATH+'SOAK_Test_TM_Secure_data_Path_automation_'+timestamp
                                if stepParamList_list[j]['key']=='entityTypeIdAndVersion':
                                    stepParamList_list[j]['valueText'] = entityName+'('+str(entityTypeId)+'.'+str(version)+')'

                        if stepList_list[i]['stepName']=='UTF':
                            stepParamList_list=stepList_list[i]['stepParamList']
                            print(stepParamList_list)
                            for j in range(len(stepParamList_list)):
                                if stepParamList_list[j]['key']=='destinationPath':
                                    stepParamList_list[j]['valueText'] = cof.WF_BASE_PATH+'SOAK_UTF_data_Path_automation_'+timestamp
                                if stepParamList_list[j]['key']=='extraJobConfig':
                                    stepParamList_list[j]['valueText'] = 'hdp.version:'+cof.hdp_version_for_UTF

                        if stepList_list[i]['stepName']=='File Move':
                            stepParamList_list=stepList_list[i]['stepParamList']
                            print(stepParamList_list)
                            for j in range(len(stepParamList_list)):
                                if stepParamList_list[j]['key']=='srcDesPairs':
                                    stepParamList_list[j]['valueText'] = cof.WF_BASE_PATH+'SOAK_UTF_data_Path_automation_'+timestamp+'/${WORKFLOW.INSTANCE_ID}/'+';HDFS;'+cof.WF_BASE_PATH+'SOAK_File_Move_data_Path_automation_'+timestamp+';HDFS;false;'+str(connection_id)+';'+str(connection_id)

                        if stepList_list[i]['stepName']=='cleaning script':
                            stepParamList_list=stepList_list[i]['stepParamList']
                            print(stepParamList_list)
                            for j in range(len(stepParamList_list)):
                                if stepParamList_list[j]['key']=='scriptContent':
                                    stepParamList_list[j]['valueText'] = 'hadoop fs -rm -r ${WORKFLOW.HDFS_INPUT_PATH}\nhadoop fs -rm -r '+cof.WF_BASE_PATH+'SOAK_Test_FDQ_Good_data_Path_automation_'+timestamp+'/instanceid=${WORKFLOW.INSTANCE_ID}\nhadoop fs -rm -r '+cof.WF_BASE_PATH+'SOAK_Test_TM_Store_data_Path_automation_'+timestamp+'/instanceid=${WORKFLOW.INSTANCE_ID}\nhadoop fs -rm -r '+cof.WF_BASE_PATH+'SOAK_Test_TM_Secure_data_Path_automation_'+timestamp+'/instanceid=${WORKFLOW.INSTANCE_ID}\nhadoop fs -rm -r '+cof.WF_BASE_PATH+'SOAK_File_Move_data_Path_automation_'+timestamp+'/${WORKFLOW.INSTANCE_ID}'
                    print(requestJson)

                    URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/projects/"+cof.project+"/workflows"
                    response=session.post(URL,json=requestJson)
                    print(response.text)
                    wfId=response.json()['result']['wfId']
        return wfId
    except Exception as e:
        print("Some Exception has been found:",e)


