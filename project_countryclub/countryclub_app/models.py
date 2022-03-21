from django.db import models
from django_countries.fields import CountryField


# Create your models here.

class ClubModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Club(ClubModel):
    city = models.CharField(null=False, blank=False, max_length=128)
    address = models.CharField(null=False, blank=False, max_length=512)
    country = CountryField()

    class Meta:
        db_table = "clubs"

    def __str__(self):
        return f"{self.address} {self.city}"


class ClubMembers(ClubModel):
    passport_num = models.CharField(null=False, blank=False, max_length=128, unique=True)
    first_name = models.CharField(null=False, blank=False, max_length=128)
    last_name = models.CharField(null=False, blank=False, max_length=128)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(null=False, blank=False, max_length=128)
    address = models.CharField(null=False, blank=False, max_length=512)
    country = CountryField()
    email = models.EmailField(max_length=128)

    class Meta:
        db_table = "club_members"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ClubEvents(ClubModel):
    title = models.CharField(null=False, blank=False)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    trainer = models.ForeignKey(ClubMembers)

    class Meta:
        db_table = "club_events"

    def __str__(self):
        return f"{self.title} {self.date} {self.time}"

# TODO: Complete the ClubEvents Model with more values and add Generic ViewSets in views.py
