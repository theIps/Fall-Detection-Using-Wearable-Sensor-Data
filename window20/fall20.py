import sys, os, re
from pyspark.sql import SparkSession, types, functions
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import monotonically_increasing_id 

spark = SparkSession.builder.appName('Big Data Project').getOrCreate()
sc = spark.sparkContext
assert sys.version_info >= (3, 5)  # make sure we have Python 3.5+
assert sc.version >= '2.2'  # make sure we have Spark 2.2+

cat_dict={'SLIP':1,'TRIP':2,'CS':3,'DS':4,'HB':5,'LCC':6,'RS':7}
def string_to_float(col):
    return float(col)
count=1
for i in range(6,11):   
#     for j in ['SLIP','TRIP']:
    for j in ['SLIP','TRIP','CS','DS','HB','LCC','RS']:
        for k in range(1,4):
            train_fall=spark.read.csv('/user/psa83/IMU_Dataset/sub'+\
                                      str(i)+'/Falls/'+j+str(k)+'.csv',header = True)
            subject_id=i
            trial_id=k
            category_id=cat_dict[j]

            udf_float=functions.udf(string_to_float, returnType=types.FloatType())
            columns=train_fall.schema.names
            for column in columns:
                train_fall=train_fall.withColumnRenamed(column,column.replace(".", ""))
            columns=train_fall.schema.names
            for column in columns:
                train_fall=train_fall.withColumnRenamed(column,column.split('(')[0])
            columns=train_fall.schema.names
            for column in columns:
                train_fall=train_fall.withColumn(column+'_flt',udf_float(column)).drop(column)
                train_fall=train_fall.withColumnRenamed(column+'_flt',(column+'_flt').replace(" ", ""))
                
            
            train_fall = train_fall.select("*").withColumn("id", monotonically_increasing_id())
            train_fall.createOrReplaceTempView('fall')
            df_fall=spark.sql('''select id from fall where waistAccelerationX_flt in (
            (select MAX(ABS(waistAccelerationX_flt)) from fall),-(select MAX(ABS(waistAccelerationX_flt)) from fall) )''')
            
            max_id=df_fall.head()['id']
            train_fall.createOrReplaceTempView('window')
            df_fall=spark.sql('select * from fall where id between '+str(max_id-120) +' and '+str(max_id+120))
            
            df_fall=df_fall.withColumn('subject_id',functions.lit(subject_id))
            df_fall=df_fall.withColumn('category_id',functions.lit(category_id))
            df_fall=df_fall.withColumn('trial_id',functions.lit(trial_id))           
           # df_fall.select('subject_id','category_id','trial_id').show(5) 
            print(subject_id,category_id,trial_id)	
            df_fall.write.csv("Fall20.csv", mode="append",header=True,sep=',')	      
           # if(count==1):
           #     df_final=df_fall
           # else:
           #     df_final=df_final.union(df_fall)
           # count+=1
#df_final.coalesce(1).write.csv('Fall58.csv',sep=',',header=True)
