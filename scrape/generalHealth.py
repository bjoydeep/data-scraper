import pandas
from prometheus_api_client import *



def scrape(pc,stime,etime,step):
    print("Gathering data About General Health....")
    podRestarts(pc,stime,etime,step)
    
def podRestarts(pc,stime,etime,step):    

    print("")
    print("Pod Restarts Greater Than 3..")

    etcd_db_size = pc.custom_query_range(
    query='sum(kube_pod_container_status_restarts_total{}) by (container) > 3',
    start_time=stime,
    end_time=etime,
    step=step,
    )


    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head())
    etcd_db_sizep_df = etcd_db_size_df.pivot( columns='container' ,values='value')
    print(etcd_db_sizep_df.head())
    
    #print("Shape of the data frame: ", etcd_db_size_df.shape)
    #print(etcd_db_size_df.info())
    #print("Descriptive stats ofthe data frame", etcd_db_size_df["value"].describe())
