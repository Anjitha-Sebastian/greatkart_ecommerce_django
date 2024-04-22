from django.urls import path
from .import views


urlpatterns = [
    path('',views.storeview,name='store'),
    path('category/<slug:category_slug>/', views.storeview, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.product_detail, name='products_detail'),
    path('search/',views.search,name='search')
]
