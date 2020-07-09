variable "project_name" {
}

variable "billing_account" {
  default = "01E684-5890D9-9F92D9"
}

variable "org_id" {
  default = "1059487829153"
}
variable "region" {
  default = "europe-west2"
}

provider "google-beta" {
  region = var.region
}

resource "random_id" "id" {
  byte_length = 4
  prefix      = var.project_name
}


resource "google_project" "project" {
  name            = var.project_name
  project_id      = random_id.id.hex
  billing_account = var.billing_account
  org_id          = var.org_id
}

output "project_id" {
  value = google_project.project.project_id
}

