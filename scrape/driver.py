import json
import os
from prometheus_api_client import *
import datetime
import kubeAPIServer
import etcdStatus
import generalHealth
import containerMemory
import containerCPU
import networkStat
import storage
import iops
import acmStats
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    """Main Driver Program."""
    print("This module launches the data gathering process from Prometheus or Thanos")
    loadEnv()

def loadEnv():
    print("Loading env data.....")
    with open(os.path.join(os.path.dirname(__file__), '..', 'pwd.env')) as f:
        data = f.read()
    cred = json.loads(data)
    purl = cred.get('promurl')
    tok = cred.get('token')
    start_offset_minute = cred.get('startOffsetMinute')
    end_offset_minute = cred.get('endOffsetMinute')   
    steps_minute = cred.get('stepsMinute')

    printConfigurations(cred, purl, tok, start_offset_minute,end_offset_minute,steps_minute)
    
    pc = connectProm(purl, tok)
    start_time=(datetime.datetime.now() - datetime.timedelta(minutes=start_offset_minute))
    end_time=datetime.datetime.now()
    step=steps_minute

    startScrape(pc, start_time,end_time,step)

def connectProm(purl,tok):
    pc = PrometheusConnect(url=purl, headers={"Authorization": "Bearer {}".format(tok)}, disable_ssl=True)
    return pc 

def startScrape(pc,stime,etime,step):
    print("Run started")  
    kubeAPIServer.scrape(pc,stime,etime,step)
    etcdStatus.scrape(pc,stime,etime,step) 
    generalHealth.scrape(pc,stime,etime,step) 
    containerMemory.scrape(pc,stime,etime,step)
    containerCPU.scrape(pc,stime,etime,step)
    networkStat.scrape(pc,stime,etime,step)
    iops.scrape(pc,stime,etime,step)
    storage.scrape(pc,stime,etime,step)
    acmStats.scrape(pc,stime,etime,step)
    

def printConfigurations(cred, purl, tok, start_offset_minute,end_offset_minute,steps_minute):
    
    print("Configuration details ------ ")
    print("Prom URL:", purl)
    print("Token:", tok)
    print("Start time offset in Minutes:", start_offset_minute)
    print("End time offset in Minutes:", end_offset_minute)    
    print("Steps in Minutes:", steps_minute)
    print("-------- ------ ")     

if __name__=="__main__":
    main()