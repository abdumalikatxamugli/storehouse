from django.urls import path
from . import views

urlpatterns=[
	path('categories/', views.categories_list),
	path('categories/create/', views.categories_create),
	path('categories/delete/<int:pk>/', views.categories_delete),
	path('categories/<int:pk>', views.categories_update),
]