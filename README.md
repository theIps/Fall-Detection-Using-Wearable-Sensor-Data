## Fall-Detection-Using-Wearable-Sensor-Data

# Exploratory Data Analysis-
EDA_BigDataLabProject**.ipynb contains the EDA part for different window sizes for fall/non-fall classification(** corresponds to 10,15,20,25 window sizes)
EDA_BigDataLabProject** Multi.ipynb contains the EDA part for different window sizes for Multi classification(** corresponds to 10,15,20,25 window sizes)
Following tasks are done during EDA-
-Making training and testing dataset
-Feature Engineering
-Feature Exploration
-Feature Selection using VarianceThreshold and Correlation methods
-Selecting Top20 features corresponding to fall/non-fall classification
-Selecting Top10 features corresponding to multi classification
-Selecting Same features in training and testing dataset.
-Applying various models
-Comparing the models on basis of sensitivity and specificity

# window**
(** correspond to 10,15,20,25 window sizes)
Each folder contains files related to that window size in which
- fall**.py , nearfall**.py, adl**.py in this the selected records are fetched for various subcategories in fall, nearfall and adl trials.
-fallagg**.py , nearfallagg**.py, adlagg**.py in this the fetched records are aggregated for various subcategories in fall, nearfall and adl trials.
-dataset**.py is preparing dataset for fall/non-fall classification
-datasetmulti**.py is preparing dataset for Multi classification

