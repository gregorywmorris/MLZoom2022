
Files:
* Data dictionary: `LCDataDictionary.xlsx`
    * Referenced from [here](https://figshare.com/articles/dataset/Lending_club_dataset_description/20016077)
* Data: `lendingclub-1.csv` and `lendingclub-2.csv` 
    * Referenced in this [article](https://towardsdatascience.com/end-to-end-case-study-classification-lending-club-data-489f8a1b100a) and downloaded from [here](https://drive.google.com/drive/folders/1A74WpM8ayIfvzfrkFRFzFyBh27djL4YE)
    * Cleanded data: to train model `lc_clean.csv`; to test model `lc_test.csv`
* Notebook: `LendingClub.ipynb`
* Model Script: `training.py`
* Envronment file: `requirements.txt`
* bentoml: `bentofile.yaml` and `service.py`


## Project Criteria

* **Problem description:** Lending Club is a money loan service that operates online. To reduce risk and maximize profits management would like to reduce the opportunity for human error in identifying and approving loans. 
   * The first requirement: Do not approve loans that are high risk (less than 50% likelihood of payback).
   * The second requrement: Approve loans for those that meet the criteria of above 50% threshhold and identify them as either moderate risk (50-80%) or low risk (greater than 80%).
* **EDA:** see `LendingClub.ipynb`
* **Model training:** see `LendingClub.ipynb` or `training.py`
* **Export notebook to script:** see `training.py`
* **Reproduceability:** see section on Cloud Deployement below
* **Model Deployment:** see `deployment.pdf`
* **Dependency and enviroment management:** Anaconda see `requirements.txt`
* **Containerization:** Containerized via bentoml see `LendingClub.ipynb` or `training.py`


### Cloud Deployment: 

**Step 1 Bentoml**

* train and save model with `training.py` or `LendingClub.ipynb`
* build bento: `bentoml build`
* docker container: `bentoml containerize [bento name:code given after 'bentoml build']`
* *make sure docker service is running if setting up locally. Then run this command line:*
    * run docker contianer: `docker run -it --rm -p 3000:3000 [bento name:code given after 'bentoml build'] serve --production`

**Step 2 AWS**

  1. log in to AWS Console 
  2. Go to Elastic Container Registry. Select `Create Registry`.
  3. In the registry select `View push commands`
   * On local Windows PC use GitBash and follow macOS/Linux commands.NOTE: Must have AWS CLI installed.
   * `AWS console`, log in via the prompts.
   * `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin [censored].dkr.ecr.us-east-1.amazonaws.com`
   * Skip this command, docker build done though bentoml -> `docker build -t stroke_prediction .` 
   * `docker tag stroke_prediction:latest [censored].dkr.ecr.us-east-1.amazonaws.com/stroke_prediction:latest`
   *  `docker push [censored].dkr.ecr.us-east-1.amazonaws.com/stroke_prediction:latest`
  4. Move to Elastic Container Service, then Select `Create new Task Definition`.
   * Follow prompts, and be sure to select the image uploaded to the registry.
   * Then select `Create`
  5. Select `Clusters` on the left pane, then Select `create cluster`. 
   * Follow the prompts to create a cluster
   * Select the cluster
   * Select `Tasks` and then `Run new Task`
   * Follow the prompts and select the created task.
      * Select `Run Task` 
