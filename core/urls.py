"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App1.views import HomepageView,AboutView,NewPostView,DetailPostView,RegisterView,LoginView,LogoutView,DraftsView,MyWorkView,PostUpdateView,BlogpublishView,DeletePostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomepageView, name='home'),
    path('about/',AboutView,name='about'),
    path('newpost/',NewPostView,name='newpost'),
    path('postdetail/<pk>/',DetailPostView,name='detailpost'),
    path('accounts/register/',RegisterView,name='register'),
    path('accounts/login/',LoginView,name='login'),
    path('accounts/logout/',LogoutView,name='logout'),
    path('drafts/',DraftsView,name='drafts'),
    path('edit/<pk>/',PostUpdateView,name='edit'),
    path('publish/<pk>/',BlogpublishView,name='publish'),
    path('delete/<pk>/',DeletePostView,name='delete'),
    path('mywork/',MyWorkView,name='mywork'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)