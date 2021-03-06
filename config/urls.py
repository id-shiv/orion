from dj_rest_auth.registration.views import ConfirmEmailView, VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("dj_rest_auth.urls")),
    path(
        "api/v1/registration/account-confirm-email/<str:key>/",
        ConfirmEmailView.as_view(),
    ),
    path("api/v1/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "api/v1/account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    path(
        "api/v1/password/reset/confirm/<slug:uidb64>/<slug:token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]

admin.site.site_header = "ORION Admin"
admin.site.site_title = "ORION Admin Portal"
admin.site.index_title = "ORION Admin Portal"
