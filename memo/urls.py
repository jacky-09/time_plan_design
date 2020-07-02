from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'memo'

urlpatterns = [
    path('list/', views.memo_list, name='list'),
    path('detail/<int:id>/', views.memo_detail, name='detail'),
    path('delete/<int:id>/', views.memo_delete, name='delete'),
    path('create/', views.memo_create, name='create'),
]