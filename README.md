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


## Website-
- "website" folder contains all files related to website
- To run the website, do following steps-
1. Copy all these files to Home/ directory
2. Open terminal, create a http server using python by executing following command-
   python -m http.server
3. Install "Allow Access Control" extension on chrome
4. Run the website by clicking on frontend.html
