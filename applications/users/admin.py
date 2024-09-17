from django.contrib import admin
from .models import State,Municipality,School,User,Platform,SocialMedia

# Register your models here.

admin.site.register(State)

admin.site.register(Municipality)

admin.site.register(School)

admin.site.register(User)

admin.site.register(Platform)

admin.site.register(SocialMedia)
