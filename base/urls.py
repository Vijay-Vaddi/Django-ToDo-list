from django.urls import path, include
from .views import TaskList, TaskDetail, \
    TaskCreate, TaskUpdate, TaskDelete, UserLoginView, RegisterUser
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
    path("api/",include("base.api.urls")),
]