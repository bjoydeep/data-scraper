import pandas
from prometheus_api_client import *


def scrape(pc,stime,etime,step):
    print("Gathering data from KubeAPIServer.....")
    kubeAPITestQuery(pc,stime,etime,step)
    kubeAPIResourceCount(pc,stime,etime,step)
    #Does not work
    #def kubeAPIResourceDuration(pc,stime,etime,step)

def kubeAPITestQuery(pc,stime,etime,step):      
    print("")
    print("Test Query..")

    api_server_sum = pc.custom_query_range(
    query='sum(rate(apiserver_request_total{apiserver="kube-apiserver", verb="WATCH"}[5m]))',
    start_time=stime,
    end_time=etime,
    step=step,
    )


    api_server_sum_df = MetricRangeDataFrame(api_server_sum)
    #print(api_server_sum_df.head())
    api_server_sum_df["value"]=api_server_sum_df["value"].astype(float)
    api_server_sum_df.index= pandas.to_datetime(api_server_sum_df.index, unit="s")
   
    print(api_server_sum_df.head())
    print("Shape of the data frame: ", api_server_sum_df.shape)
    print(api_server_sum_df.info())
    print("Descriptive stats ofthe data frame", api_server_sum_df["value"].describe())

def kubeAPIResourceCount(pc,stime,etime,step):     
    print("")
    print("Top 3 APIServer Requests by Resource")

    api_server_count_top =  pc.custom_query_range(
    query='topk(3, sum(rate(apiserver_request_total{apiserver="kube-apiserver"}[5m])) by(resource))',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    api_server_count_top_df = MetricRangeDataFrame(api_server_count_top)
    api_server_count_top_df["value"]=api_server_count_top_df["value"].astype(float)
    api_server_count_top_df.index= pandas.to_datetime(api_server_count_top_df.index, unit="s")
    api_server_count_topp_df = api_server_count_top_df.pivot( columns='resource' ,values='value')
   
    print(api_server_count_topp_df)

def kubeAPIResourceDuration(pc,stime,etime,step):         
    print("")
    print("Top 3 APIServer Request Durations by Resource")
  
    """     
    api_server_duration_top =  pc.custom_query_range(
    query='topk(3,histogram_quantile(0.99, sum(rate(apiserver_request_duration_seconds_bucket{apiserver="kube-apiserver",subresource!="log",verb!~"WATCH|WATCHLIST|PROXY"}[5m])) by(resource,le)))',
    start_time=stime,
    end_time=etime,
    step=step,
    )

    api_server_duration_top_df = MetricRangeDataFrame(api_server_duration_top)
    print(api_server_duration_top_df)
    """

    #api_server_duration_top_df["value"]=api_server_duration_top_df["value"].astype(float)
    #api_server_duration_top_df.index= pandas.to_datetime(api_server_duration_top_df.index, unit="s")
    #api_server_duration_topp_df = api_server_duration_top_df.pivot( columns='resource' ,values='value')
   
    #print(api_server_duration_topp_df)
    