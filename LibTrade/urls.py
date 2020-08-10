"""LibTrade URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from LibTrade import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.Landing.as_view(), name = 'landing'),
    path('home/', views.Home.as_view(), name='home' ),

    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('exists/', views.EmailExistsView.as_view(), name="emailexists"),

    path('activate/<uidb64>/<token>', views.VerificationView.as_view(), name='activate'),

    path('user/<slug:slug>', views.UserDetailView.as_view(), name = 'userdetail'),
    path('book/', include('accounts.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
