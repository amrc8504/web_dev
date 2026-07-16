from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import send_discord_notification

def home(request):
    if request.method == "POST":

        website = request.POST.get("website")

        if website:
            messages.error(request, "Something went wrong. Please try again.")
            return redirect("home")

        name = request.POST.get("name")
        business = request.POST.get("business")
        state = request.POST.get("state")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")
        legal_agreement = request.POST.get("legal_agreement")

        if not legal_agreement:
            messages.error(
                request,
                "You must accept the Privacy Policy and Terms of Service."
            )
            return redirect("/#contact")

        send_discord_notification(
            name,
            business,
            state,
            phone,
            email,
            message,
        )

        messages.success(request, "Your request was sent successfully. I’ll get back to you within one business day.")
        return redirect("/#contact")

    return render(request, "core/home.html")

def privacy(request):
    return render(request, "core/privacy.html")

def terms(request):
    return render(request, "core/terms.html")