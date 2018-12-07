from tastypie.resources import ModelResource
from .models import Card


class CardResource(ModelResource):
    class Meta:
        queryset = Card.objects.all()
        resource_name = 'card'
