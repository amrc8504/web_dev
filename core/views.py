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

        send_discord_notification(
            name,
            business,
            state,
            phone,
            email,
            message,
        )

        messages.success(request, "Your request was sent successfully. I’ll get back to you within one business day.")
        return redirect("home")

    return render(request, "core/home.html")