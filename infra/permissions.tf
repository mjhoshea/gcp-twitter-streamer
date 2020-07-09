resource "google_project_iam_member" "project_iam" {
  project = google_project.project.project_id
  role    = "roles/secretmanager.admin"
  member  = "serviceAccount:${google_project.project.project_id}@appspot.gserviceaccount.com"
}