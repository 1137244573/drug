"""
URL configuration for drug_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from app.views import drug, work, out, ink, login, pay, search, home, datapic, datapicwork

urlpatterns = [

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

    path("stock_query/", drug.stock_query),
    path("stock_query/work/", drug.stock_querywork),

    # 药品
    path("drug/list/", drug.drug_list),
    path("drug/worklist/", drug.drug_worklist),
    path("drug/userlist/", drug.drug_userlist),
    path("drug/add/", drug.drug_add),
    path("drug/workadd/", drug.drug_workadd),
    path("drug/<int:nid>/edit/", drug.drug_edit),
    path("drug/<int:nid>/workedit/", drug.drug_workedit),
    path("drug/<int:nid>/del/", drug.drug_del),
    path("drug/<int:nid>/workdel/", drug.drug_workdel),

    # 工作人员
    path("work/list/", work.work_list),
    path("work/add/", work.work_add),
    path("work/<int:nid>/edit/", work.work_edit),
    path("work/<int:nid>/change/", work.work_change),
    path("work/<int:nid>/del/", work.work_del),

    # 普通用户
    path("putong/list/", work.putong_list),
    path("putong/<int:nid>/edit/", work.putong_edit),
    path("putong/<int:nid>/del/", work.putong_del),

    # 出库
    path("out/list/", out.out_list),
    path("out/worklist/", out.out_worklist),
    path("out/add/", out.out_add),
    path("out/workadd/", out.out_workadd),

    # 入库
    path("ink/list/", ink.ink_list),
    path("ink/worklist/", ink.ink_worklist),
    path("ink/add/", ink.ink_add),
    path("ink/workadd/", ink.ink_workadd),

    # 登录
    path("login/", login.login),
    path("logout/", login.logout),
    path("change/", login.change_pwd),
    path("change/work/", login.change_workpwd),

    # 注册
    path("login/reg/", login.login_reg),

    # 支付
    path("pay/", pay.pay),

    # 搜索

    path("search/drug/", search.search_drug),
    path("search/workdrug/", search.search_workdrug),
    path("search/userdrug/", search.search_userdrug),
    path("search/work/", search.search_work),
    path("search/out/", search.search_out),

    path("search/workout/", search.search_workout),
    path("search/in/", search.search_in),
    path("search/workin/", search.search_workin),

    # 主界面
    path("home/", home.home),
    path("home_2/", home.home_2),
    path("home_3/", home.home_3),

    # 数据统计

    path("datapic/chu/", datapic.datapic_chu),
    path("datapic/ru/", datapic.datapic_ru),
    path("datapic/num/", datapic.datapic_num),
    path("datapic/chuhuan/", datapic.datapic_chuhuan),
    path("datapic/ruhuan/", datapic.datapic_ruhuan),
    path("datapic/baoxian/", datapic.datapic_baoxian),
    path("datapic/kangjun/", datapic.datapic_kangjun),
    path("datapic/zhong/", datapic.datapic_zhong),
    path("datapic/money/", datapic.datapic_money),

    # 员工数据统计
    path("datapicwork/chu/", datapicwork.datapic_chu),
    path("datapicwork/ru/", datapicwork.datapic_ru),
    path("datapicwork/num/", datapicwork.datapic_num),
    path("datapicwork/chuhuan/", datapicwork.datapic_chuhuan),
    path("datapicwork/ruhuan/", datapicwork.datapic_ruhuan),
    path("datapicwork/baoxian/", datapicwork.datapic_baoxian),
    path("datapicwork/kangjun/", datapicwork.datapic_kangjun),
    path("datapicwork/zhong/", datapicwork.datapic_zhong),
    path("datapicwork/money/", datapicwork.datapic_money),

]
