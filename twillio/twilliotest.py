from __future__ import print_function
from flask import Flask, jsonify, request
import os
import pickle
import os.path
import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import ast
from pprint import pprint
import json
from jinja2 import Environment, FileSystemLoader
import base64
import re
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import time, datetime
import requests
import csv
import pandas as pd
import numpy as np
import math

class wa_twillio():
    def __init__(self, json , values):
        self.json = json
        self.values = values
        self.account_sid = ""
        self.auth_token = ""
        self.inbound_url = ""
        self.deliveryAndEngagement_url = ""
        self.posttestingurl = ""
    
    
    
    def InComing(self):
        time1= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Body = self.values('Body', None)
        From = self.values('From', None)
        To = self.values('To', None)
        SmsStatus = self.values('SmsStatus', None)
        MessageSid = self.values('MessageSid', None)
        MediaUrl0 = self.values('MediaUrl0', None)
        number_from = From.split(":")
        number_to = To.split(":")
        #client = Client(self.account_sid, self.auth_token)
        #body1='welcome '+number_from[1]+', this is the ISM whatsapp microservice'
        # message = client.messages.create(
        #                             from_=self.values('To', None) ,
        #                             body=body1,
        #                             to=self.values('From', None)
        #                         )
        # try:
        
        #     # message = client.messages.create(
        #     #                     from_=self.values('To', None),
        #     #                     body=MediaUrl0,
        #     #                     to=self.values('From', None)
        #     #                 )
        #     body2=MediaUrl0
        # except:
        #     MediaUrl0="0"
        #     # message = client.messages.create(
        #     #                     from_=self.values('To', None),
        #     #                     body='Processing Your Request',
        #     #                     to=self.values('From', None)
        #     #                 )
        #     body2='Processing Your Request'
        
        data1 = {
        "Incoming" : {
            "MessageSid":MessageSid,
            "From":number_from[1],
            "To":number_to[1],
            "Body":Body,
            "media_url":MediaUrl0,
            "Timestamp":str(time1),
            "SmsStatus":SmsStatus
        },
        "OutGoing" : {
            "MessageSid":"message.sid",
            "From":number_to[1],
            "To":number_from[1],
            "Body":"body1++body2",
            "media_url":MediaUrl0,
            "Timestamp":str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        }
        }
        data = data1["Incoming"]
        try:
            df1 = pd.read_csv("Residue_Inbound.csv")
        except:
            try:
                df1 = pd.DataFrame({"MessageSid":[],
                                   "From":[],
                                   "To":[],
                                   "Body":[],
                                   "media_url":[],
                                   "Timestamp":[],
                                   "SmsStatus":[]
                                   })
            except:
                df1 = pd.DataFrame(columns=["MessageSid","From","To","Body","media_url","Timestamp","SmsStatus"])
            df1 = df1.fillna(0)
            print("###### printing the data frame ######")
            print(df1)
            df2 = pd.DataFrame({"MessageSid":[str(data["MessageSid"])],
                               "From":[number_from[1]],
                               "To":[number_to[1]],
                               "Body":[str(data["Body"])],
                               "media_url":[str(data["media_url"])],
                               "Timestamp":[str(data["Timestamp"])],
                               "SmsStatus":[str(data["SmsStatus"])]
                               })
            df3 = df1.append(df2,ignore_index=True)
                               df3 = df3.fillna(0)
                               print(df3)
            df3.to_csv('Residue_Inbound.csv',index=False)
            residues = []
            for i in range(len(df3)) :
            print(df3.loc[i, "MessageSid"], df3.loc[i, "Body"],df3.loc[i, "From"],df3.loc[i, "To"])
            res = {
                "MessageSid":df3.loc[i, "MessageSid"],
                "From":("+"+str(df3.loc[i, "From"])),
                "To":("+"+str(df3.loc[i, "To"])),
                "Body":df3.loc[i, "Body"],
                "media_url":df3.loc[i, "media_url"],
                "Timestamp":df3.loc[i, "Timestamp"],
                "SmsStatus":df3.loc[i, "SmsStatus"]
            }
                residues.append(res)

            residues_dict = { "data":residues }
            print(residues_dict)
            try:
            headers = {'content-type': 'application/json'}
            API_ENDPOINT = self.inbound_url
            resp = requests.post(url = API_ENDPOINT,json = residues_dict)
            print(resp)
            # API_ENDPOINT_test = self.posttestingurl
            # resp = requests.post(url = API_ENDPOINT_test,json = residues_dict,headers=headers)
            # print(resp)
                print('"Status":"Sent to ISM table"')
            except:
                    print("ism strem failed")
                        
                        return jsonify({"Status":"Sent to ISM table"})

def OutGoing(self):
    print("##################")
    print("##################")
    print("##################")
    print("##################")
    print("##################")
    print("##################")
    print(self.json)
    print("##################")
    print("##################")
    print("##################")
    print("##################")
    print("##################")
    print("##################")
    From=self.json["From"]
    To=self.json["To"]
    BODY=self.json["Body"]
    MEDIA_URL=self.json["media_url"]
    number_from = From.split(":")
    number_to = To.split(":")
    
    client = Client(self.account_sid, self.auth_token)
        try:
            message = client.messages.create(
                                             from_=self.json["From"],
                                             body=BODY,
                                             to=self.json["To"],
                                             media_url=MEDIA_URL,
                                             )
                                             data = {
                                                 "MessageSID":message.sid,
                                                     "From":number_from[1],
                                                     "To":number_to[1],
                                                     "Body":BODY,
                                                         "media_url":MEDIA_URL,
                                                             "DeliveryStatus":"Sent",
                                                                 "Timestamp":str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        }
        except ClientError as e:
            print("##################")
            print("##################")
            print("##################")
            print("##################")
            print("##################")
            print("##################")
            print(e)
            data = {
                "MessageSID":"",
                "From":number_from[1],
                "To":number_to[1],
                "Body":BODY,
                "media_url":MEDIA_URL,
                "DeliveryStatus":"Unsuccessful",
                "Timestamp":str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        }

        print(data)
                    return jsonify(data)

def TrackingResponse(self):
    EventType = self.values('EventType', None)
    ###############
    MessageSid = self.values('MessageSid', None)
        ###############
        SmsStatus = self.values('SmsStatus', None)
        ###############
        To = self.values('To', None)
        ###############
        From = self.values('From', None)
        number_from = From.split(":")
        number_to = To.split(":")
        
        client = Client(self.account_sid, self.auth_token)
        if SmsStatus == 'delivered' or EventType == 'DELIVERED':
            print("delivered")
            data = {
                "MessageSid":MessageSid,
                "From":number_from[1],
                "To":number_to[1],
                "SmsStatus":SmsStatus,
                "EventType":EventType,
                "Timestamp":str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                "DeliveryStatus":"delivered",
                "ReadStatus":"Unread"}
    elif SmsStatus == 'read' or EventType == 'READ':
        print("read")
        data = {
            "MessageSid":MessageSid,
                "From":number_from[1],
                "To":number_to[1],
                "SmsStatus":SmsStatus,
                "EventType":EventType,
                "Timestamp":str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                "DeliveryStatus":"delivered",
                "ReadStatus":"read"}
        elif SmsStatus == "sent":
            # data = {
            #     "MessageSid":MessageSid,
            #     "From":number_from[1],
            #     "To":number_to[1],
            #     "SmsStatus":SmsStatus,
            #     "EventType":EventType,
            #     "Timestamp":str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            #     "DeliveryStatus":"Sent",
            #     "ReadStatus":"Unread"}
            return jsonify({"Status":"Sent "})
    else :
        print("else")
        data = {
        }
        try:
            df1 = pd.read_csv("Residue_DeliveryandEngagement.csv")
except:
    try:
        df1 = pd.DataFrame({'MessageSid':[],
                           'From':[],
                           'To':[],
                           'SmsStatus':[],
                           'EventType':[],
                           'Timestamp':[],
                           'DeliveryStatus':[],
                           'ReadStatus':[]
                           })
            except:
                df1 = pd.DataFrame(columns=["MessageSid","From","To","SmsStatus","EventType","Timestamp","DeliveryStatus","ReadStatus"])
    df1 = df1.fillna(0)
        print("#########################################")
        #print(df1)
        #print(number_to)
        #print(number_from)
        df2 = pd.DataFrame({'MessageSid':[str(data["MessageSid"])],
                           'From':[number_from[1]],
                           'To':[number_to[1]],
                           'SmsStatus':[str(data["SmsStatus"])],
                           'EventType':[str(data["EventType"])],
                           'Timestamp':[str(data["Timestamp"])],
                           'DeliveryStatus':[str(data["DeliveryStatus"])],
                           'ReadStatus':[str(data["ReadStatus"])]
                           })
                           df3 = df1.append(df2,ignore_index=True)
                           df3 = df3.fillna(0)
                           #print(df3)
                           df3.to_csv('Residue_DeliveryandEngagement.csv',index=False)
                           
                           residues = []
                           for i in range(len(df3)) :
                               print(df3.loc[i, "MessageSid"], df3.loc[i, "From"],df3.loc[i, "To"])
                               print("+"+str(df3.loc[i, "From"]))
                               print("+"+str(df3.loc[i, "To"]))
                               res = {
                                   "MessageSid":df3.loc[i, "MessageSid"],
                                   "From":("+"+str(df3.loc[i, "From"])),
                                   "To":("+"+str(df3.loc[i, "To"])),
                                   "SmsStatus":df3.loc[i, "SmsStatus"],
                                   "EventType":df3.loc[i, "EventType"],
                                   "Timestamp":df3.loc[i, "Timestamp"],
                                   "ReadStatus":df3.loc[i, "ReadStatus"],
                                   "DeliveryStatus":df3.loc[i, "DeliveryStatus"]
                                       }
                                           residues.append(res)

residues_dict = { "data":residues }
    print(residues_dict)
    try:
        headers = {'content-type': 'application/json'}
            API_ENDPOINT = self.deliveryAndEngagement_url
            resp = requests.post(url = API_ENDPOINT,json = residues_dict,headers=headers)
            print(resp)
            # API_ENDPOINT_test = self.posttestingurl
            # resp = requests.post(url = API_ENDPOINT_test,json = residues_dict,headers=headers)
            # print(resp)
            print("Data for "+str(data["MessageSid"])+" and status "+str(data["DeliveryStatus"])+" : "+str(data["ReadStatus"]))
            print('"Status":"Sent to ISM table"')
        except:
            print("ISM data stream failed")

    return jsonify({"Status":"Sent to ISM table"})

def cleanResidueDNE(self):
    print("##################")
    print("##################")
    print("##################")
    print("##################")
    print("##################")
    print("##################")
    print(self.json)
    Delivery=self.json["Delivery"]
    Engagement=self.json["Engagement"]
    MessageSid=self.json["MessageSid"]
    
    try:
        df1 = pd.read_csv("Residue_DeliveryandEngagement.csv")
        except:
            try:
                df1 = pd.DataFrame({'MessageSid':[],
                                   'From':[],
                                   'To':[],
                                   'SmsStatus':[],
                                   'EventType':[],
                                   'Timestamp':[],
                                   'DeliveryStatus':[],
                                   'ReadStatus':[]
                                   })
            except:
                df1 = pd.DataFrame(columns=["MessageSid","From","To","SmsStatus","EventType","Timestamp","DeliveryStatus","ReadStatus"])
    
    print(df1)
        df1 = df1.fillna(0)
        all_columns = list(df1) # Creates list of all column headers
        df1[all_columns] = df1[all_columns].astype(str)
        print("after removing nans")
        print(df1.dtypes)
        print(df1)
        index1 = df1[ (df1['MessageSid'] == MessageSid) & (df1['DeliveryStatus'] == Delivery) & (df1['ReadStatus'] == Engagement)].index
        print("###################")
        print(index1)
        df1.drop(index1, inplace=True)
        print(df1)
        df1.to_csv('Residue_DeliveryandEngagement.csv',index=False)
        return jsonify({"Status":"Removed from Residue table"})

def cleanResidueInbound(self):
    ###############
    print("##################")
    print("##################")
    print("##################")
    print("##################")
    print("##################")
    print("##################")
    print(self.json)
    MessageSid=self.json["MessageSid"]
    To=self.json["To"]
    From=self.json["From"]
    try:
        df1 = pd.read_csv("Residue_Inbound.csv")
        except:
            try:
                df1 = pd.DataFrame({"MessageSid":[],
                                   "From":[],
                                   "To":[],
                                   "Body":[],
                                   "media_url":[],
                                   "Timestamp":[],
                                   "SmsStatus":[]
                                   })
            except:
                df1 = pd.DataFrame(columns=["MessageSid","From","To","Body","media_url","Timestamp","SmsStatus"])
    print(df1)
        df1 = df1.fillna(0)
        all_columns = list(df1) # Creates list of all column headers
        df1[all_columns] = df1[all_columns].astype(str)
        print("after removing nans")
        print(df1.dtypes)
        df1["To"]="+"+df1["To"]
        df1["From"]="+"+df1["From"]
        print(df1)
        # print(To)
        # print(type(To))
        index1 = df1[ (df1['MessageSid']== MessageSid) & (df1["To"] == To) & (df1["From"] == From)].index
        #print(indexNames)
        df1.drop(index1, inplace=True)
        print(df1)
        df1.to_csv('Residue_Inbound.csv',index=False)
        return jsonify({"Status":"Removed from Residue table"})


def testingpost (self):
    #contacts=request.json["Contact"]
    print("functioned called for testing the request Json values to be sent to ISM endpoint ")
    print("################## Request . json ")
    print(request.json)
    
        return ("Printed the request Json values recived ")


