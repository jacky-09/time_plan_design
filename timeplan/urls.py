from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'timeplan'

urlpatterns = [
    path('work/', views.workshop, name='workshop'),
    path('work-detail/<int:id>/', views.work_detail, name='detail'),
    path('create/', views.work_create, name='create'),
    path('finish/<int:id>/', views.work_finish, name='finish'),
    path('report/<int:id>/', views.work_report, name='report'),
    path('template-create/', views.t_create, name='tcreate'),
    path('template-work-create/<int:id>/', views.t_work_create, name='twc'),
    path('template-delete/<int:id>/', views.t_delete, name='tdelete'),
]