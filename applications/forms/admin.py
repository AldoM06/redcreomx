from django.contrib import admin
from .models import Form,Question,Response

# Register your models here.
admin.site.register(Question)
admin.site.register(Form)
admin.site.register(Response)
