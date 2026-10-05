from django.urls import path
from django.views.generic import RedirectView

from . import views


app_name = "website"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("products/", views.products, name="products"),
    path("products/lmvp-switchgear/<slug:item_slug>/", views.lmvp_product_detail, name="lmvp_product_detail"),
    path("products/<slug:slug>/", views.product_detail, name="product_detail"),
    path("services/", views.services, name="services"),
    path("services/pv-solar-epc/", RedirectView.as_view(pattern_name="website:pv_solar_epc", permanent=True), name="old_pv_solar_epc"),
    path("services/<slug:slug>/", views.service_detail, name="service_detail"),
    path("projects/", views.projects, name="projects"),
    path("opportunities/", views.opportunities, name="opportunities"),
    path("opportunities/pv-solar-epc/", views.pv_solar_epc, name="pv_solar_epc"),
    path("opportunities/project-capital-partners/", views.project_capital_partners, name="project_capital_partners"),
    path("contact/", views.contact, name="contact"),
]
