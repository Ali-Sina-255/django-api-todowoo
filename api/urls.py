from django.urls import path
from . import views

urlpatterns = [
    path('todo/',views.CreateTodoAPIView.as_view(),name='create'),
    path('todo/<int:pk>/',views.TodoUpdateDestroyAPIView.as_view(),name='updated'),
    path('todo/<int:pk>/complete/',views.TodoMarkCompleteAPI.as_view(),name='mark-complete'),
    path('todo/completed/', views.TodoCompletedList.as_view(), name='complete')
]
