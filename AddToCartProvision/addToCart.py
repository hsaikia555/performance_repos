import requests
import json
import AddToCartProvision.config as cof
import time
import csv
import AddToCartProvision.LogInToZDP


def addToCart():
        with open('addToCartJson.csv') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if row[0] == "addToCartJson":
                    request=row[1]
                    print(request)
                    requestJson=json.loads(request)
                    for x in range(4, 5):
                        print(x)
                        requestJson['entityTypeId'] = x
                        requestJson['outputDataset'] = 'Add_To_card'+time.strftime('%Y%m%d%H%M%S')+str(x)
                        print("Modified Json-----")
                        print(requestJson)
                        URL=cof.PROTOCOL+"://"+cof.HOST+":"+cof.PORT+"/bedrock-app/services/rest/provision/cart/item/user"
                        print(URL)
                        response=session.post(URL,json=requestJson)
                        print(response.text)
                        print("Add To Card done")
                        #entityTypeId=response.json()["result"]["entityTypeId"]
                        #version=response.json()["result"]["version"]
                        #entityName=response.json()["result"]["technicalName"]
        return

session=AddToCartProvision.LogInToZDP.logIn()
addToCart()