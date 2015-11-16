#-*- coding: UTF-8 -*-
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from models import User

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    passworld = forms.CharField(label='密 码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮 件')
    name = forms.CharField(label='姓 名',max_length=100)
    num = forms.CharField(label='学 号',max_length=100)
    major = forms.CharField(label='学 院',max_length=100)

class LogForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    passworld = forms.CharField(label='密 码',widget=forms.PasswordInput())
    
class PersonForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    passworld = forms.CharField(label='原密码',widget=forms.PasswordInput())
    newpass = forms.CharField(label='新密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮 件')
    name = forms.CharField(label='姓 名',max_length=100)
    num = forms.CharField(label='学 号',max_length=100)
    major = forms.CharField(label='学 院',max_length=100)
    
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
        #获取表单信息
            usernames = uf.cleaned_data['username']
            passworlds = uf.cleaned_data['passworld']
            emails = uf.cleaned_data['email']
            names = uf.cleaned_data['name']
            nums = uf.cleaned_data['num']
            majors = uf.cleaned_data['major']
            #将表单写入数据库
            user = User(
            username = usernames,
            password = passworlds,
            email = emails,
            name = names,
            num = nums,
            major = majors
            )
            #user.passworld.create(password=passworlds)
            user.save()
            a1 = 1
            a2 = 2
            a3 = 3
            a4 = 4
            #返回注册成功页面
            return render_to_response('select.html',locals())
    else:
        uf = UserForm()
        return render_to_response('register.html',{'uf':uf})

def login(request):
    if request.method == "POST":
        uf = LogForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['passworld']
            user = User.objects.get(username = username)
            if user.password == password:
                a1 = 1
                a2 = 2
                a3 = 3
                a4 = 4
                #返回登陆成功页面
                return render_to_response('select.html',locals())
            else:
                 return render_to_response('wrong.html')
        else:
            return render_to_response('wrong.html')
    else:
        uf = LogForm()
        return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(request))

def personal(request):
    if request.method == "POST":
        uf = PersonForm(request.POST)
        if uf.is_valid():
            usernames = uf.cleaned_data['username']
            passworlds = uf.cleaned_data['passworld']
            pers = User.objects.get(username = usernames)
            if pers.password == passworlds:
                newpassd = uf.cleaned_data['newpass']
                emails = uf.cleaned_data['email']
                names = uf.cleaned_data['name']
                nums = uf.cleaned_data['num']
                majors = uf.cleaned_data['major']
                pers.password = newpassd
                pers.email = emails
                pers.name = names
                pers.num = nums
                pers.major = majors
                a1 = 1
                a2 = 2
                a3 = 3
                a4 = 4
                pers.save()
                return render_to_response('select.html',locals())
            else :
                return render_to_response('wrong.html')
    else:
        uf = PersonForm()
        return render_to_response('personal.html',{'uf':uf},context_instance=RequestContext(request))

def result(request, num):

	return render_to_response('result.html')

def aboutus(request):

	return render_to_response('about_us.html')


def tomap(request):
	return render_to_response('map.html')
    
def detail(request):
    return render_to_response('detail.html')

def logout(request):
    return render_to_response('login.html')
