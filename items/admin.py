from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(CPU)
admin.site.register(MB)
admin.site.register(Ram)
admin.site.register(Storage)
admin.site.register(GPU)
admin.site.register(PSU)