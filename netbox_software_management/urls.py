from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView


urlpatterns = (
    path('software-version/', views.SoftwareVersionListView.as_view(), name='softwareversion_list'),
    path('software-version/add/', views.SoftwareVersionEditView.as_view(), name='softwareversion_add'),
    path('software-version/<int:pk>/', views.SoftwareVersionView.as_view(), name='softwareversion'),
    path('software-version/<int:pk>/edit/', views.SoftwareVersionEditView.as_view(), name='softwareversion_edit'),
    path('software-version/<int:pk>/delete/', views.SoftwareVersionDeleteView.as_view(), name='softwareversion_delete'),
    path('software-version/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='softwareversion_changelog', kwargs={
        'model': models.SoftwareVersion
    }),
)