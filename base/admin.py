from django.contrib import admin

from base.models import Case, CodeError, DiscordUser


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ("slug", "created_for", "created_at", "last_edited_at")
    readonly_fields = ("slug", "created_for", "created_at", "last_edited_at")
    list_filter = ("created_at", "last_edited_at", "created_for")
    search_fields = ("slug",)


@admin.register(CodeError)
class CodeErrorAdmin(admin.ModelAdmin):
    list_display = ("case", "message", "old_code_link", "fixed_code_link")
    search_fields = ("case__slug", "message")


@admin.register(DiscordUser)
class DiscordUserAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "last_known_name",
    )
