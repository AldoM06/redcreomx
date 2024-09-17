from django.contrib import admin

from .models import Classroom,Session,Result

# Register your models here.
admin.site.register(Classroom)
admin.site.register(Session)
admin.site.register(Result)
