from django.contrib import admin

# Register your models here.
from .models import RegisteredPerson


@admin.register(RegisteredPerson)
class RegisteredPersonAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'father_name',
        'mobile',
        'gotra',
        'pur',
        'city',
        'district',
        'state',
        'created_at',
    )

    search_fields = (
        'full_name',
        'father_name',
        'mobile',
        'email',
        'gotra',
        'pur',
        'city',
        'district',
        'state',
    )

    list_filter = (
        'gender',
        'marital_status',
        'state',
        'district',
    )

    ordering = (
        '-created_at',
    )