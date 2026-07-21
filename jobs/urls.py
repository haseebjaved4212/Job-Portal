from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name='job-list'),
    path('job/<int:pk>/', views.JobDetailView.as_view(), name='job-detail'),
    path('job/new/', views.JobCreateView.as_view(), name='job-create'),
    path('job/<int:pk>/edit/', views.JobUpdateView.as_view(), name='job-update'),
    path('job/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job-delete'),
    path('my-jobs/', views.MyJobsListView.as_view(), name='my-jobs'),
    path('apply/<int:pk>/', views.apply_to_job, name='apply-to-job'),
    path('my-applications/', views.MyApplicationsListView.as_view(), name='my-applications'),
]
