from django.urls import include, path
from .import views

app_name = "reciepes"
urlpatterns = [

    path("", views.index, name="index"),
    path("<int:id>", views.detail, name="detail"),
    # path("<int:id>",views.create,name="create")

]