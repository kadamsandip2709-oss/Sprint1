from django.contrib import admin

from .models import Member, FreeClassApplication


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "full_name",
        "email",
    )


@admin.register(FreeClassApplication)
class FreeClassApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "selected_class",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "selected_class",
    )