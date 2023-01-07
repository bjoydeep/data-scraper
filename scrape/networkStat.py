import pandas
from prometheus_api_client import *



def scrape(pc,stime,etime,step):
    print("Gathering data About Network Usage....")
    clusterNetworkReceived(pc,stime,etime,step)
    nodeNetworkReceived(pc,stime,etime,step)
    acmNetworkReceived(pc,stime,etime,step)
    clusterNetworkTransmit(pc,stime,etime,step)
    nodeNetworkTransmit(pc,stime,etime,step)
    acmNetworkTransmit(pc,stime,etime,step)

def clusterNetworkReceived(pc,stime,etime,step):    

    print("")
    print("Cluster level Received Network Traffic -- this is not correct !!! ..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='sum(irate(container_network_receive_bytes_total{namespace=~".+"}[5m]))',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head())

def nodeNetworkReceived(pc,stime,etime,step):    

    print("")
    print("Node level Received Network Traffic -- this is not correct !!! ..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='instance:node_network_receive_bytes_excluding_lo:rate1m',
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

def acmNetworkReceived(pc,stime,etime,step):    

    print("")
    print("ACM level Received Network Traffic -- this is not correct !!! ..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='sum(irate(container_network_receive_bytes_total{namespace=~"open-cluster-management.*|multicluster-engine"}[5m]))',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head())        

def clusterNetworkTransmit(pc,stime,etime,step):    

    print("")
    print("Cluster level Transmit Network Traffic -- this is not correct !!! ..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='sum(irate(container_network_transmit_bytes_total{}[5m]))',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head())

def nodeNetworkTransmit(pc,stime,etime,step):    

    print("")
    print("Node level Transmit Network Traffic -- this is not correct !!! ..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='instance:node_network_transmit_bytes_excluding_lo:rate1m',
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

def acmNetworkTransmit(pc,stime,etime,step):    

    print("")
    print("ACM level Transmit Network Traffic -- this is not correct !!! ..")

    etcd_db_size = pc.custom_query_range(
    #this query needed to be changed    
    query='sum(irate(container_network_transmit_bytes_total{namespace=~"open-cluster-management.*|multicluster-engine"}[5m]))',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    etcd_db_size_df = MetricRangeDataFrame(etcd_db_size)
    etcd_db_size_df["value"]=etcd_db_size_df["value"].astype(float)
    etcd_db_size_df.index= pandas.to_datetime(etcd_db_size_df.index, unit="s")
    print(etcd_db_size_df.head())            