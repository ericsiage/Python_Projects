from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

# Register your models here.

from .models import Categoria, Post

class categoriaAdmin(admin.ModelAdmin): 
    readonly_fields=('created','updated') #solo de lectura

class postAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Categoria,categoriaAdmin)
admin.site.register(Post,postAdmin)