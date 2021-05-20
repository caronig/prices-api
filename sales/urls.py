from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path('products/<int:pk>/', views.ProductView.as_view()),
    path('products/<int:productId>/prices', views.ProductPriceView.as_view()),
]