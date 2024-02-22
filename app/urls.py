from django.urls import path

from . import views

urlpatterns = [
  

    # ========{login/logout/registar}
    path('',views.regs,name='regs'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    # =========================================={profile the user}
    path('home',views.home,name='home'),
    
]
