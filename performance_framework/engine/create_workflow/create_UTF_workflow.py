# Author: Himanshu Saikia
# Dated: 15/03/2019
# create_utf_workflow will create multiple UTF workflows base on the requirements

import json
import test_repo.performance_framework.core.Application.Workflow.workflow as cof
import test_repo.performance_framework.configs.global_config as global_config
import time
import csv
import test_repo.performance_framework.core.utils.random_value_generator as random_gen

def create_utf_workflow(session, no_of_utf_workflow, utf_input_path, wf_base_path):
    try:
        with open('../engine/create_workflow/create_workflow_json.csv') as csv_file:
            csv_reader=csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == "create_utf_workflow":
                    request = row[1]
                    print(request)
                    for x in range(no_of_utf_workflow):
                        print(x)
                        request_json = json.loads(request)
                        request_json['wfName'] = 'Auto_UTF_WF'+str(random_gen.random_value(8))+str(random_gen.random_value(8))
                        step_list = request_json['stepList']
                        print(step_list)
                        for i in range(len(step_list)):
                            if step_list[i]['stepName'] == 'UTF':
                                step_param_list = step_list[i]['stepParamList']
                                print(step_param_list)
                                for j in range(len(step_param_list)):
                                    if step_param_list[j]['key'] == 'sourcePath':
                                        step_param_list[j]['valueText'] = utf_input_path
                                    if step_param_list[j]['key'] == 'destinationPath':
                                        step_param_list[j]['valueText'] = wf_base_path+"Automation_UTF_destination_path"+str(random_gen.random_value(8))+str(random_gen.random_value(8))
                        print(request_json)
                        wf_id, wf_name = cof.create_workflow(session, global_config.HOST, global_config.PORT, request_json, global_config.PROTOCOL, global_config.PROJECT_ID)
                        print("Workflow with name ", wf_name+" created with ID: ", wf_id)
#        return wf_id, wf_name
    except Exception as e:
        print("Exception:", e)





