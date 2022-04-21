from django.urls import path

from classroom_app import views
from classroom_app.views import student_register

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('student_home/',views.student_home,name='student_home'),
    path('student_register/',views.student_register,name='student_register'),
    path('complaint_add/',views.complaint_add,name='complaint_add'),
    path('complaint_view/',views.complaint_view,name='complaint_view'),
    path('notification_add/', views.notification_add, name='notification_add'),
    path('notification_view/', views.notification_view, name='notification_view'),
    path('student_reg_view/',views.student_reg_view,name='student_reg_view'),
    path('update_view/<int:id>/',views.update_view,name='update_view'),
    path('delete_view/<int:id>/',views.delete_view,name='delete_view')
]