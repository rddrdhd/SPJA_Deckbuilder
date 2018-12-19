from django.urls import path
from . import views

app_name = 'builder'
urlpatterns = [
    path('', views.index, name='index'),

    path('signup/', views.SignUp.as_view(), name='signup'),

    path('search/', views.search, name='search'),  # search field
    path('search/result/', views.result, name='result'),  # results of searching
    path('search/result/<str:card_id>/', views.detail, name='detail'),  # detail of card

    path('players/', views.players, name='players'),  # all players
    path('player/<int:player_id>/', views.player, name='player'),  # detail of player

    path('decks/', views.decks, name='decks'),  # all decks
    path('deck/<int:deck_id>/', views.deck, name='deck'),  # detail of deck

    path('create_deck/<str:card_id>/', views.create_deck, name='create_deck'),
    path('create_deck_submit/<str:card_id>/', views.create_deck_submit, name='create_deck_submit'),
    path('add_to_deck/<str:card_id>/', views.add_to_deck, name='add_to_deck'),
    path('add_to_deck_submit/<str:card_id>/', views.add_to_deck_submit, name='add_to_deck_submit'),

    path('delete_card/<int:id>/', views.delete_card, name='delete_card'),
    path('delete_deck/<int:id>/', views.delete_deck, name='delete_deck'),

    path('new_comment/<int:deck_id>/', views.new_comment, name='new_comment'),
    path('new_comment_submit/<int:deck_id>/', views.new_comment_submit, name='new_comment_submit'),

]
