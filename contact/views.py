from django.core.mail import send_mail
from django.shortcuts import render

def contact_form(request):
    success = False

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            f"Sporočilo od {name}",
            message,
            email,
            ["random123@gmail.com"],
        )

        success = True

    return render(request, "contact.html", {"success": success})
