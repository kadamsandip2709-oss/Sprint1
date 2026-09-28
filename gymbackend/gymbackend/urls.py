from django.contrib import admin
from django.urls import path

from gym import views


urlpatterns = [

    # =========================
    # ADMIN
    # =========================

    path("admin/", admin.site.urls),


    # =========================
    # AUTHENTICATION
    # =========================

    path("", views.login_view, name="login"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),


    # =========================
    # MAIN PAGES
    # =========================

    path("home/", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("nutrition/", views.nutrition, name="nutrition"),
    path("about/", views.about, name="about"),
    path("classes/", views.classes, name="classes"),
    path("contact/", views.contact, name="contact"),


    # =========================
    # FREE CLASS
    # =========================

    path(
        "apply-free-class/",
        views.apply_free_class,
        name="apply_free_class"
    ),


    # =========================
    # LOGOUT
    # =========================

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),
]