from users.views import login_view, logout_view, register
from articles.views import add_post, edit_post, post, index
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("add/", add_post, name="add_post"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register, name="register"),
    path("post/<int:post_id>/", post, name="post"),
    path("post/<int:post_id>/edit/", edit_post, name="edit_post"),
]
