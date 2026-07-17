import logging

from django.contrib import messages
from django.shortcuts import redirect, render

from .models import ContactRequest
from .utils import send_discord_notification


logger = logging.getLogger(__name__)


def home(request):
    if request.method == "POST":
        website = request.POST.get("website", "").strip()

        if website:
            messages.error(
                request,
                "Something went wrong. Please try again."
            )
            return redirect("/#contact")

        name = request.POST.get("name", "").strip()
        business = request.POST.get("business", "").strip()
        state = request.POST.get("state", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()
        legal_agreement = request.POST.get("legal_agreement")

        if not legal_agreement:
            messages.error(
                request,
                "You must accept the Privacy Policy and Terms of Service."
            )
            return redirect("/#contact")

        if not name or not state or not email or not message:
            messages.error(
                request,
                "Please complete all required fields."
            )
            return redirect("/#contact")

        lead = ContactRequest.objects.create(
            name=name,
            business=business,
            state=state,
            phone=phone,
            email=email,
            message=message,
            legal_agreement=True,
        )

        try:
            send_discord_notification(
                name,
                business,
                state,
                phone,
                email,
                message,
            )
        except Exception:
            logger.exception(
                "Discord notification failed for contact request %s",
                lead.pk,
            )

        messages.success(
            request,
            "Your request was sent successfully. "
            "I’ll get back to you within one business day."
        )

        return redirect("/#contact")

    return render(request, "core/home.html")


def privacy(request):
    return render(request, "core/privacy.html")


def terms(request):
    return render(request, "core/terms.html")