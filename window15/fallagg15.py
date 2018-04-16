import sys, os, re
from pyspark.sql import SparkSession, types, functions
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import monotonically_increasing_id 

spark = SparkSession.builder.appName('Big Data Project').getOrCreate()
sc = spark.sparkContext
assert sys.version_info >= (3, 5)  # make sure we have Python 3.5+
assert sc.version >= '2.2'  # make sure we have Spark 2.2+


def string_to_float(col):
    return float(col)

fall_agg=spark.read.csv('Fall15.csv',header = True)

udf_float=functions.udf(string_to_float, returnType=types.FloatType())
columns=fall_agg.schema.names
for column in columns:
	fall_agg=fall_agg.withColumn(column+'_f',udf_float(column)).drop(column)
        
fall_agg=fall_agg.drop('Time_flt_f')
columns=fall_agg.schema.names
temp=''

for name in columns:
    temp=temp+"avg(abs("+name+")),variance(abs("+name+")),"
  
   
temp=temp.rstrip(",")
fall_agg.createOrReplaceTempView("aggregate")
fall_agg=spark.sql('''select '''+temp+'''
from aggregate group by subject_id_f,category_id_f,trial_id_f''')
fall_agg.write.csv("Fall_Agg_15.csv",header=True,sep=',')


