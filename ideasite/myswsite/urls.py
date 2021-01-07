from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from myswsite.views import *

app_name = 'myswsite'

urlpatterns = [
    path("", idea_list, name="idea_list"),

    path("idea/<int:pk>/", idea_read, name="idea_read"),
    path("idea/create/", idea_create, name="idea_create"),
    path("idea/update/<int:pk>/", idea_update, name="idea_update"),
    path("idea/delete/<int:pk>/", idea_delete, name="idea_delete"),

    path("devtool/", devtool_list, name="devtool_list"),
    path("devtool/<int:pk>/", devtool_read, name="devtool_read"),
    path("devtool/create/", devtool_create, name="devtool_create"),
    path("devtool/update/<int:pk>/", devtool_update, name="devtool_update"),
    path("devtool/delete/<int:pk>/", devtool_delete, name="devtool_delete"),
]