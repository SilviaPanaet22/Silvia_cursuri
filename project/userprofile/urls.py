
from django.urls import path
from userprofile import views
app_name = "userprofile"


urlpatterns=[
    path('new_account', views.CreateNewAccountView.as_view(), name='utilizator_nou'),
]