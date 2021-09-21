from django.urls import path
from . import views

urlpatterns=[
	path('categories/', views.CategoryListView.as_view()),
	path('categories/<int:pk>/', views.CategoryDetailView.as_view()),

	path('products/', views.ProductListView.as_view()),
	path('products/<int:pk>/', views.ProductDetailView.as_view()),

	path('items/', views.ItemListView.as_view()),
	path('items/<int:pk>/', views.ItemDetailView.as_view()),
]