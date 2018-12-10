from django.urls import path
from . import views

app_name = 'builder'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('search/result', views.result, name='result'),
    path('search/result/<str:card_id>', views.detail, name='detail'),
    path('search/result/add_to_deck/<str:card_id>', views.add_to_deck, name='add_to_deck'),
    path('search/result/create_deck/<str:card_id>', views.create_deck, name='create_deck'),

    path('decks/', views.decks, name='decks'),
    path('deck/<int:deck_id>', views.deck, name='deck'),

    path('search/result/create_deck_submit/<str:card_id>', views.create_deck_submit, name='create_deck_submit'),
    path('search/result/add_to_deck_submit/<str:card_id>', views.add_to_deck_submit, name='add_to_deck_submit'),

    #path('<int:player_id>/', views.player, name='player'),
]