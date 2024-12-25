from django.urls import path

from . import views # import views module

urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path("", views.home, name='home'),
    path("create/", views.create, name="create"),
]

# start