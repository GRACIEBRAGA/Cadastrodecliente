from django.urls import path

from store import views


app_name = 'store'


urlpatterns = [

    path('', views.Clientelist.as_view(), name='clientelist'),
    path('create/', views.ClienteCreate.as_view(), name='clientecreate'),
    path('homepage/', views.Homepage.as_view(), name='homepage'),
    path('homestore/', views.Homestore.as_view(), name='homestore'),
    path('estoque/', views.Estoquecreate.as_view(), name='estoquecreate'),
    path('estoquelist', views.Estoquelist.as_view(), name='estoquelist'),
    path('venda/', views.Vendacreate.as_view(), name='vendacreate'),
    path('vendalist', views.Vendalist.as_view(), name='vendalist'),

]