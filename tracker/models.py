from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    position_lat = models.DecimalField(decimal_places=8, max_digits=10)
    position_long = models.DecimalField(decimal_places=8, max_digits=10)
    date_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def get_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Place(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    position_lat = models.DecimalField(decimal_places=8, max_digits=10)
    position_long = models.DecimalField(decimal_places=8, max_digits=10)

    def __str__(self):
        return self.name


class Tracker(models.Model):
    name = models.CharField(max_length=30, unique=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_of_delivery = models.DateTimeField()
    user_id = models.ForeignKey(User)
    place_id = models.ForeignKey(Place)

    def __str__(self):
        return self.name
