from django.db import models


"""
class Player(models.Model):
    login = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    registered_at = models.DateTimeField(auto_now_add=True) #when creating player

    def __str__(self):
        return '%s, %s' % (self.login, self.email)

"""


class Card(models.Model):
    card_id = models.CharField(max_length=100, null = True)
    name = models.CharField(max_length=150, null = True) #string
    cmc = models.IntegerField() #int - converted mana cost
    rarity = models.CharField(max_length=20) #string
    text = models.CharField(max_length=1000, null = True) #string
    imgUrl = models.CharField(max_length=1000)

    def __str__(self):
        return '%s, {%s}' % (self.name, self.cmc)


class Deck(models.Model):
    deck_name = models.CharField(max_length=50) #string
    cards = models.ManyToManyField(Card)

    def __str__(self):

        return self.deck_name

