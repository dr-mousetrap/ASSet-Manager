from django.contrib import admin
from .models import teacher
from .models import assets
# Register your models here.

class teacherAdmin(admin.ModelAdmin):
    list_display = ("Names", "Area",)

class assetsAdmin(admin.ModelAdmin):
    list_display = ("type", "teacher",)


admin.site.register(teacher, teacherAdmin)
admin.site.register(assets, assetsAdmin)