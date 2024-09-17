from django.db import models
from model_utils.models import TimeStampedModel
from applications.users.models import User

# Create your models here.

class Form(TimeStampedModel):
    Name = models.CharField('Nombre', max_length=50)
    active = models.CharField('Usuario', max_length=50)
    description = models.TextField(
        'descripcion del producto',
        blank=True,
    )

class Question(TimeStampedModel):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question_text = models.TextField()
    QUESTION_TYPES = [
        ('text', 'Text'),
        ('multiple_choice', 'Multiple Choice'),
    ]
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

class Response(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_text = models.TextField()
