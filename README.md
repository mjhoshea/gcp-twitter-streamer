# Google Cloud Platform Twitter Streaming Boilerplate

This repository serves two purposes. Firstly, it provides the boiler plate to
run a bare bones flask app that streams data from twitter and writes it a 
a Google Cloud Storage Bucket. Secondly, it provides the terraform to create
the the infrastructure required to run the flask app and dump the streamed tweets..

## Infrastructure

The /infra directory contains all of the terraform required to create a GCP project
and necessary resources within that project required to run the application.

```bash
export TF_VAR_org_id=YOUR_ORG_ID
export TF_VAR_billing_account=YOUR_BILLING_ACCOUNT_ID
export TF_ADMIN=${USER}-tf-admin
export TF_CREDS=~/.config/gcloud/${USER}-tf-admin.json
```

Org id and billing id can be found with the following

```bash
gcloud organizations list
gcloud beta billing accounts list
```

Enable the following services in the terraform admin project. 

```bash
gcloud config set project ADMIN_PROJECT

gcloud services enable cloudresourcemanager.googleapis.com
gcloud services enable cloudbilling.googleapis.com
gcloud services enable iam.googleapis.com
gcloud services enable appengine.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable secretmanager.googleapis.com
gcloud services enable serviceusage.googleapis.com
```


Apply the terraform

```bash
terraform apply
```

Enable the following services in you newly created project

```bash
gcloud config set project NEW_PROJECT

gcloud services enable secretmanager.googleapis.com
```

Apply the terraform again

```bash
terraform apply
```
### Manual steps

- Cloudbuild: Current you have to manually configure cloud build in the gcp UI. 
- Secrets: You need to manually add your twitter credentials do the secrets
created in secret manager.
- Redeploy: Currently need to deploy, then enable secret manager and then redeploy.

## Application

The /app directory contains a simple flask application that streams data from
twitter and dumps it into a gcs bucket.

