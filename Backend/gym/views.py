from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password

from .models import Member, FreeClassApplication


# =========================
# REGISTER
# =========================

def register(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(request, "regitration.html", {
                "error": "Passwords do not match."
            })

        if Member.objects.filter(email=email).exists():
            return render(request, "regitration.html", {
                "error": "Email already registered."
            })

        Member.objects.create(
            full_name=full_name,
            email=email,
            password=make_password(password)
        )

        return redirect("login")

    return render(request, "regitration.html")


# =========================
# LOGIN
# =========================

def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:

            member = Member.objects.get(email=email)

            if check_password(password, member.password):

                request.session["member_id"] = member.id
                request.session["member_name"] = member.full_name
                request.session["member_email"] = member.email

                # LOGIN SUCCESS → HOME
                return redirect("home")

            else:

                return render(request, "login.html", {
                    "error": "Invalid email or password."
                })

        except Member.DoesNotExist:

            return render(request, "login.html", {
                "error": "Invalid email or password."
            })

    return render(request, "login.html")


# =========================
# HOME
# =========================

def home(request):

    # User must login first
    if not request.session.get("member_id"):
        return redirect("login")

    return render(request, "Project.html")


# =========================
# DASHBOARD
# =========================

def dashboard(request):

    member_email = request.session.get("member_email")

    if not member_email:
        return redirect("login")

    applications = FreeClassApplication.objects.filter(
        email=member_email
    ).order_by("-id")

    context = {
        "applications": applications,
        "member_name": request.session.get("member_name"),
    }

    return render(request, "dashboard.html", context)


# =========================
# APPLY FREE CLASS
# =========================

def apply_free_class(request):

    if not request.session.get("member_id"):
        return redirect("login")

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        selected_class = request.POST.get("selected_class")

        FreeClassApplication.objects.create(
            name=name,
            email=email,
            phone=phone,
            selected_class=selected_class
        )

        return redirect("dashboard")

    return redirect("dashboard")


# =========================
# NUTRITION
# =========================

def nutrition(request):

    if not request.session.get("member_id"):
        return redirect("login")

    return render(request, "nutrition.html")

# =========================
# ABOUT
# =========================

def about(request):
    return render(request, "about.html")


# =========================
# CLASSES
# =========================

def classes(request):

    if not request.session.get("member_id"):
        return redirect("login")

    return render(request, "classes.html")


# =========================
# CONTACT
# =========================

def contact(request):

    if not request.session.get("member_id"):
        return redirect("login")

    return render(request, "contact.html")


# =========================
# LOGOUT
# =========================

def logout_view(request):

    request.session.flush()

    return redirect("login")