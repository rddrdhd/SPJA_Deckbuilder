from django.db import models


"""
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    registered_at = models.DateTimeField(auto_now_add=True) #when creating player

    def __str__(self):
        return '%s, %s' % (self.username, self.email)

"""


class Card(models.Model):
    #id = models.CharField(max_length=100)
    name = models.CharField(max_length=150) #string
    cmc = models.IntegerField() #int - converted mana cost
    rarity = models.CharField(max_length=20) #string
    text = models.CharField(max_length=1000) #string
    imgUrl = models.CharField(max_length=1000)


class Deck(models.Model):
    deck_name = models.CharField(max_length=50) #string
    cards = models.ManyToManyField(Card)

    def __str__(self):

        return self.deck_name




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
