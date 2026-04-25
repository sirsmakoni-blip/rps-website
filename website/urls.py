from django.urls import path

from . import views


app_name = "website"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("products/", views.products, name="products"),
    path("products/<slug:slug>/", views.product_detail, name="product_detail"),
    path("services/", views.services, name="services"),
    path("services/<slug:slug>/", views.service_detail, name="service_detail"),
    path("projects/", views.projects, name="projects"),
    path("contact/", views.contact, name="contact"),
]

