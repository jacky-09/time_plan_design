# 引入redirect重定向模块
from django.shortcuts import render, redirect
# 引入HttpResponse
from django.http import HttpResponse
# 引入刚才定义的ArticlePostForm表单类
from .forms import TimeplanForm, TemplateForm
# 引入User模型
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# 导入数据模型ArticlePost
from .models import Timeplan, Template
import datetime
from django.utils import timezone

@login_required(login_url='/userprofile/login/')
def workshop(request):
    # 取出所有博客文章
    timeplans = Timeplan.objects.filter(author=request.user)
    templates = Template.objects.filter(author=request.user)
    # 需要传递给模板（templates）的对象
    context = { 'timeplans': timeplans, 'templates': templates }
    # render函数：载入模板，并返回context对象
    return render(request, 'timeplan/workshop.html', context)

def work_detail(request, id):
    # 取出相应的文章
    timeplan = Timeplan.objects.get(id=id)
    # 需要传递给模板的对象
    context = { 'timeplan': timeplan }
    # 载入模板，并返回context对象
    return render(request, 'timeplan/detail.html', context)

@login_required(login_url='/userprofile/login/')
def work_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        timeplan_form = TimeplanForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if timeplan_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_timeplan = timeplan_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_timeplan.author = User.objects.get(id=request.user.id)
            # 将新文章保存到数据库中
            new_timeplan.save()
            # 完成后返回到文章列表
            return redirect("timeplan:workshop")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        timeplan_form = TimeplanForm()
        # 赋值上下文
        context = { 'timeplan_form': timeplan_form }
        # 返回模板
        return render(request, 'timeplan/create.html', context)

@login_required(login_url='/userprofile/login/')
def work_finish(request, id):
    # 取出所有博客文章
    timeplan = Timeplan.objects.get(id=id)
    timeplan.complete = True
    timeplan.finish = timezone.now()
    finish = timezone.now()
    finish = int(finish.strftime("%Y%m%d%H%M"))
    start = Timeplan.objects.get(id=id).start
    start = int(start.strftime("%Y%m%d%H%M"))
    timeplan.time = finish - start
    timeplan.save()
    # render函数：载入模板，并返回context对象
    return redirect("timeplan:workshop")

@login_required(login_url='/userprofile/login/')
def work_report(request, id):
    # 取出所有博客文章
    timeplan = Timeplan.objects.get(id=id)
    time = Timeplan.objects.get(id=id).time
    differ = Timeplan.objects.get(id=id).differ
    num = Timeplan.objects.get(id=id).num
    result = 2 * num * differ / time
    timeplan.result = result
    if result >= 4:
        timeplan.gb4 = "优秀"
    if result >= 2.5 and result < 4:
        timeplan.gb4 = "良好"
    if result >= 0.7 and result < 2.5:
        timeplan.gb4 = "合格"
    if result < 0.7:
        timeplan.gb4 = "不合格"
    timeplan.save()
    # 赋值上下文
    context = { 'timeplan': timeplan }
    # 返回模板
    return render(request, 'timeplan/report.html', context)

@login_required(login_url='/userprofile/login/')
def t_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        template_form = TemplateForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if template_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_template = template_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_template.author = User.objects.get(id=request.user.id)
            # 将新文章保存到数据库中
            new_template.save()
            # 完成后返回到文章列表
            return redirect("timeplan:workshop")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        template_form = TemplateForm()
        # 赋值上下文
        context = { 'template_form': template_form }
        # 返回模板
        return render(request, 'timeplan/tcreate.html', context)

@login_required(login_url='/userprofile/login/')
def t_work_create(request, id):
    templates = Template.objects.get(id=id)
    obj = Timeplan()
    obj.author = User.objects.get(id=request.user.id)
    obj.title = templates.ttitle
    obj.describe = templates.tdescribe
    obj.differ = templates.tdiffer
    obj.num = templates.tnum
    obj.start = timezone.now()
    obj.save()
    context = { 'template': templates }
    return redirect("timeplan:workshop")

@login_required(login_url='/userprofile/login/')
def t_delete(request, id):
    # 根据 id 获取需要删除的文章
    template = Template.objects.get(id=id)
    # 调用.delete()方法删除文章
    template.delete()
    # 完成删除后返回文章列表
    return redirect("timeplan:workshop")