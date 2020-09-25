from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('schools/', views.schoolListView.as_view(), name='schools'),
    path('schools/<int:pk>/', views.schoolDetailView.as_view(), name='school_detail'),
    path('create/', views.schoolCreateView.as_view(), name='school_create'),
    path('stu_create/<int:pk>', views.studentCreateView.as_view(), name='student_create'),
    path('update/<int:pk>/', views.schoolUpdateView.as_view(), name='school_update'),
    path('stu_update/<int:pk>/', views.studentUpdateView.as_view(), name='student_update'),
    path('delete/<int:pk>/', views.schoolDeleteView.as_view(), name='school_delete'),
    path('stu_delete/<int:pk>/', views.studentDeleteView.as_view(), name='student_delete'),
    path('delete_all/', views.school_delete_all, name='schools_delete'),
    path('stu_delete_all/', views.student_delete_all, name='students_delete'),
]
