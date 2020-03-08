# from django.contrib import admin
# from django.urls import include,path
# urlspatterns=[
# ]
# from django.urls import path
#
#
# from . import views
#
# urlpatterns = [
#     path('xyz', views.index, name='index'),
#     path('home', views.show_details, name='nana'),
#     path('family', views.home, name='pavan'),
#     path('state', views.capitals, name='venu'),
#     path('details', views.company, name='ramesh'),
#     path('storage', views.institute, name='ganesh'),
#     path('popular', views.colleges, name='high'),
#     path('pavan/', views.show_details, name='college'),
#     path('amar/', views.college_details, name='pavan'),
#     path('lucky/', views.bank_details, name='ramesh'),
#     path('venu/', views.family_details, name='amma'),
# ]
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/detail', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

