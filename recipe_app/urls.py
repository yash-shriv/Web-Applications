from django.urls import path
from . import views
from .views import receipes, contact, about, success_page

urlpatterns = [
    path('', views.receipes, name='receipes'),
    # path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('success-page/', views.success_page, name='success_page'),
    # path('recipes/delete/<int:id>/', views.delete_recipe, name='delete_recipe'),
    path('delete/<int:id>/', views.delete_recipe, name='delete_recipe'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),  # New edit URL
]
