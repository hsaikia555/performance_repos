# Author: Himanshu Saikia
# Dated : 15/03/2019
# This module is used to login and logout to ZDP

import requests
import test_repo.performance_framework.configs.global_config as cof
import test_repo.performance_framework.core.Application.ZDP_API_LIST.ZDP_API as API


def log_in():
    try:
        log_into_zdp_base_url = str(API.log_into_zdp)
        print(log_into_zdp_base_url)
        session=requests.session()
        url = cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+log_into_zdp_base_url
#        url = cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/login"
        print(url)
        request_json={"username": cof.USER_NAME,"password": cof.PASSWORD}
        print("Login to ZDP........")
        response=session.post(url, json=request_json)
        print(response.text)
#        print(response.headers['JSESSIONID'])
        if int(response.status_code) == 200:
            print("Login successful")
        else:
            print("Login failure")
            exit()
        return session
    except Exception as e:
        print("Exception :",e)




