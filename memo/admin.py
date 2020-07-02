from django.contrib import admin

# 别忘了导入ArticlerPost
from .models import Memo

# 注册ArticlePost到admin中
admin.site.register(Memo)