from django.contrib import admin
from .models import Person
from .models import Members
from .models import Blog

# Register your models here. 
admin.site.register(Person) 
admin.site.register(Members)
class Admin(admin.ModelAdmin):
    list_display=('title','content')
admin.site.register(Blog,Admin)
    

