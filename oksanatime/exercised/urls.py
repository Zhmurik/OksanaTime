from django.urls import path

from . import views

app_name = 'exercised'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:exercise_id>/', views.detail, name='detail'),
    path('equipment/', views.equipmentViews, name='equipment')
]
