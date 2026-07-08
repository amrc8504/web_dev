import requests

from django.conf import settings


def send_discord_notification(name, business, phone, email, message):

    data = {
        "embeds": [
            {
                "title": "📩 New Website Inquiry",
                "color": 3066993,
                "fields": [
                    {
                        "name": "Name",
                        "value": name or "N/A",
                        "inline": True
                    },
                    {
                        "name": "Business",
                        "value": business or "N/A",
                        "inline": True
                    },
                    {
                        "name": "Phone",
                        "value": phone or "N/A",
                        "inline": False
                    },
                    {
                        "name": "Email",
                        "value": email,
                        "inline": False
                    },
                    {
                        "name": "Project",
                        "value": message,
                        "inline": False
                    }
                ]
            }
        ]
    }

    requests.post(settings.DISCORD_WEBHOOK_URL, json=data)