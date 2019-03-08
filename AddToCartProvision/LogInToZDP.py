import requests
import json
import AddToCartProvision.config as cof
import time


def logIn():
    try:

        session=requests.session()
        URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/login"
        print(URL)
        requestJson={"username": cof.USERNAME,"password": cof.PASSWORD}
        print(requestJson)
        response=session.post(URL,json=requestJson)
        print(response.text)
        print(response.headers['JSESSIONID'])
        if int(response.status_code) == 200:
            print("login successful")
        else:
            print("unsucessful long")
            exit()
        return session
    except Exception as e:
        print("Some Exception has been found:",e)



