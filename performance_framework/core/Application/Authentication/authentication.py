# Author: Himanshu Saikia
# Dated : 15/03/2019
# This module is used to login and logout to ZDP

import requests
import test_repo.performance_framework.configs.global_config as cof


def log_in():
    try:

        session=requests.session()
        url = cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/login"
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




