from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Thing(models.Model):
    #Thing is essentially the user profile, that has a 1:1 relationship with
    #the django User model
    user = models.OneToOneField(User, blank=True, null=True)
    team = models.ForeignKey('Team', blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)


class Social(models.Model):
    #These are social accounts related to 'thing' (aka user profile)
    SOCIAL_TYPES = (
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('pinterest', 'Pinterest'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
    )
    network = models.CharField(max_length=255, choices=SOCIAL_TYPES)
    username = models.CharField(max_length=255)
    thing = models.ForeignKey(Thing, related_name="social_accounts")

    class Meta:
        #this changes the display name in the django admin
        verbose_name_plural = "Social media links"

class Team(models.Model):
    teammates = models.ManyToManyField(User, through='Thing')
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
