# 引入表单类
from django import forms
# 引入文章模型
from .models import Timeplan,Template

# 写文章的表单类
class TimeplanForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = Timeplan
        # 定义表单包含的字段
        fields = ('title', 'describe', 'differ', 'num', 'start')

# 写文章的表单类
class TemplateForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = Template
        # 定义表单包含的字段
        fields = ('ttitle', 'tdescribe', 'tdiffer', 'tnum')