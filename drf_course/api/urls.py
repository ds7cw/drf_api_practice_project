from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('products/', views.ProductListCreateAPIView.as_view()),
    path('products/info/', views.ProductInfoAPIView.as_view()),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view()),
    path('users/', views.UserListView.as_view()),
    # path('orders/', views.OrderListAPIView.as_view()), # replaced by views.OrderViewSet
    # path('user-orders/', views.UserOrderListAPIView.as_view(), name='user-orders'),
    path('index/', views.IndexPageTestView.as_view(), name="index"),
    path('products-test/', views.ProductTestListView.as_view(), name='products-test'),
]

router = DefaultRouter()
router.register('orders', views.OrderViewSet)
urlpatterns += router.urls
