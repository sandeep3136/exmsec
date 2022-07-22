from unicodedata import name
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('rem/', views.remuneration, name='remuneration'),
    path('bill<int:id>/', views.bill, name='bill'),
    path('genrl<int:id>', views.genRL, name='genRL'),
    path('report', views.consReport, name='report'),
    path('genbill<int:id>', views.genbill, name='genbill'),
    path('report_txt <int:bid>', views.report_txt, name='report_txt')

]
