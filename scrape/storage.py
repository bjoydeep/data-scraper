import pandas
from prometheus_api_client import *



def scrape(pc,stime,etime,step):
    print("Gathering data About Storage Usage....")
    nodeDiskUtil(pc,stime,etime,step)
    nodeDFileSystem(pc,stime,etime,step)

def nodeDiskUtil(pc,stime,etime,step):    

    print("")
    print("Node Disk Util Data..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='sum by(instance) (1-(max without (mountpoint, fstype) (node_filesystem_avail_bytes{job="node-exporter", fstype!=""})/max without (mountpoint, fstype) (node_filesystem_size_bytes{job="node-exporter", fstype!=""})))',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    #print(etcd_db_size_df.head())
    etcd_db_sizep_df = etcd_db_size_df.pivot( columns='instance' ,values='value')
    print(etcd_db_sizep_df.head())

def nodeDFileSystem(pc,stime,etime,step):    

    print("")
    print("Node File System Max Data..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='sum by (instance)(max without (mountpoint, fstype) (node_filesystem_size_bytes{}) - max without (mountpoint, fstype) (node_filesystem_avail_bytes{}))',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    #print(etcd_db_size_df.head())
    etcd_db_sizep_df = etcd_db_size_df.pivot( columns='instance' ,values='value')
    print(etcd_db_sizep_df.head())

