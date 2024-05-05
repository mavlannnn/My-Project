from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),

    path('brand/', BrandViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='brand_list'),
    path('brand/<int:pk>/', BrandViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='brand_detail'),


    path('watch/', WatchViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='watch_list'),
    path('watch/<int:pk>/', WatchViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='watch_detail'),


    path('customer/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='customer_list'),
    path('customer/<int:pk>/', CustomerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='customer_detail'),


    path('order', OrderViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='order_list'),
    path('order/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='order_detail'),


    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='rating_detail'),


    path('reviews', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='review_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='review_detail'),

    path('store', StoreViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='store_list'),
    path('store/<int:pk>/', StoreViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='store_detail'),

]

