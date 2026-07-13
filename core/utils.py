import requests
from django.conf import settings


def send_discord_notification(
    name,
    business,
    state,
    phone,
    email,
    message,
):
    phone_display = (
        f"[📞 Call {phone}](tel:{phone})"
        if phone
        else "Not provided"
    )

    data = {
        "embeds": [
            {
                "title": "📩 New Website Inquiry",
                "color": 12730636,
                "description": (
                    f"**👤 Name**\n"
                    f"{name or 'Not provided'}\n\n"

                    f"**🏢 Business**\n"
                    f"{business or 'Not provided'}\n\n"

                    f"**📍 State**\n"
                    f"{state or 'Not provided'}\n\n"

                    f"**📞 Phone**\n"
                    f"{phone_display}\n\n"

                    f"**📧 Email**\n"
                    f"{email or 'Not provided'}\n\n"

                    f"**💬 Project Details**\n"
                    f"{message or 'No message provided'}"
                ),
            }
        ]
    }

    try:
        response = requests.post(
            settings.DISCORD_WEBHOOK_URL,
            json=data,
            timeout=10,
        )
        response.raise_for_status()

    except requests.RequestException as error:
        print(f"Discord webhook failed: {error}")