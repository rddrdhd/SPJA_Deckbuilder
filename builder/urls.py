from django.urls import path
from . import views

app_name = 'builder'
urlpatterns = [
    path('', views.builder, name='index'),
    path('search/', views.search, name='search'),
    path('search/result', views.result, name='result'),
    path('search/result/<str:id>', views.detail, name='detail'),

    #path('<int:multiverseid>/', views.card, name='card'),
    #path('<int:deck_id>/', views.deck, name='deck'),
    #path('<int:player_id>/', views.player, name='player'),
]