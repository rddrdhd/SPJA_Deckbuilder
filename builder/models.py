from django.contrib.auth.models import User
from django.db import models


class Deck(models.Model):
    deck_name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_cards(self):
        return Card.objects.filter(deck=self)

    def get_comments(self):
        return Comment.objects.filter(to_deck=self)

    def __str__(self):
        return self.deck_name


class Card(models.Model):
    card_id = models.CharField(max_length=100)
    name = models.CharField(max_length=150)  # string
    manaCost = models.CharField(max_length=100, null=True)
    colors = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=30)
    cmc = models.IntegerField()  # int - converted mana cost
    rarity = models.CharField(max_length=20)
    text = models.CharField(max_length=1000, null=True)
    flavor = models.CharField(max_length=1000, null=True)
    imgUrl = models.CharField(max_length=1000)
    artist = models.CharField(max_length=100)
    number = models.IntegerField(null=True)  # Some cards dont have number???
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, {%s}' % (self.name, self.cmc)


class Comment(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    to_deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.title, self.text)
