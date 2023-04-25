from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Organization)
admin.site.register(Survey)
admin.site.register(Topic)
admin.site.register(Question)