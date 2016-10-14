from django.db import models
from tracker.models import User, Tracker


# Create your models here.

class Call(models.Model):
    user_id = models.ForeignKey(User, verbose_name="Користувач")
    track_id = models.ForeignKey(Tracker, verbose_name="Марштрут")
    is_called = models.BooleanField(default=False, verbose_name="Вже зателефоновано")

    def __str__(self):
        return '{0}: Маршрут - {1}, номер телефону {2}'.format(self.user_id.get_name(), self.track_id,
                                                               self.user_id.phone_number)

