"""URL configuration for project project."""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="assignment/index.html")),
    path("admin/", admin.site.urls),
    path("products/", include("assignment.urls")),
]
