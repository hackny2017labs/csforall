# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from cs4all.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(User, UserAdmin)