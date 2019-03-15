# Author: Himanshu Saikia
# Dated: 15/03/2019
# create_delimited_entity will create delimited entities with pre defined 10 fields

import json
import time
import csv
import test_repo.performance_framework.core.Application.Entity.entity as cof
import test_repo.performance_framework.configs.global_config as global_conf
import test_repo.performance_framework.core.utils.random_value_generator as random_gen

def create_delimited_entity(session, no_of_entities):
    try:
        with open('../engine/create_entity/create_entity_json.csv') as csv_file:
            csv_reader=csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == "create_delimited_entity":
                    request = row[1]
                    print(request)
                    request_json = json.loads(request)
                    for x in range(no_of_entities):
                        print(x)
                        request_json['businessName'] = 'Auto_delimited_10_fields'+str(random_gen.random_value(8))+str(random_gen.random_value(8))
                        request_json['technicalName'] = 'Auto_delimited_10_fields'+str(random_gen.random_value(8))+str(random_gen.random_value(8))
                        request_json['sourcePlatform'] = 'Auto_delimited_10_fields'+str(random_gen.random_value(8))+str(random_gen.random_value(8))
                        request_json['sourceSchema'] = 'Auto_delimited_10_fields'+str(random_gen.random_value(8))+str(random_gen.random_value(8))
                        request_json['tableName'] = 'Auto_delimited_10_fields'+str(random_gen.random_value(8))+str(random_gen.random_value(8))
                        request_json['targetSchema'] = global_conf.TARGET_SCHEMA
                        print(request_json)
                        entity_type_id, version, entity_name = cof.create_entity(global_conf.PROTOCOL, global_conf.HOST, global_conf.PORT, session, request_json, global_conf.PROJECT_ID)
                        print("Entity ID: ",entity_type_id, "With Version: ", version, "Entity Name: ", entity_name)
    except Exception as e:
        print("Exception :", e)

