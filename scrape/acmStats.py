import pandas
from prometheus_api_client import *



def scrape(pc,stime,etime,step):
    print("Gathering data from ACM....")
    acmManagedCluster(pc,stime,etime,step)

def acmManagedCluster(pc,stime,etime,step):    

    print("")
    print("Number of Managed clusters per ACM Data..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='apiserver_storage_objects{resource=~"managedclusters.cluster.open-cluster-management.io"}',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head())
