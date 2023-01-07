import pandas
from prometheus_api_client import *



def scrape(pc,stime,etime,step):
    print("Gathering data About Memory Usage....")
    clusterMemoryUsage(pc,stime,etime,step)
    acmMemoryUsage(pc,stime,etime,step)
    openshiftKubeAPIMemoryUsage(pc,stime,etime,step)
    observabilityMemoryUsage(pc,stime,etime,step)
    observabilityReceiverMemoryUsage(pc,stime,etime,step)
    assistedMemoryUsage(pc,stime,etime,step)
    etcdMemoryUsage(pc,stime,etime,step)
    nodeMemoryUsage(pc,stime,etime,step)
    
def clusterMemoryUsage(pc,stime,etime,step):    

    print("")
    print("Cluster Memory Usage..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='sum(container_memory_working_set_bytes{namespace!="minio", container!=""})',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head())
    
    #etcd_db_sizep_df = etcd_db_size_df.pivot( columns='container' ,values='value')
    #print(etcd_db_sizep_df.head())

def acmMemoryUsage(pc,stime,etime,step):    

    print("")
    print("ACM Memory Usage..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='sum(container_memory_working_set_bytes{namespace!="minio", container!="",namespace=~"open-cluster-management.*|multicluster-engine"})',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head()) 

def openshiftKubeAPIMemoryUsage(pc,stime,etime,step):    

    print("")
    print("OpenShift KubeAPIServer Memory Usage..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='sum(container_memory_working_set_bytes{namespace!="minio", container!="",namespace=~"openshift-kube-apiserver.*"})',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head()) 

def observabilityMemoryUsage(pc,stime,etime,step):    

    print("")
    print("Observability Memory Usage..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='sum(container_memory_working_set_bytes{namespace!="minio", container!="",namespace="open-cluster-management-observability"})',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head())

def observabilityReceiverMemoryUsage(pc,stime,etime,step):    

    print("")
    print("Observability Receiver Memory Usage..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='sum(container_memory_working_set_bytes{namespace!="minio", pod=~"observability-thanos-receive-default.+", container!=""})',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head())     

def assistedMemoryUsage(pc,stime,etime,step):    

    print("")
    print("Assisted Installer Memory Usage..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='sum(container_memory_working_set_bytes{namespace!="minio", container!="",namespace="multicluster-engine",pod=~"assisted-.*service-.*"})',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head())  

def etcdMemoryUsage(pc,stime,etime,step):    

    print("")
    print("etcd pods Memory Usage..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='sum(avg_over_time(container_memory_working_set_bytes{container="",pod!="", namespace=~"openshift-etcd.*"}[5m])) BY (pod, namespace)',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head())                  

def nodeMemoryUsage(pc,stime,etime,step):    

    print("")
    print("Node (Master or Worker???) Memory Usage..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='sum by(node) (container_memory_working_set_bytes{namespace!="minio", container!=""})',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head())                      