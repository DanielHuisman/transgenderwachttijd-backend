import graphene
from graphene_django import DjangoObjectType

from . import models


class Provider(DjangoObjectType):
    class Meta:
        model = models.Provider

    def resolve_locations(self: models.Provider, _info):
        return self.locations.order_by('name').all()


class Location(DjangoObjectType):
    class Meta:
        model = models.Location


class Query(graphene.ObjectType):
    provider = graphene.Field(Provider, id=graphene.UUID())
    providers = graphene.NonNull(graphene.List(graphene.NonNull(Provider)))

    location = graphene.Field(Location, id=graphene.UUID())
    locations = graphene.NonNull(graphene.List(graphene.NonNull(Location)))

    def resolve_provider(self, _info, **kwargs):
        return models.Provider.objects.get(id=kwargs['id'])

    def resolve_providers(self, _info):
        return models.Provider.objects.order_by('name').all()

    def resolve_location(self, _info, **kwargs):
        return models.Location.objects.get(id=kwargs['id'])

    def resolve_locations(self, _info):
        return models.Location.objects.order_by('name').all()
