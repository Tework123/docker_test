from django.db import models


class TimeSecond5(models.Model):
    time = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return f'{self.time}'


class Value9(models.Model):
    time = models.DateTimeField()

    def __str__(self):
        return f'{self.time}'
