from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import split, regexp_extract, col
from os import listdir
from os.path import isfile, join
import shutil
import sys, getopt
import utils

def setup_spark_context():
    return SparkContext("local", "NASA Data Set Analysis")

def main(log_file):
    sc = setup_spark_context()

    sqlContext = SQLContext(sc)
    try:
        sql_log_data = sqlContext.read.text(log_file)
    except:
        print("######################")
        print("Bad file name!")
        return

    splited_data_frame = sql_log_data.select(regexp_extract('value', r'^([^\s]+\s)', 1).alias('host'),
            regexp_extract('value', r'^.*\[(\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} -\d{4})]', 1).alias('timestamp'),
            regexp_extract('value', r'^.*"\w+\s+([^\s]+)\s+HTTP.*"', 1).alias('request'),
            regexp_extract('value', r'^.*"\s+([^\s]+)', 1).cast('integer').alias('http_status'),
            regexp_extract('value', r'^.*\s+(\d+)$',1).cast('integer').alias('content_size_in_bytes'))

    splited_data_frame.cache()

    data_frames = {}

    data_frames['unique_hosts'] = splited_data_frame.groupBy('host').count().filter('count = 1').select('host')

    data_frames['total_http_404'] = splited_data_frame.groupBy('http_status').count().filter('http_status = "404"')

    data_frames['top_5_hosts_http_404'] = splited_data_frame.filter('http_status = "404"').groupBy('request').count().sort(col("count").desc()).limit(5)

    data_frames['qty_http_404_per_day'] = splited_data_frame.filter('http_status = "404"').groupBy(splited_data_frame.timestamp.substr(1,11).alias('day')).count()

    data_frames['sum_bytes '] = splited_data_frame.select('content_size_in_bytes').groupBy().sum()

    utils.export_all_queries_to_csv(data_frames)

if __name__== "__main__":
    main(sys.argv[1])
