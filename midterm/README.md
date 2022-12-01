# Stroke Prediction Project

**Files**
* Repository Description: `README.md` *this file
* Data Documentation: `DATA.md` 
* Conda enviroment: `requirements.txt` - used to create conda envirment with `conda create --name <env> --file requirements.txt`. 
  * **Note:** this is not the right format for pip. 
* Notebook: `notebook.ipynb`
* Data: `healthcare-dataset-stroke-data.csv`
* ML script: `service.py`
  * Note: Model is saved locally via bentoml 
* Dependency and enviroment management: `bentofile.yaml`
* Standalone Model Creation Script: `training.py`

## Problem Statement

### By the Numbers

**Global:** Strokes are a global epidemic. They are the second leading cause of death and have increased by 70% between 1990 to 2019, with death from strokes inceasing by 43% (source). The WHO estimates the annual cost of strokes to be over US$721 billion (source).

**United State:** While strokes have been declining for decades in the US, it still has a large financial burden, amounting to $53 billion annually (source). Currently, stroke is the 5th leading cause of death in the US.

### Optimal Outcomes

**Model Goal:** To predict stroke likely patients.

**Global:** Predicting a stroke can provide an opportunity to take corrective actions before a stroke occurs. Most importantly, resulting in fewer deaths and disabilities.

Additionally, the money lost to strokes would boost economies. Assuming cost and stroke occurrence are linear, if strokes were reduced by just 5%, that would inject $36 billion into world economies.

**United State:** And $2.65 billion into the US economy.

### Machine Learning (ML)
**Machine Learning goal:**

Provide stroke risk prediction so that people may understand their risk rate in a meaningful manner. Predictions will be Low, Moderate, and High. These values were chosen because they would provide better context to the average person rather than a risk percentage. For example, a risk of 15% may not be clear if it is a need for concern or not. 

**Why Machine Learning?**

ML is best suited for complex problems that are not answered by simple logic. In healthcare, disease epidemiology is often complex and our understanding changing. This makes diseases, such as stroke, prime candidates for ML.

## Instructions
* To access and test the API see the section below `Production App Access`.
* For a quick review: select `notebook.ipynb` in the respository and scroll.
* To run: Open `notebook.ipynb` in google Colab (link at top of notebook) recommended.
  * The notebook can be downloaded and run on a local Jupyter instance but it is optimized for Google Colab for review purposes.  
  * In Colab select `Runtime` from the top menu, then `Run All`.
  * A popup will appear, select `Run Anyways`. 
  
### notebook.ipynb

* **The notebook has been optimized for Google Colab**

* Throughout this notebook you will find links to further understanding or clarification of various concepts. 

* Dataprep may fail (though appears resolved recently) and give the error: `TypeError: Callbacks must be either Callback or tuple`, this means the kernal needs to be restarted, see !pip below.

* **!pip:** Check !pip for alerts stating the kernal needs to restart. If you see this alert, just click the `Restart Runtime` button provided by the error. This is an issue with Google colab and `!pip install dask` is the culprit. Click Yes on the popup and then go ahead and run it all again.

* **Notebook Index** is your guide to exploring the notebook and has links to different sections. Alternatively, you can expand the hamburger icon on the left pane.

### Environment
* see `notebook.ipynb` section!PIP
  
### Containerization: 
  * In `notebook.ipynb`, see section section *Deployment*, then subsection *BentoML* on build instructions.
  * To build a bento instance for a live test, the notebook must be run on a local Jupyter instance.
  * Script creation is done in the notebook with the use of [magic code](https://ipython.readthedocs.io/en/stable/interactive/magics.html) to create files in the notebook directory.
  * Bentoml commands are listed but not run from the notebook.
  
### Cloud deployment: 
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

## Production App Access

**Instructions**

1.) To access the production site go here: http://3.91.93.14:3000/

2.) Select Try it out in the POST section.

![image](https://user-images.githubusercontent.com/83911983/200917321-a0adb65c-1972-48b0-a90b-36bb2e35ad7d.png)

3.) In the Request body enter patient information based on the template or paste in the example patient. Select Execute.

![image](https://user-images.githubusercontent.com/83911983/200917598-1bb98d39-258f-46c5-8039-934e4840c4ca.png)

**Template**
* All values must be filled in.
* Strings must be within double quotes " "
* Float values must be in format 0.0
* Capitalization for values must be followed

{

"gender": "Male" or "Female",

"age": float,

"hypertension": 1 or 0,

"heart_disease": 1 or 0,

"ever_married": 1 or 0,

"work_type": "Private" or "Self-employed" or "children" or "Govt_job" or "Never_worked",

"residence_type": "Urban" or "Rural",

"avg_glucose_level": float,

"bmi": float,

"smoking_status": "smokes" or "never smoked" or "Unkown" or "formerly smoked",

"obese": 1 or 0,

"clearly_diabetes": 1 or 0

}

**Example Patient**

{

"gender": "Male",

"age": 69.0,

"hypertension": 0,

"heart_disease": 1,

"ever_married": 1,

"work_type": "self_employed",

"residence_type": "Urban",

"avg_glucose_level": 195.23,

"bmi": 28.3,

"smoking_status": "smokes",

"obese": 0,

"clearly_diabetes": 1

}

4.) Scroll down to Server response and see the response in the Response body.
Possible Responses:

* "Stroke Risk: HIGH"
* "Stroke Risk: MODERATE"
* "Stroke Risk: LOW"

![image](https://user-images.githubusercontent.com/83911983/200917718-c85185b6-d5ae-4f57-90e4-9552ef1a3837.png)
