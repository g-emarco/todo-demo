# GCP CI/CD Shift left security demo and tutorial
This demo demonstrates shift left security pratice with Google Cloud Build, Cloud Run, Artifact Registry, Container Analysis, Bandit and Kritis, slack integraiton. 


## Preview
<img width="1919" alt="Screen Shot 2022-08-25 at 17 06 06" src="https://user-images.githubusercontent.com/111509936/186687012-a6c38896-9bcb-4ef3-a961-5d6c946f0cd3.png">

## Run application locally
From root directory
```bash
flask run
```

## Cloud Build CI/CD Setup

Create a _Cloud Build_ trigger from your desired repository and trigger method
make sure to select the option of:

<img width="568" alt="image" src="https://user-images.githubusercontent.com/111509936/187224001-e83321df-5135-431a-9c7e-706d8e68fd3b.png">


Create a ```cloud-builds``` topic in pubsub (Cloud Build will publish here build results)
```bash
gcloud pubsub topics create cloud-builds
```

Create the Artifact Registry repository (Cloud build will push the image artifact to this repository)
```bash
gcloud artifacts repositories create todo-demo2 --location=us-east1 \
--repository-format=docker
```

## Enable GCP relevant services API's 

```bash
gcloud services enable cloudbuild.googleapis.com   containerregistry.googleapis.com
containerscanning.googleapis.com   cloudkms.googleapis.com. artifactregistry.googleapis.com
```

## Set up the Kritis Signer custom builder
prerequiste for security policy enforcment build step) 
Refrenced from [Binary Authorization attestations tutorial](https://cloud.google.com/binary-authorization/docs/creating-attestations-kritis).

enable Cloud Build to access Container Analysis API (so it can fetch for each image the result fo the vulnrablity scan)
```bash
gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com --role roles/containeranalysis.notes.editor
gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com --role roles/containeranalysis.notes.occurrences.viewer
gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com --role roles/containeranalysis.occurrences.editor
```

Clone the Kritis repository 
```bash
git clone https://github.com/grafeas/kritis.git
```

Navigate to the ```kritis/``` directory
```bash
cd kritis
```

Build and register Kritis Signer custom builder
```bash
gcloud builds submit . --config deploy/kritis-signer/cloudbuild.yaml
```

## Cloud Build Slack CI/CD notification integration (Optional)

Navigate to the ```cloud-functions/``` directory

```bash
cd cloud-functions
```

Create staging bucket for Slack Integration code
```bash
gsutil mb gs://${PROJECT_ID}_gcb-slack-integration
```

Deploy python Cloud function subsribed to ```cloud-builds``` topic created earler
```bash
gcloud functions deploy slack_integration
--stage-bucket ${PROJECT_ID}_gcb-slack-integration --trigger-topic cloud-builds --runtime python38
```

Add a new secret to ```Secret Manager``` with the identifier: ```slack-webhook-url``` 
the secret value should be taken from the slack portal as the webhook URL for a created Slack application

Grant the function permission to access this secret (it is used in the python script)



