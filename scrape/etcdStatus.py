import pandas
from prometheus_api_client import *



def scrape(pc,stime,etime,step):
    print("Gathering data from etcd....")
    etcdDBSize(pc,stime,etime,step)
    etcdDBSizeUse(pc,stime,etime,step)
    etcdDiskSync(pc,stime,etime,step)
    etcdBackendCommit(pc,stime,etime,step)
    etcdLeaderElection(pc,stime,etime,step)
    etcdLeaderChange(pc,stime,etime,step)
    etcdPeerRoundTrip(pc,stime,etime,step)
    
def etcdDBSize(pc,stime,etime,step):    

    print("")
    print("etcd DB Size..")

    etcd_db_size = pc.custom_query_range(
    query='etcd_mvcc_db_total_size_in_bytes',
    start_time=stime,
    end_time=etime,
    step=step,
    )


    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head())
    
    #print("Shape of the data frame: ", etcd_db_size_df.shape)
    #print(etcd_db_size_df.info())
    print("Descriptive stats ofthe data frame", etcd_db_size_df["value"].describe())

def etcdDBSizeUse(pc,stime,etime,step):    

    print("")
    print("etcd DB Size in Use..")

    etcd_db_size_use = pc.custom_query_range(
    query='etcd_mvcc_db_total_size_in_use_in_bytes',
    start_time=stime,
    end_time=etime,
    step=step,
    )


    etcd_db_size_use_df = MetricRangeDataFrame(etcd_db_size_use)
    etcd_db_size_use_df["value"]=etcd_db_size_use_df["value"].astype(float)
    etcd_db_size_use_df.index= pandas.to_datetime(etcd_db_size_use_df.index, unit="s")
    print(etcd_db_size_use_df.head()) 
    print("Descriptive stats ofthe data frame", etcd_db_size_use_df["value"].describe())

def etcdDiskSync(pc,stime,etime,step):    

    print("")
    print("etcd Disk Sync Duration..")

    etcd_disk_sync = pc.custom_query_range(
    query='histogram_quantile(0.99, sum(rate(etcd_disk_wal_fsync_duration_seconds_bucket{job="etcd"}[5m])) by (instance, le))',
    start_time=stime,
    end_time=etime,
    step=step,
    )


    etcd_disk_sync_df = MetricRangeDataFrame(etcd_disk_sync)
    etcd_disk_sync_df["value"]=etcd_disk_sync_df["value"].astype(float)
    etcd_disk_sync_df.index= pandas.to_datetime(etcd_disk_sync_df.index, unit="s")
    etcd_disk_syncp_df = etcd_disk_sync_df.pivot( columns='instance' ,values='value')
    print(etcd_disk_syncp_df.head()) 
    #print("Descriptive stats ofthe data frame", etcd_db_size_usep_df["value"].describe())    

def etcdBackendCommit(pc,stime,etime,step):    

    print("")
    print("etcd Backend Commit Duration..")

    etcd_disk_sync = pc.custom_query_range(
    query='histogram_quantile(0.99, irate(etcd_disk_backend_commit_duration_seconds_bucket[5m]))',
    start_time=stime,
    end_time=etime,
    step=step,
    )


    etcd_disk_sync_df = MetricRangeDataFrame(etcd_disk_sync)
    etcd_disk_sync_df["value"]=etcd_disk_sync_df["value"].astype(float)
    etcd_disk_sync_df.index= pandas.to_datetime(etcd_disk_sync_df.index, unit="s")
    #etcd_disk_syncp_df = etcd_disk_sync_df.pivot( columns='instance' ,values='value')
    print(etcd_disk_sync_df.head()) 
    print("Descriptive stats ofthe data frame", etcd_disk_sync_df["value"].describe()) 

def etcdLeaderElection(pc,stime,etime,step):    

    print("")
    print("etcd Total Leader Elections Per Day..")

    etcd_disk_sync = pc.custom_query_range(
    query='changes(etcd_server_leader_changes_seen_total{job="etcd"}[1d])',
    start_time=stime,
    end_time=etime,
    step=step,
    )


    etcd_disk_sync_df = MetricRangeDataFrame(etcd_disk_sync)
    etcd_disk_sync_df["value"]=etcd_disk_sync_df["value"].astype(float)
    etcd_disk_sync_df.index= pandas.to_datetime(etcd_disk_sync_df.index, unit="s")
    #etcd_disk_syncp_df = etcd_disk_sync_df.pivot( columns='instance' ,values='value')
    print(etcd_disk_sync_df.head()) 
    print("Descriptive stats ofthe data frame", etcd_disk_sync_df["value"].describe())

def etcdLeaderChange(pc,stime,etime,step):    

    print("")
    print("etcd Max Leader changes..")

    etcd_disk_sync = pc.custom_query_range(
    query='max(etcd_server_leader_changes_seen_total)',
    start_time=stime,
    end_time=etime,
    step=step,
    )


    etcd_disk_sync_df = MetricRangeDataFrame(etcd_disk_sync)
    etcd_disk_sync_df["value"]=etcd_disk_sync_df["value"].astype(float)
    etcd_disk_sync_df.index= pandas.to_datetime(etcd_disk_sync_df.index, unit="s")
    #etcd_disk_syncp_df = etcd_disk_sync_df.pivot( columns='instance' ,values='value')
    print(etcd_disk_sync_df.head()) 
    print("Descriptive stats ofthe data frame", etcd_disk_sync_df["value"].describe())

def etcdPeerRoundTrip(pc,stime,etime,step):    

    print("")
    print("etcd ETCD Peer Roundtrip Time..")

    etcd_disk_sync = pc.custom_query_range(
    query='histogram_quantile(0.99, irate(etcd_network_peer_round_trip_time_seconds_bucket[5m]))',
    start_time=stime,
    end_time=etime,
    step=step,
    )


    etcd_disk_sync_df = MetricRangeDataFrame(etcd_disk_sync)
    etcd_disk_sync_df["value"]=etcd_disk_sync_df["value"].astype(float)
    etcd_disk_sync_df.index= pandas.to_datetime(etcd_disk_sync_df.index, unit="s")
    #etcd_disk_syncp_df = etcd_disk_sync_df.pivot( columns='instance' ,values='value')
    print(etcd_disk_sync_df.head()) 
    print("Descriptive stats ofthe data frame", etcd_disk_sync_df["value"].describe())                    
    