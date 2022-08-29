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

Create a ```cloud-builds``` topic in pubsub (Cloud Build will publish here build results)
```bash
gcloud pubsub topics create cloud-builds
```

## Enable GCP relevant services API's 

```bash
gcloud services enable cloudbuild.googleapis.com   containerregistry.googleapis.com
containerscanning.googleapis.com   cloudkms.googleapis.com
```

## Set up the Kritis Signer custom builder
prerequiste for security policy enforcment build step) 
Refrenced from [Binary Authorization attestations tutorial](https://cloud.google.com/binary-authorization/docs/creating-attestations-kritis).


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

Deploy python Cloud function subsribed to ```cloud-builds``` topic created earler
```bash
gcloud functions deploy slack_integration
--stage-bucket ${PROJECT_ID}_gcb-slack-integration --trigger-topic cloud-builds --runtime python38
```




