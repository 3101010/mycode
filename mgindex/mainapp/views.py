#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth.decorators import permission_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from mainapp.models import (Server_Assets,Assets,User_Server,Service_Assets)

from mainapp.serializers import *
# from mainapp.models import UserProfile

#登录异常
def noperm(request):
    return render(request,'mainapp/noperm.html',{"user":request.user})

#首页
@login_required(login_url='/login')
def index(request):
    return render(request, 'mainapp/index.html')

#常用导航
@login_required(login_url='/login')
def assets_links(request):
    return render(request, 'mainapp/assets_links.html')

#常用导航
@login_required(login_url='/login')
def daohang(request):
    return render(request, 'mainapp/daohang.html')

#资产列表
@login_required(login_url='/login')
def assets_list(request):
    return render(request, 'mainapp/assets_list.html')

#登录验证
def login(request):
    if request.session.get('username') is not None:
        return HttpResponseRedirect('/',{"user":request.user})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user and user.is_active:
            auth.login(request,user)
            request.session['username'] = username
            return HttpResponseRedirect('/daohang',{"user":request.user})
        else:
            if request.method == "POST":
                return render(request, 'mainapp/login.html', {"login_error_info": "用户名不错存在，或者密码错误！"}, )
            else:
                return render(request, 'mainapp/login.html')

#退出登录
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')


#用户管理
@login_required()
@permission_required('auth.change_user',login_url='/noperm/')
def user_manage(request):
    if request.method == "GET":
        userList = User.objects.all()
        groupList = Group.objects.all()
        # ph = User.objects.all()[0].userprofile.phone# 测试
        # print(ph)
        # #添加手机号-old
        # userList_profile = []
        # for usr in userList:
        #     try:
        #         ph = UserProfile.objects.get(user_id=usr.id)
        #     except Exception as e:
        #         ph.phone = 'Null'
        #     usr.phone = ph.phone
        #     userList_profile.append(usr)
        # #增加字段测试
        return render(request,'mainapp/user_manage.html',{"user":request.user,"userList":userList,"groupList":groupList})

#用户添加注册
def register(request):
    if request.method == "POST":
        if request.POST.get('password') == request.POST.get('c_password'):
            try:
                user = User.objects.filter(username=request.POST.get('username'))
                if len(user) > 0:
                    return JsonResponse({"code": 500, "data": None, "msg": "注册失败，用户已经存在。"})
                else:
                    user = User()
                    user.username = request.POST.get('username')
                    user.email = request.POST.get('email')
                    user.is_staff = 0
                    user.is_active = 0
                    user.is_superuser = 0
                    user.set_password(request.POST.get('password'))
                    user.save()
                    # profile = UserProfile()
                    # profile.user_id = user.id
                    # profile.phone = request.POST.get('phone')
                    # profile.save()
                    return JsonResponse({"code": 200, "data": None, "msg": "用户注册成功"})
            except Exception as e:
                return JsonResponse({"code": 500, "data": None, "msg": "用户注册失败"})
        else:
            return JsonResponse({"code": 500, "data": None, "msg": "密码不一致，用户注册失败。"})

#用户操作
@login_required
@permission_required('auth.change_user', login_url='/noperm/')
def user(request, uid):
    if request.method == "GET":
        try:
            user = User.objects.get(id=uid)
        except Exception as e:
            return render(request, 'mainapp/user_info.html', {"user": request.user,
                                                            "errorInfo": "用户不存在，可能已经被删除."})
            # 获取用户权限列表
        userGroupList = []
        permList = Permission.objects.filter(codename__startswith="can_")
        userPermList = [u.get('id') for u in user.user_permissions.values()]
        for ds in permList:
            if ds.id in userPermList:
                ds.status = 1
            else:
                ds.status = 0
            # 获取用户组列表
        groupList = Group.objects.all()
        userGroupList = [g.get('id') for g in user.groups.values()]
        for gs in groupList:
            if gs.id in userGroupList:
                gs.status = 1
            else:
                gs.status = 0
        serverList = Server_Assets.objects.all()
        userServerListId = [i.server_id for i in User_Server.objects.filter(user_id=user.id)]
        for ser in serverList:
            if ser.id in userServerListId:
                ser.status = 1
            else:
                ser.status = 0

        serviceList = Service_Assets.objects.all()
        return render(request, 'mainapp/user_info.html', {"user": request.user, "user_info": user,
                                                        "serverList": serverList, "serviceList": serviceList,
                                                        "permList": permList, "groupList": groupList})

    elif request.method == "POST":
        try:
            user = User.objects.get(id=uid)
            User.objects.filter(id=uid).update(
                is_active=request.POST.get('is_active'),
                is_superuser=int(request.POST.get('is_superuser')),
                email=request.POST.get('email'),
                username=request.POST.get('username')
            )
            # 如果权限key不存在就单做清除权限
            if request.POST.getlist('perms') is None:
                user.user_permissions.clear()
            else:
                userPermList = []
                for perm in user.user_permissions.values():
                    userPermList.append(perm.get('id'))
                permList = [int(i) for i in request.POST.getlist('perms')]
                addPermList = list(set(permList).difference(set(userPermList)))
                delPermList = list(set(userPermList).difference(set(permList)))
                # 添加新增的权限
                for permId in addPermList:
                    perm = Permission.objects.get(id=permId)
                    User.objects.get(id=uid).user_permissions.add(perm)
                # 删除去掉的权限
                for permId in delPermList:
                    perm = Permission.objects.get(id=permId)
                    User.objects.get(id=uid).user_permissions.remove(perm)
                    # 如果用户组key不存在就单做清除用户组
            if request.POST.getlist('groups') is None:
                user.groups.clear()
            else:
                userGroupList = []
                for group in user.groups.values():
                    userGroupList.append(group.get('id'))
                groupList = [int(i) for i in request.POST.getlist('groups')]
                addGroupList = list(set(groupList).difference(set(userGroupList)))
                delGroupList = list(set(userGroupList).difference(set(groupList)))
                # 添加新增的用户组
                for groupId in addGroupList:
                    group = Group.objects.get(id=groupId)
                    user.groups.add(group)
                # 删除去掉的用户组
                for groupId in delGroupList:
                    group = Group.objects.get(id=groupId)
                    user.groups.remove(group)
            return HttpResponseRedirect('/user/{uid}/'.format(uid=uid))
        except Exception as e:
            return render(request, 'mainapp/user_info.html', {"user": request.user, "errorInfo": "用户资料修改错误：%s" % str(e)})


@api_view(['GET', 'PUT', 'DELETE'])
@permission_required('OpsManage.change_user', raise_exception=True)
def user_detail(request, id, format=None):
    """
    Retrieve, update or delete a server assets instance.
    """
    try:
        snippet = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if not request.user.has_perm('OpsManage.delete_user'):
            return Response(status=status.HTTP_403_FORBIDDEN)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)