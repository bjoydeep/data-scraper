import pandas
from prometheus_api_client import *



def scrape(pc,stime,etime,step):
    print("Gathering data About IOPS Usage....")
    iops(pc,stime,etime,step)
    thruput(pc,stime,etime,step)

def iops(pc,stime,etime,step):    

    print("")
    print("Top 3 IOPS(Reads+Writes)..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='topk(3, ceil(sum by(namespace) (rate(container_fs_reads_total{}[5m]) + rate(container_fs_writes_total{}[5m]))))',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    #print(etcd_db_size_df.head())
    etcd_db_sizep_df = etcd_db_size_df.pivot( columns='namespace' ,values='value')
    print(etcd_db_sizep_df.head())

def thruput(pc,stime,etime,step):    

    print("")
    print("Top 3 ThroughPut(Read+Write)..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='topk(3, sum by(namespace) (rate(container_fs_reads_bytes_total{}[5m]) + rate(container_fs_writes_bytes_total{}[5m])))',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    #print(etcd_db_size_df.head())
    etcd_db_sizep_df = etcd_db_size_df.pivot( columns='namespace' ,values='value')
    print(etcd_db_sizep_df.head())        