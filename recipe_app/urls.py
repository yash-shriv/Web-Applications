from django.urls import path
from . import views
from .views import receipes, contact, about, success_page

urlpatterns = [
    path('', views.receipes, name='receipes'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('success-page/', views.success_page, name='success_page'),
    path('delete/<int:id>/', views.delete_recipe, name='delete_recipe'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
]
