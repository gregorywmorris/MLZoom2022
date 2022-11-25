# Stroke Prediction Dataset (SPD)
This dataset is used to predict whether a patient is likely to have a stroke based on the input parameters like gender, age, various diseases, and smoking status. Each row in the data provides relevant information about the patient.

#### Dataset Link
<!-- info: Provide a link to the dataset: -->
<!-- width: half -->
[Kaggle Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)

#### Data Card Author(s)
<!-- info: Select **one role per** Data Card Author:

(Usage Note: Select the most appropriate choice to describe the author's role
in creating the Data Card.) -->
<!-- width: half -->

- **Gregory Morris, Team: Machine Learning**


## Authorship
### Publishers
#### Publishing Organization(s)
<!-- scope: telescope -->
<!-- info: Provide the names of the institution or organization responsible
for publishing the dataset: -->

Kaggle

#### Industry Type(s)
<!-- scope: periscope -->
<!-- info: Select **all applicable** industry types to which the publishing
organizations belong: -->

- Academic - Tech


#### Point of Contact (POC) Detail(s)
<!-- scope: microscope -->
<!-- info: Provide publisher contact details: -->
- **Publishing POC:** N/A
- **Affiliation:** N/A
- **Contact:** N/A
- **Mailing List:** N/A
- **Website:** https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

### Dataset Owners
#### Team(s)
<!-- scope: telescope -->
<!-- info: Provide the names of the groups or team(s) that own the dataset: -->
Kaggle Contributor

#### Contact Detail(s)
<!-- scope: periscope -->
<!-- info: Provide pathways to contact dataset owners: -->
- **Dataset Owner(s):** Federico Soriano Palacios
- **Affiliation:** Contributor
- **Contact:** N/A
- **Group Email:** N/A
- **Website:** https://www.linkedin.com/in/federico-soriano-palacios/

#### Author(s)
<!-- scope: microscope -->
<!-- info: Provide the details of all authors associated with the dataset:

(Usage Note: Provide the affiliation and year if different from publishing
institutions or multiple affiliations.) -->
- Federico Soriano Palacios, Contributor, 2020


### Funding Sources
#### Institution(s)
<!-- scope: telescope -->
<!-- info: Provide the names of the funding institution(s): -->
N/A
#### Funding or Grant Summary(ies)
<!-- scope: periscope -->
<!-- width: full -->
<!-- info: Provide a short summary of programs or projects that may have funded
the creation, collection, or curation of the dataset.

Use additional notes to capture any other relevant information or
considerations. -->
N/A


## Dataset Overview
#### Data Subject(s)
<!-- scope: telescope -->
<!-- info: Select ***all applicable**** subjects contained the dataset: -->

- Sensitive Data About People
  - Personal Health Information (PHI) that has been anonymized
- Medical Data


#### File Snapshot
<!-- scope: periscope -->
<!-- info: Provide a snapshot of the dataset:<br><br>(Use the additional notes
to include relevant information, considerations, and links to table(s) with
more detailed breakdowns.) -->
Category | Data
--- | ---
File Type(s) | CSV
Size of Dataset | 316.97 KB
Number of Observations | 5110
Number of Features | 12


#### Dataset Snapshot
<!-- scope: microscope -->
<!-- info: Provide a short description of the content in a data point: -->
 #|   Column|            Non-Null Count|  Dtype|  
|---|---|---|---|
 0|   gender|             5110 non-null|   object| 
 1|   age|                5110 non-null|   float64|
 2|   hypertension|       5110 non-null|   int64|  
 3|   heart_disease|      5110 non-null|   int64|  
 4|   ever_married|       5110 non-null|   object| 
 5|   work_type|          5110 non-null|   object| 
 6|   residence_type|     5110 non-null|   object| 
 7|   avg_glucose_level|  5110 non-null|   float64|
 8|   bmi|                4909 non-null|   float64|
 9|   smoking_status|     5110 non-null|   object| 
 10|  stroke|             5110 non-null|  int64| 

**Additional Notes:** Excludes ID Column

#### Descriptive Statistics
<!-- width: full -->
<!-- info: Provide basic descriptive statistics for each field. --->

 
Statistic | age | hypertension| heart_disease | avg_glucose_level | bmi |stroke
|---|---|---|---|---|---|---|
count|	5110|	110|	5110|	5110|	4909|	5110|
mean|	43.226614|	0.097456|	0.054012|	106.147677|	28.893237|	0.048728|
std|	22.612647|	0.296607|	0.226063|	45.283560|	7.854067|	0.215320|
min|	0.080000|	0.000000|	0.000000|	55.120000|	10.300000|	0.000000|
25%|	25.000000|	0.000000|	0.000000|	77.245000|	23.500000|	0.000000|
50%|	45.000000|	0.000000|	0.000000|	91.885000|	28.100000|	0.000000|
75%|	61.000000|	0.000000|	0.000000|	114.090000|	33.100000|	0.000000|
max|	82.000000|	1.000000|	1.000000|	271.740000|	97.600000|	1.000000|
