import pandas
from prometheus_api_client import *



def scrape(pc,stime,etime,step):
    print("Gathering data About CPU Usage....")
    clusterCPUUsage(pc,stime,etime,step)
    acmCPUUsage(pc,stime,etime,step)
    openshiftKubeAPICPUUsage(pc,stime,etime,step)
    observabilityCPUUsage(pc,stime,etime,step)
    observabilityReceiverCPUUsage(pc,stime,etime,step)
    assistedCPUUsage(pc,stime,etime,step)
    etcdCPUUsage(pc,stime,etime,step)
    nodeCPUUsage(pc,stime,etime,step)
    
def clusterCPUUsage(pc,stime,etime,step):    

    print("")
    print("Cluster CPU Usage..")

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

def acmCPUUsage(pc,stime,etime,step):    

    print("")
    print("ACM CPU Usage..")

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

def openshiftKubeAPICPUUsage(pc,stime,etime,step):    

    print("")
    print("OpenShift KubeAPIServer CPU Usage..")

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

def observabilityCPUUsage(pc,stime,etime,step):    

    print("")
    print("Observability CPU Usage..")

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

def observabilityReceiverCPUUsage(pc,stime,etime,step):    

    print("")
    print("Observability Receiver CPU Usage..")

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

def assistedCPUUsage(pc,stime,etime,step):    

    print("")
    print("Assisted Installer CPU Usage..")

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

def etcdCPUUsage(pc,stime,etime,step):    

    print("")
    print("etcd pods CPU Usage..")

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

def nodeCPUUsage(pc,stime,etime,step):    

    print("")
    print("Node (Master or Worker???) CPU Usage..")

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