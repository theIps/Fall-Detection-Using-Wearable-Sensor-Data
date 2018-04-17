# Fall-Detection-Using-Wearable-Sensor-Data

## Data Preparation (window**)
(** correspond to 10,15,20,25 window sizes)
- Each folder contains files related to that window size in which :-
- fall**.py , nearfall**.py, adl**.py in this the selected records are fetched for various subcategories in fall, nearfall and adl trials.
- fallagg**.py , nearfallagg**.py, adlagg**.py in this the fetched records are aggregated for various subcategories in fall, nearfall and adl trials.
- dataset**.py is preparing dataset for fall/non-fall classification
- datasetmulti**.py is preparing dataset for Multi classification


## Exploratory Data Analysis-
- EDA_BigDataLabProject**.ipynb contains the EDA part for different window sizes for fall/non-fall classification(** corresponds to 10,15,20,25 window sizes)
- EDA_BigDataLabProject** Multi.ipynb contains the EDA part for different window sizes for Multi classification(** corresponds to 10,15,20,25 window sizes)
- Following tasks are done during EDA-
1. Making training and testing dataset
2. Feature Engineering
3. Feature Exploration
4. Feature Selection using VarianceThreshold and Correlation methods
5. Selecting Top20 features corresponding to fall/non-fall classification
6. Selecting Top10 features corresponding to multi classification
7. Selecting Same features in training and testing dataset.
8. Applying various models
9. Comparing the models on basis of sensitivity and specificity


## Machine Learning
1. BDProj.ipynb: This file contains Spark MLlib code corresponding to fall/non-fall classification. 
2. BDProj2.ipynb: This file contains Spark MLlib code corresponding to Multi classification. 


## Kafka-
There are 2 codes corresponding to kafka:
1. kafka_producer: In this code we are publishing the data in to the topic 'test' of the kafka message broker. The published data is collected from the sensors. We are publishing the data at the similar rate to the one collected from the actual trials in order to keep the stream rate close to real-time. 

2. spark_kafka_consumer: In this program, we are consuming the data from the kafka message broker in to the spark streaming context. Then we are loading the saved trained machine learning model in to program execution.

The structured streaming is vectorized and prediction is made on the transformed dataframe using the loaded model. These predictions are shown on the console. 


## Website-
- "website" folder contains all files related to website
- To run the website, do following steps-
1. Copy all these files to Home/ directory
2. Open terminal, create a http server using python by executing following command-
   python -m http.server
3. Install "Allow Access Control" extension on chrome
4. Run the website by clicking on frontend.html


