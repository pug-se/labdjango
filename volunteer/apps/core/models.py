from django.db import models


class DefaultFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Profile(DefaultFields):
    user = models.OneToOneField('auth.User', related_name='profile')
    birth_date = models.DateField()


class Organization(DefaultFields):
    # required
    owner = models.ForeignKey('auth.User', related_name='organizations')
    name = models.CharField(max_length=100)
    description = models.TextField()
    # optional
    site = models.URLField(null=True, blank=True)
    cnpj = models.CharField(max_length=14, null=True, blank=True)


class Opportunity(DefaultFields):
    # relation
    organization = models.ForeignKey('Organization', related_name='opportunities')
    volunteers = models.ManyToManyField('auth.User', related_name='opportunities', through='Collaboration')
    # required
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    # optional
    min_volunteer = models.IntegerField(null=True, blank=True)
    max_volunteer = models.IntegerField(null=True, blank=True)
    site = models.URLField()


class Collaboration(DefaultFields):
    opportunity = models.ForeignKey('Opportunity', related_name='collaborations')
    user = models.ForeignKey('auth.User', related_name='collaborations')
    confirmed = models.BooleanField()

    class Meta:
        unique_together = ('opportunity', 'user')
