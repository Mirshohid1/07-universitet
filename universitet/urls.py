from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('faculties/', views.faculties, name='faculties'),
    path('students/', views.students, name='students'),
    path('kafedras/', views.kafedras, name='kafedras'),
    path('subjects/', views.subjects, name='subjects'),
    path('teachers/', views.teachers, name='teachers'),
    path('groups/', views.groups, name='groups'),
]