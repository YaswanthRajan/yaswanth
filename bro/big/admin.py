from django.contrib import admin
from .models import show, kim, bob, one


# Register your models here.

class showadmin(admin.ModelAdmin):
    model = 'show'
    list_display = ['name', 'age', 'add']
    list_editable = ('age', 'add',)
    list_filter = ('add',)


admin.site.register(show, showadmin)


class showadmin(admin.ModelAdmin):
    model = 'bob'
    list_display = ['name', 'des']
    list_editable = ('des',)


admin.site.register(bob, showadmin)


class showadmin(admin.ModelAdmin):
    model = 'one'
    list_display = ['image', 'des']
    list_editable = ('des',)


admin.site.register(one, showadmin)
