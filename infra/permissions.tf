resource "google_project_iam_member" "project_iam" {
  project = google_project.project.project_id
  role    = "roles/secretmanager.admin"
  member  = "serviceAccount:${google_project.project.project_id}@appspot.gserviceaccount.com"
}

resource "google_project_iam_member" "app_engine" {
  project = google_project.project.project_id
  role    = "roles/appengine.appAdmin"
  member  = "459905785585@cloudbuild.gserviceaccount.com"
}