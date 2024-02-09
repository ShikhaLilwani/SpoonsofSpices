from django.contrib import admin
from recipe.models import RecipeTable
# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display=['id','name','details','category','is_active','rating']
admin.site.register(RecipeTable,RecipeAdmin)