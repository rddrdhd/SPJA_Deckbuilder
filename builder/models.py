from django.db import models

"""
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    registered_at = models.DateTimeField(auto_now_add=True) #when creating player

    def __str__(self):
        return '%s, %s' % (self.username, self.email)

"""

class Deck(models.Model):
    deck_name = models.CharField(max_length=50) #string
    deck_player = models.ForeignKey(User, on_delete=models.CASCADE) # Who is the owner of deck?

    def __str__(self):

        return '%s, %s' % (self.deck_name, self.deck_player)


class Card(models.Model):
    #card_number = models.CharField() #string
    name = models.CharField(max_length=150) #string
    cmc = models.IntegerField() #int - converted mana cost
    rarity = models.CharField(max_length=20) #string
    text = models.CharField(max_length=1000) #string
    card_deck = models.ForeignKey(Deck, on_delete=models.DO_NOTHING) # Is the card in some deck?
    """
    COMMON = 'CO'
    UNCOMMON = 'UC'
    RARE = 'RA'
    MYTHIC_RARE = 'MR'
    SPECIAL = 'SP'
    BASIC_LAND = 'BL'
    RARITY_CHOICES=(
        (COMMON, 'common'),
        (UNCOMMON, 'uncommon'),
        (RARE, 'common'),
        (MYTHIC_RARE, 'common'),
        (SPECIAL, 'common'),
        (BASIC_LAND, 'common'),
    )
    """
    def __str__(self):
        return '%s, %s' % (self.name, self.cmc)
