from django.db import models

from model_utils.models import TimeStampedModel


from .managers import UserManager

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# EMPIEZA MODELOS PARA ASIGNAR ESCUELA A LOS ALUMNOS (A).
class State(TimeStampedModel):
    Name = models.CharField('Nombres', max_length=150,blank=False,)
    active = models.BooleanField(default=False)

class Municipality(TimeStampedModel):
    Name = models.CharField('Nombres', max_length=150,blank=False,)
    State = models.ForeignKey(
        State,
        on_delete=models.PROTECT,
        verbose_name='Estado',
    )
    CP = models.PositiveIntegerField(
        'Codigo postal',
        default=0,
        blank=False,
    )
    active = models.BooleanField(default=False)

class School(TimeStampedModel):
    Name = models.CharField('Nombres', max_length=150,blank=False,)
    Address = models.CharField('Direccion', max_length=150)
    CP = models.PositiveIntegerField(
        'Codigo postal',
        default=0,
        blank=False,
    )
    Municipality = models.ForeignKey(
        Municipality,
        on_delete=models.PROTECT,
        verbose_name='Municipio',
    )
    latitud = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    active = models.BooleanField(default=False)
#TERMINA ASIGNACION DE ESCUELA (A)

#INICIA DATOS DE REDES SOCIALES (B)
class Platform(TimeStampedModel):
    Name = models.CharField('Nombre', max_length=50)
    URL = models.CharField('Usuario', max_length=50)
    description = models.TextField(
        'descripcion del producto',
        blank=True,
    )

class SocialMedia(TimeStampedModel):
    Plataforma = models.ForeignKey(
        Platform,
        on_delete=models.PROTECT,
        verbose_name='Plataforma',
    )
    Name = models.CharField('Nombre', max_length=50)
    User = models.CharField('Usuario', max_length=50)
    active = models.BooleanField(default=False)
#TERMINA DATOS DE REDES SOCIALES (B)

class User(AbstractBaseUser,PermissionsMixin ):
    # TIPO DE USUARIOS
    ADMINISTRADOR = '0'
    DIRECTOR = '1'
    SUPERVISOR = '2'
    PROFESOR = '3'
    ASESOR = '4'
    ALUMNO = '5'
    TUTOR = '6'


    # GENEROS
    VARON = 'M'
    MUJER = 'F'
    OTRO = 'O'
    #
    OCUPATION_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (DIRECTOR, 'Director'),
        (SUPERVISOR, 'Supervisor'),
        (PROFESOR, 'Profesor'),
        (ASESOR , 'Asesor'),
        (ALUMNO , 'Alumno'),
        (TUTOR , 'Tutor'),

    ]

    GENDER_CHOICES = [
        (VARON, 'Masculino'),
        (MUJER, 'Femenino'),
        (OTRO, 'Otros'),
    ]
    username = models.CharField('Nombres', max_length=10, unique = True)
    email = models.EmailField(unique=True)
    Name = models.CharField('Nombres', max_length=35,blank=True)
    LastName = models.CharField('Apellido P', max_length=35,blank=True)
    MiddleName = models.CharField('Apellido M', max_length=35,blank=True)
    Curp = models.CharField('CURP', max_length=18,blank=True)

    ocupation = models.CharField(
        max_length=1,
        choices=OCUPATION_CHOICES,
        blank=True
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True
    )
    #
    School = models.ForeignKey(
        School,
        on_delete=models.PROTECT,
        verbose_name='Escuela',
        null=True,
        blank=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    objects = UserManager()


    REQUIRED_FIELDS = ['username']

#    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.Name + ' '+ self.LastName

#TABLAS AUXILIARES

class User_Social(TimeStampedModel):
    user_id = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Usuario',
    )
    SocialMedia_id = models.ForeignKey(
        SocialMedia,
        on_delete=models.PROTECT,
        verbose_name='Redes',
    )
