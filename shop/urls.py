from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:c_slug>/', views.home, name='prod_cat'),
    # path('details', views.prod_detail, name='prod_detail'),
    path('<slug:c_slug>/<slug:prod_slug>/', views.prod_detail, name='prod_detail'),
    path('search', views.searching, name='search'),

]
