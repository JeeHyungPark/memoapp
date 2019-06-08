
from django.contrib import admin
from django.urls import path

import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.home, name="home"),
    path('blog/<int:blog_id>/', myapp.views.detail, name='detail'),
    path('new/', myapp.views.new, name='new'),
    path('creat', myapp.views.create, name='create'),
    path('blog/<int:blog_id>/delete/', myapp.views.delete, name='delete'),
    path('blog/<int:blog_id>/edit/', myapp.views.edit, name='edit'),
    path('blog/<int:blog_id>/update/', myapp.views.update, name='update'),
]
