from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("voting_app.urls")),  # Ensure "voting_app.urls" is included for the homepage
]
