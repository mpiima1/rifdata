#!/usr/bin/env /home/mpiima/rifdata/readings/bin/python
import os
import json
import csv
if not os.path.isfile('data.csv'):
    print('no')
    with open("data.csv","a") as csvfile:
        cwriter = csv.writer(csvfile)
        cwriter.writerow(["Application ID","Device ID","Sample Number","Temperature","Humidity","Time"])
def writeCsv(dataString):
    resultDict = json.loads(dataString)
    with open("data.csv","a") as csvfile:
        cwriter = csv.writer(csvfile)
        cwriter.writerow([resultDict["app_id"],resultDict["dev_id"],resultDict["counter"],resultDict["payload_fields"]["temperature_1"],resultDict["payload_fields"]["relative_humidity_3"],resultDict["metadata"]["time"]])
