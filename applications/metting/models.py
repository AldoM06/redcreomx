from django.db import models
from applications.users.models import User
from model_utils.models import TimeStampedModel

# Create your models here.
class Classroom(TimeStampedModel):
    Name = models.CharField('Nombre', max_length=50)
    active = models.BooleanField(default=False)

class Session(TimeStampedModel):
    student = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Alumno',
        related_name = 'alumno_sesion',

    )
    coach = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    room = models.ForeignKey(
        Classroom,
        on_delete=models.PROTECT,
        verbose_name='Salon',
    )
    time = models.DateTimeField()
    active = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)


class Result(TimeStampedModel):
    session = models.ForeignKey(
        Session,
        on_delete=models.PROTECT,
        verbose_name='Sesion',

    )
    objective = models.TextField(
        'Objetico de la sesion',
        blank=True,
    )
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='media/')
    active = models.BooleanField(default=False)
