from django.contrib import admin
from .models import List,ListAllDefects,ListAllDefects1
import eav

# Register your models here.
admin.site.register(List)
admin.site.register(ListAllDefects)
admin.site.register(ListAllDefects1)

# eav.register(ListAllDefects)



 
