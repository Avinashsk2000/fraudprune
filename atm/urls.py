from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("register_account", views.register_account, name="register_account"),
    path("withdraw", views.withdraw, name="withgraw"),
    path("bank", views.bank, name="bank"),
    path("logout", views.logout, name="logout"),
    path("check_balance",views.check_balance, name="check_balance"),
    path("set",views.set,name="set"),

]
