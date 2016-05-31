from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth import models as model_user


class User(model_user.User):
    position_lat = models.DecimalField(decimal_places=8, max_digits=10, verbose_name="Широта")
    position_long = models.DecimalField(decimal_places=8, max_digits=10, verbose_name="Довгота")
    date_registration = models.DateTimeField(auto_now_add=True, verbose_name="Дата реєстрації")
    phone_regex = RegexValidator(regex=r'\+?380?\d{9}$',
                                 message="Номеру повинен бути виду +380000000000.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=13, verbose_name="Номер телефону")

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.username

    def get_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Place(models.Model):
    name = models.CharField(max_length=30, verbose_name="Назва")
    position_lat = models.DecimalField(decimal_places=8, max_digits=10, verbose_name="Широта")
    position_long = models.DecimalField(decimal_places=8, max_digits=10, verbose_name="Довгота")

    class Meta:
        verbose_name = 'Місце'
        verbose_name_plural = 'Місця'

    def __str__(self):
        return self.name


class Tracker(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Назва")
    description = models.TextField(max_length=500, verbose_name="Опис")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    date_of_delivery = models.DateTimeField(verbose_name="Необхідно виконати маршрут до:")
    user_id = models.ForeignKey(User, verbose_name="Користувач")
    place_id = models.ForeignKey(Place, verbose_name="Місце")

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршрути'

    def __str__(self):
        return self.name
