from django.contrib import admin

from .models import ContactRequest


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "business",
        "state",
        "email",
        "submitted_at",
        "contacted",
    )

    list_filter = (
        "contacted",
        "state",
        "submitted_at",
    )

    search_fields = (
        "name",
        "business",
        "email",
        "phone",
        "message",
    )

    readonly_fields = (
        "name",
        "business",
        "state",
        "phone",
        "email",
        "message",
        "legal_agreement",
        "submitted_at",
    )

    fieldsets = (
        (
            "Lead Information",
            {
                "fields": (
                    "name",
                    "business",
                    "state",
                    "phone",
                    "email",
                    "message",
                    "legal_agreement",
                    "submitted_at",
                )
            },
        ),
        (
            "Follow-Up",
            {
                "fields": (
                    "contacted",
                    "notes",
                )
            },
        ),
    )