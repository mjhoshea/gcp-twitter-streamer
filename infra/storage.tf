# Create a GCS Bucket
resource "google_storage_bucket" "bucket" {
  project = google_project.project.project_id
  name     = google_project.project.project_id
  location = var.region
}