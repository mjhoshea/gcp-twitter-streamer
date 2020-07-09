variable "secret-names" {
  type = list(string)
  default = [
    "twitter_consumer_key",
    "twitter_consumer_secret",
    "twitter_access_token",
    "twitter_access_token_secret"]
}



resource "google_secret_manager_secret" "secret" {
  count = length(var.secret-names)
  project = google_project.project.project_id
  secret_id = var.secret-names[count.index]

  replication {
    automatic = true
  }
}


