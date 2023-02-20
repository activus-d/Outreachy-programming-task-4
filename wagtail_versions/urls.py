from django.urls import path
from . import views

urlpatterns = [
    path('', views.version_list, name='version_list'),
    path('version/<version>/', views.version, name='version'),
]

# handler404 = "wagtail_versions.views.error_404"