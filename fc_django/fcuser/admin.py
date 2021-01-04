from django.contrib import admin
from .models import Fcuser

# Register your models here.


class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email', )  # ,써야 튜플로 인식. ,안쓰면 문자열로 인식


admin.site.register(Fcuser, FcuserAdmin)
