resource "google_app_engine_application" "app" {
  project     = google_project.project.project_id
  location_id = "europe-west2"
}