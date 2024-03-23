from django.urls import path
from .views import ProductListCreate, ProductRetrieveUpdateDestroy

urlpatterns = [
    path('api/products/', ProductListCreate.as_view()),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view()),
]
