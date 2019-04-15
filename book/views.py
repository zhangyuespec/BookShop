from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from book import forms, models
import random
from django.contrib import auth
from PIL import Image, ImageDraw, ImageFont
import random
from io import BytesIO
import numpy as np
from django.db.models import F


# Create your views here.

# 注册的视图函数
def register(request):
    form_obj = forms.RegForm()
    if request.method == "POST":
        ret = {"status": 0, "msg": ""}
        form_obj = forms.RegForm(request.POST)
        print(request.POST)
        # 帮我做校验
        if form_obj.is_valid():
            # 校验通过，去数据库创建一个新的用户
            print(111111)
            print(form_obj.cleaned_data)
            form_obj.cleaned_data.pop("re_password")
            print(66666666)
            # form_obj.cleaned_data.pop("csrfmiddlewaretoken")
            print(form_obj.cleaned_data)
            # print(**form_obj.cleaned_data)
            print(7777)
            try:

                models.User.objects.create_user(**form_obj.cleaned_data)

                ret["msg"] = "/index/"
            except:

                ret["msg"] = "/error/"
                print(ret["msg"])
            print(44444444)

            print(5555555555)
            return JsonResponse(ret)
        else:
            print(form_obj.errors)
            ret["status"] = 1
            ret["msg"] = form_obj.errors
            print(ret)
            print("=" * 120)
            return JsonResponse(ret)
    # 生成一个form对象
    # form_obj = forms.RegForm()
    print(222222222)
    print(form_obj.fields)
    return render(request, "register.html", {"form_obj": form_obj})


def index(request):
    import os
    os.system("cp -rf ./media/pic ./static/")
    # book_list = []
    if request.user.is_authenticated():
        content_pks = models.Book.objects.values_list('pk', flat=True)
        selected_pks = random.sample(list(content_pks), 10)
        book_list = models.Book.objects.filter(pk__in=selected_pks)
        # print(book_list)
        selected_pks = random.sample(list(content_pks), 4)
        book_list2 = models.Book.objects.filter(pk__in=selected_pks)
    else:
        # for i in range(10):
        # book_list.append(models.Book.objects.filter(pk=1))
        book_list = models.Book.objects.all()[1:10]
        # print(book_list)
        # print(book0)
        book_list2 = models.Book.objects.all()[1:10]
    activate = models.Activate.objects.all()

    return render(request, "index.html", {"book_list": book_list, "book_list2": book_list2, "activate_list": activate})


def check_username_exist(request):
    print(555555)
    ret = {"status": 0, "msg": ""}
    username = request.GET.get("username")
    print(username + "11111111")
    is_exist = models.User.objects.filter(username=username)
    if is_exist:
        ret["status"] = 1
        ret["msg"] = "用户名已被注册"

    return JsonResponse(ret)


def error(request):
    return render(request, "error.html")


def login(request):
    if request.method == "POST":
        # 初始化一个给AJAX返回的数据
        ret = {"status": 0, "msg": ""}
        # 从提交过来的数据中 取到用户名和密码
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        valid_code = request.POST.get("valid_code")  # 获取用户填写的验证码
        if valid_code and valid_code.upper() == request.session.get("valid_code", "").upper():
            # 验证码正确
            # 利用auth模块做用户名和密码的校验
            user = auth.authenticate(username=username, password=pwd)
            if user:
                # 用户名密码正确
                # 给用户做登录
                auth.login(request, user)
                ret["msg"] = "/index/"
            else:
                # 用户名密码错误
                ret["status"] = 1
                ret["msg"] = "用户名或密码错误！"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"

        return JsonResponse(ret)
    return render(request, "login.html")


# 获取验证码图片的视图
def get_valid_img(request):
    # 获取随机颜色的函数
    def get_random_color():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    # 生成一个图片对象
    img_obj = Image.new(
        'RGB',
        (220, 35),
        get_random_color()
    )
    # 在生成的图片上写字符
    # 生成一个图片画笔对象
    draw_obj = ImageDraw.Draw(img_obj)
    # 加载字体文件， 得到一个字体对象
    font_obj = ImageFont.truetype("static/font/kumo.ttf", 28)
    # 开始生成随机字符串并且写到图片上
    tmp_list = []
    for i in range(5):
        u = chr(random.randint(65, 90))  # 生成大写字母
        l = chr(random.randint(97, 122))  # 生成小写字母
        n = str(random.randint(0, 9))  # 生成数字，注意要转换成字符串类型

        tmp = random.choice([u, l, n])
        tmp_list.append(tmp)
        draw_obj.text((20 + 40 * i, 0), tmp, fill=get_random_color(), font=font_obj)

    # 保存到session
    request.session["valid_code"] = "".join(tmp_list)
    # 加干扰线
    width = 220  # 图片宽度（防止越界）
    height = 35
    for i in range(5):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw_obj.line((x1, y1, x2, y2), fill=get_random_color())

    # 加干扰点
    for i in range(40):
        draw_obj.point((random.randint(0, width), random.randint(0, height)), fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw_obj.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

    # 不需要在硬盘上保存文件，直接在内存中加载就可以
    io_obj = BytesIO()
    # 将生成的图片数据保存在io对象中
    img_obj.save(io_obj, "png")
    # 从io对象里面取上一步保存的数据
    data = io_obj.getvalue()
    return HttpResponse(data)


def logout(request):
    auth.logout(request)
    return redirect("/index/")


def activate(request, pk):
    print(5555555)
    print(pk)
    print(6666666666)
    activate = models.Activate.objects.filter(pk=pk)
    print(activate)
    return render(request, "activate.html", {"activate": activate})


def baoming(request, pk):
    if request.user.is_authenticated():
        a = models.Activate.objects.filter(pk=pk)
        models.Inactivate.objects.create(user_id=request.user.pk, activate_id=pk, is_in=True)
    return redirect("/index/")


def remen(request):
    content_pks = models.Book.objects.values_list('pk', flat=True)
    selected_pks = random.sample(list(content_pks), 20)
    book_list = models.Book.objects.filter(pk__in=selected_pks)
    return render(request, "remen.html", {"book_list": book_list})


def huojiang(request):
    book_list = models.Book.objects.filter(is_huojiang=True)
    return render(request, "huojiang.html", {"book_list": book_list})


def find_book(request):
    book_name = request.GET['book_name']
    print(00000000000000000000)
    print(book_name)
    response = {"status": 0, "msg": ""}

    print(1111111111111)
    book = models.Book.objects.filter(title__contains=book_name)
    print(33333333333)
    print(book)
    if book:
        print("book不空")
        response["status"] = 1
        response["msg"] = "/detail/"
        comment_list = models.Comment.objects.filter(book_id=book[0].pk)
        return render(request, "detail.html", {"book": book, "comment_list": comment_list})

    else:
        print("bookkong")
        print(22222222222222222222)
        # response["status"] = 1
        response["msg"] = "没有你要查询的图书"
        # response["msg"] = "/detail/"
        print(response)
        return JsonResponse(response)


def find(request, pk):
    book = models.Book.objects.filter(nid=pk)
    print(book)
    comment_list = models.Comment.objects.filter(book_id=book[0].pk)
    print(comment_list)
    return render(request, "detail.html", {"book": book, "comment_list": comment_list})


def add_comment(request):
    print(55555555555)
    response = {"msg": ""}
    book_pk = request.GET.get("book_pk")
    print(book_pk)
    # username = request.user.username
    comment = request.GET.get("comment")

    print(comment)
    # book = models.Book.objects.filter(title=book_name)
    models.Comment.objects.create(book_id=book_pk, user_id=request.user.pk, content=comment)
    response["msg"] = "您已评论"
    return render(request, "detail.html")


def shoucang(request, book_pk):
    # book_pk = request.GET.get("book_pk")
    models.Collect.objects.create(book_id=book_pk, user_id=request.user.pk, is_collect=True)
    book = models.Book.objects.filter(nid=book_pk)
    comment_list = models.Comment.objects.filter(book_id=book[0].pk)
    msg = "您已"
    return render(request, "detail.html", {"book": book, "comment_list": comment_list, "msg": msg})


def dianzan(request, pk, book_pk):
    try:
        print(pk, "......", request.user.pk)
        models.Commetupdown.objects.create(comment_id=pk, user_id=request.user.pk, is_up=True)
        print("保存ok")
        book = models.Book.objects.filter(nid=book_pk)
        comment_list = models.Comment.objects.filter(book_id=book[0].pk)
        msg0 = "您已"
        models.Commetupdown.objects.filter(nid=pk).update(count=F("count") + 1)
        return render(request, "detail.html", {"book": book, "comment_list": comment_list, "msg0": msg0})
    except:
        print("出租哦")
        book = models.Book.objects.filter(nid=book_pk)
        comment_list = models.Comment.objects.filter(book_id=book[0].pk)
        # commentup = models.Commetupdown.objects.all()
        # msg0 = "您已"
        return render(request, "detail.html", {"book": book, "comment_list": comment_list})


def home(request):
    if request.user.is_authenticated():
        user_pk = request.user.pk
        collect = models.Collect.objects.filter(user_id=user_pk)
        print(collect)
        commentup = models.Commetupdown.objects.filter(user_id=user_pk)
        print(commentup)
        activate = models.Inactivate.objects.filter(user_id=user_pk)
        print(activate)
        score = models.Score.objects.filter(user_id=user_pk)
        return render(request, "home.html", {"collect": collect, "commentup": commentup, "activate1": activate,"score_list":score})


def score(request):
    if request.user.is_authenticated():
        user_pk = request.user.pk
        score = request.GET.get("score")
        print(score)
        book_id = request.GET.get("book_pk")
        print(book_id)
        models.Score.objects.create(book_id=book_id, user_id=user_pk, score=score)
        print("baocun ok")
        book = models.Book.objects.filter(nid=book_id)
        print(book)
        comment_list = models.Comment.objects.filter(book_id=book[0].pk)
        print(comment_list)
        s = models.Score.objects.filter(user_id=user_pk, book_id=book_id).first()
        print(s)
        # commentup = models.Commetupdown.objects.all()
        # msg0 = "您已"
        print(11111111111111)
        return render(request, "detail.html", {"book": book, "comment_list": comment_list, "score": s})
