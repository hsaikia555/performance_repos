
# Author: Himanshu Saikia
# Dated: 15/03/2019
# create_utf_workflow will create multiple UTF workflows base on the requirements

import json
import test_repo.performance_framework.core.Application.Workflow.workflow as cof
import test_repo.performance_framework.configs.global_config as global_config
import csv


def execute_workflow(session, execution_frequency, wf_name, wf_id):
    try:
        with open('../engine/execute_workflow/execute_workflow_json.csv') as csv_file:
            csv_reader=csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == "execute_workflow":
                    request = row[1]
                    print(request)
                    for x in range(execution_frequency):
                        print(x)
                        request_json = json.loads(request)
                        request_json['wfName'] = wf_name
                        print(request_json)
                        instance_id = cof.execute_workflow(global_config.PROTOCOL, global_config.HOST, global_config.PORT, wf_id, global_config.PROJECT_ID, request_json, session)
                        print("Workflow with name  ", wf_name+" executed with instance id : ", instance_id)
    except Exception as e:
        print("Exception:", e)
















