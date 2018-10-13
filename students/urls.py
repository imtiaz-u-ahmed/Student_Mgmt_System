"""stdMgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
# from .views import StudentsInfoList
from students import views

urlpatterns = [
    # path('dlist/',StudentsInfoList, name="students-info-list")
    path('list/',views.StudentsInfoListVW, name="students-info-list"),
    path('dtls/<int:student_roll>',views.StudentsInfoDetailsVW, name="students-info-dtls"),
    path('glist/',views.GuardianInfoListVW, name="guardians-info-list"),
    path('gdtls/<phone_no>',views.GuardianInfoDtlsVW, name="guardians-info-dtls")
]
