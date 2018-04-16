import sys, os, re
from pyspark.sql import SparkSession, types, functions
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import monotonically_increasing_id

spark = SparkSession.builder.appName('Big Data Project').getOrCreate()
sc = spark.sparkContext
assert sys.version_info >= (3, 5)  # make sure we have Python 3.5+
assert sc.version >= '2.2'  # make sure we have Spark 2.2+

fall_dataset=spark.read.csv('Fall_Agg_15.csv',header = True)
nonfall_dataset=spark.read.csv('Near_Fall_Agg_15.csv',header = True)
adl_dataset=spark.read.csv('ADL_Agg_15.csv',header= True)

fall_dataset=fall_dataset.withColumn('class_label',functions.lit(1))
nonfall_dataset=nonfall_dataset.withColumn('class_label',functions.lit(0))
adl_dataset=adl_dataset.withColumn('class_label',functions.lit(0))

fall_dataset.write.csv("ClassificationDataset15.csv",header=True,sep=',')
nonfall_dataset.write.csv("ClassificationDataset15.csv",mode="append",header=True,sep=',')
adl_dataset.write.csv("ClassificationDataset15.csv", mode="append",header=True,sep=',')


