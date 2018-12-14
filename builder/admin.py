from django.contrib import admin

from .models import Card, Deck, Comment

admin.site.register(Card)
admin.site.register(Deck)
admin.site.register(Comment)
