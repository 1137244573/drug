import json
from django.shortcuts import render, redirect, HttpResponse
from app import models
from django import forms
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe
from app.utils.pagination import Pagination
from app.utils.bootstrap import BootStrapModelForm, BootStrapForm
from pyecharts.charts import Bar, Pie, Map, Line, Page, Timeline, Grid
from pyecharts.globals import ThemeType, ChartType, SymbolType
from pyecharts import options as opts
from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum  # 统计数据库中数据的数量
from pyecharts.commons.utils import JsCode



# 出库数据统计
def datapic_chu(request):
    search_data = request.GET.get('q', "")
    data_month = (models.ChuKu.objects.filter(drug_name=search_data)
                  .annotate(month=TruncMonth('out_time'))  # 时间
                  .values('month')  # 月份
                  .annotate(count=Sum('out_number'))  # 数量
                  .order_by('month'))

    x_data = [data['month'].strftime('%Y-%m') for data in data_month]
    y_data = [data['count'] for data in data_month]

    line = (Line(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
    .add_xaxis(x_data)  # 设置x轴 时间月份
    .add_yaxis('药品出库数量', y_data,  # 各月份的出库数量
               is_smooth=True,  # 折线变成曲线
               is_symbol_show=False,  # 是否显示标记点
               linestyle_opts=opts.LineStyleOpts(width=3)  # 线的宽度
               )

    .set_global_opts(tooltip_opts=opts.TooltipOpts(
        trigger='axis', axis_pointer_type='cross', background_color='white'),  # 设置提示框配置项目
        xaxis_opts=opts.AxisOpts(
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="black")
            ),
            axislabel_opts=opts.LabelOpts(color="black"),
        ),
        yaxis_opts=opts.AxisOpts(
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="black")
            ),
            axislabel_opts=opts.LabelOpts(color="black"),
        ),
    )
    )
    context = {
        'chart': line.render_embed()
    }

    return render(request, 'datapic_chu.html', context)


# 入库数据统计
def datapic_ru(request):
    search_data = request.GET.get('q', "")
    data_month = (models.RuKu.objects.filter(drug_name=search_data)
                  .annotate(month=TruncMonth('in_time'))  # 时间
                  .values('month')  # 月份
                  .annotate(count=Sum('in_number'))  # 数量
                  .order_by('month'))

    x_data = [data['month'].strftime('%Y-%m') for data in data_month]
    y_data = [data['count'] for data in data_month]

    line = (Line(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
    .add_xaxis(x_data)  # 设置x轴 时间月份
    .add_yaxis('药品出库数量', y_data,  # 各月份的出库数量
               is_smooth=True,  # 折线变成曲线
               is_symbol_show=False,  # 是否显示标记点
               linestyle_opts=opts.LineStyleOpts(width=3)  # 线的宽度
               )

    .set_global_opts(tooltip_opts=opts.TooltipOpts(
        trigger='axis', axis_pointer_type='cross', background_color='white'),  # 设置提示框配置项目
        xaxis_opts=opts.AxisOpts(
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="black")
            ),
            axislabel_opts=opts.LabelOpts(color="black"),
        ),
        yaxis_opts=opts.AxisOpts(
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="black")
            ),
            axislabel_opts=opts.LabelOpts(color="black"),
        ),
    )
    )
    context = {
        'chart': line.render_embed()
    }

    return render(request, 'datapic_ru.html', context)


# 药品数量占比
def datapic_num(request):
    drug_data = models.Drug.objects.all().order_by('number')
    total_num = []
    drug_names = []
    for drug in drug_data:
        total_num.append(drug.number)
        drug_names.append(drug.drugname)


    bar = (Bar(init_opts=opts.InitOpts(
        width='1100px',height='580px', theme=ThemeType.INFOGRAPHIC))  # 设置图像的长高，以及主题
           .add_xaxis(drug_names)  # 添加X轴数据
           .add_yaxis('药品数量', total_num, bar_width='40px')  # 添加Y轴数据
           .set_global_opts(title_opts=opts.TitleOpts(title='药品库存数量',
                                                      pos_left='42%',
                                                      pos_top='95%',
                                                      title_textstyle_opts=opts.TextStyleOpts(
                                                          font_size=25,
                                                          font_family='KaiTi'), ),

                            legend_opts=opts.LegendOpts(pos_top='2%',
                                                        item_height=20,
                                                        item_gap=20,
                                                        ),  # 设置图例位置

                            xaxis_opts=opts.AxisOpts(name='药品名',  # 坐标轴名称
                                                     name_location='center',  # 坐标轴位置
                                                     name_gap=25,  # 坐标轴名称距离坐标标签的位置
                                                     ),
                            tooltip_opts=opts.TooltipOpts(
                                trigger='axis', axis_pointer_type='cross', background_color='white'),
                            datazoom_opts=opts.DataZoomOpts(type_='inside') # 区域缩放
                            )
           )

    context = {
        'charts': bar.render_embed()
    }

    return render(request, 'datapic_num.html', context)


# 出库饼图
def datapic_chuhuan(request):
    month = request.GET.get('month', "1")
    year = request.GET.get('year', '2023')
    total_money = models.ChuKu.objects.filter(out_time__month=month, out_time__year=year).values('drug_name').annotate(
        total=Sum('out_money')).annotate(total_2=Sum('out_number'))

    lists = []
    for data in total_money:
        drugname = data['drug_name']
        money = data['total']
        lists.append((drugname, money))

    pie = (Pie(init_opts=opts.InitOpts(width='500px'))
           .add(series_name='药品出库总价', data_pair=lists,
                label_opts=opts.LabelOpts(formatter="{b}:{c}元 ({d}%)"),
                radius=['30%', '60%'],
                center=['50%', '50%'],
                # rosetype='radius'
                )
           .set_global_opts(title_opts=opts.TitleOpts(title='药品出库金额占比图',
                                                      pos_top='450px',
                                                      pos_left='160px',
                                                      title_textstyle_opts=opts.TextStyleOpts(font_size=18,
                                                                                              font_family='KaiTi')), )
           )

    lists_2 = []
    for data_2 in total_money:
        drugname = data_2['drug_name']
        num = data_2['total_2']
        lists_2.append((drugname, num))

    pie_2 = (Pie(init_opts=opts.InitOpts(width='500px'))
             .add(series_name='药品出库数量', data_pair=lists_2,
                  label_opts=opts.LabelOpts(formatter="{b}:{c} ({d}%)"),
                  radius=['30%', '60%'],
                  center=['50%', '50%'],
                  )
             .set_global_opts(title_opts=opts.TitleOpts(title='药品出库数量占比图',
                                                        pos_top='450px',
                                                        pos_right='160px',
                                                        title_textstyle_opts=opts.TextStyleOpts(font_size=18,
                                                                                                font_family='KaiTi')))
             )

    context = {
        'charts': pie.render_embed(),
        'charts_2': pie_2.render_embed()
    }

    return render(request, 'datapic_chuhuan.html', context)


# 入库饼图
def datapic_ruhuan(request):
    month = request.GET.get('month', "1")
    year = request.GET.get('year', '2023')
    total_money = models.RuKu.objects.filter(in_time__month=month, in_time__year=year).values('drug_name').annotate(
        total=Sum('in_money')).annotate(total_2=Sum('in_number'))

    ru_list = []
    for data in total_money:
        drugname = data['drug_name']
        money = data['total']
        ru_list.append((drugname, money))

    pie = (Pie(init_opts=opts.InitOpts(width='500px'))
           .add(series_name='药品入库总价', data_pair=ru_list,
                label_opts=opts.LabelOpts(formatter="{b}:{c}元 ({d}%)"),
                radius=['30%', '60%'],
                center=['50%', '50%'],
                # rosetype='radius'
                )
           .set_global_opts(title_opts=opts.TitleOpts(title='药品入库金额占比图',
                                                      pos_top='450px',
                                                      pos_left='160px',
                                                      title_textstyle_opts=opts.TextStyleOpts(font_size=18,
                                                                                              font_family='KaiTi')), )
           )

    ru_lists_2 = []
    for data_2 in total_money:
        drugname = data_2['drug_name']
        num = data_2['total_2']
        ru_lists_2.append((drugname, num))

    pie_2 = (Pie(init_opts=opts.InitOpts(width='500px'))
             .add(series_name='药品入库数量', data_pair=ru_lists_2,
                  label_opts=opts.LabelOpts(formatter="{b}:{c} ({d}%)"),
                  radius=['30%', '60%'],
                  center=['50%', '50%'],
                  )
             .set_global_opts(title_opts=opts.TitleOpts(title='药品入库数量占比图',
                                                        pos_top='450px',
                                                        pos_right='160px',
                                                        title_textstyle_opts=opts.TextStyleOpts(font_size=18,
                                                                                                font_family='KaiTi')))
             )

    context = {
        'charts': pie.render_embed(),
        'charts_2': pie_2.render_embed()
    }

    return render(request, 'datapic_ruhuan.html', context)



# 保险类型
def datapic_baoxian(request):
    ins_counts = models.Drug.objects.values('insure').annotate(count=Count('id')).annotate(sum=Sum('number'))

    ins_types = [ins['insure'] for ins in ins_counts]
    ins_types_display = [dict(models.Drug.insure_choices)[ins] for ins in ins_types]
    drug_counts = [num['count'] for num in ins_counts]

    bar = (Bar(init_opts=opts.InitOpts(
        width='600px', theme=ThemeType.INFOGRAPHIC))  # 设置图像的长高，以及主题
           .add_xaxis(ins_types_display)  # 添加X轴数据
           .add_yaxis('药品种类数量', drug_counts)  # 添加Y轴数据
           .set_global_opts(title_opts=opts.TitleOpts(title='各保险类型药品种类数量',
                                                      pos_left='30%',
                                                      pos_top='95%',
                                                      title_textstyle_opts=opts.TextStyleOpts(
                                                                                              font_size=20,
                                                                                              font_family='KaiTi'),),


                            legend_opts=opts.LegendOpts(pos_top='2%',
                                                        item_height=20,
                                                        item_gap=20,
                                                       ),  # 设置图例位置

                            xaxis_opts=opts.AxisOpts(name='保险类型',  # 坐标轴名称
                                                     name_location='center',  # 坐标轴位置
                                                     name_gap=25,  # 坐标轴名称距离坐标标签的位置
                                                     ),
                            tooltip_opts=opts.TooltipOpts(
                                trigger='axis', axis_pointer_type='cross', background_color='white')
                            )
           )

    lists = []
    for data in ins_counts:
        ins_number = data['sum']
        lists.append(ins_number)


    pie = (Pie(init_opts=opts.InitOpts(width='600px'))
           .add(series_name='药品数量', data_pair=[list(z) for z in zip(list(ins_types_display), lists)],
                label_opts=opts.LabelOpts(formatter="{b}:{c} ({d}%)"),
                radius=['30%', '60%'],
                center=['50%', '50%'],
                # rosetype='radius'
                )
           .set_global_opts(title_opts=opts.TitleOpts(title='各保险类型药品数量占比',
                                                      pos_top='95%',
                                                      pos_left='160px',
                                                      title_textstyle_opts=opts.TextStyleOpts(font_size=20,
                                                                                              font_family='KaiTi')), )
           .set_colors(['#FFCC00', '#339933', '#666666', '#00CCFF'])
           )



    context = {
        'charts': bar.render_embed(),
        'charts_2': pie.render_embed(),
    }

    return render(request, 'datapic_baoxian.html', context)



# 抗菌类型
def datapic_kangjun(request):
    drugant_counts = models.Drug.objects.values('drugant').annotate(count=Count('id')).annotate(sum=Sum('number'))

    drugant_types = [ant['drugant'] for ant in drugant_counts]
    drugant_types_display = [dict(models.Drug.drugant_choices)[ant] for ant in drugant_types]
    drug_counts = [num['count'] for num in drugant_counts]

    bar = (Bar(init_opts=opts.InitOpts(
        width='600px', theme=ThemeType.INFOGRAPHIC))  # 设置图像的长高，以及主题
           .add_xaxis(drugant_types_display)  # 添加X轴数据
           .add_yaxis('药品种类数量', drug_counts)  # 添加Y轴数据
           .set_global_opts(title_opts=opts.TitleOpts(title='各抗菌类型药品种类数量',
                                                      pos_left='30%',
                                                      pos_top='95%',
                                                      title_textstyle_opts=opts.TextStyleOpts(
                                                                                              font_size=20,
                                                                                              font_family='KaiTi'),),


                            legend_opts=opts.LegendOpts(pos_top='2%',
                                                        item_height=20,
                                                        item_gap=20,
                                                       ),  # 设置图例位置

                            xaxis_opts=opts.AxisOpts(name='药品抗菌类型',  # 坐标轴名称
                                                     name_location='center',  # 坐标轴位置
                                                     name_gap=25,  # 坐标轴名称距离坐标标签的位置
                                                     ),
                            tooltip_opts=opts.TooltipOpts(
                                trigger='axis', axis_pointer_type='cross', background_color='white')
                            )
           )

    lists = []
    for data in drugant_counts:
        drugant_number = data['sum']
        lists.append(drugant_number)


    pie = (Pie(init_opts=opts.InitOpts(width='600px'))
           .add(series_name='药品数量', data_pair=[list(z) for z in zip(list(drugant_types_display), lists)],
                label_opts=opts.LabelOpts(formatter="{b}:{c} ({d}%)"),
                radius=['30%', '60%'],
                center=['50%', '50%'],
                # rosetype='radius'
                )
           .set_global_opts(title_opts=opts.TitleOpts(title='各抗菌类型药品数量占比',
                                                      pos_top='95%',
                                                      pos_left='160px',
                                                      title_textstyle_opts=opts.TextStyleOpts(font_size=20,
                                                                                              font_family='KaiTi')), )
           .set_colors(['#990033', '#660099', '#FFCC00', '#339933', '#666666', '#00CCFF', '#996600'])
           )



    context = {
        'charts': bar.render_embed(),
        'charts_2': pie.render_embed(),
    }

    return render(request, 'datapic_kangjun.html', context)



# 一致性检验，重点关注药品
def datapic_zhong(request):
    drugkey_counts = models.Drug.objects.values('drugkey').annotate(count=Count('id'))

    drugkey_types = [key['drugkey'] for key in drugkey_counts]
    drugkey_types_display = [dict(models.Drug.drugkey_choices)[key] for key in drugkey_types]
    drug_counts = [num['count'] for num in drugkey_counts]

    bar = (Bar(init_opts=opts.InitOpts(
        width='600px', theme=ThemeType.INFOGRAPHIC))  # 设置图像的长高，以及主题
           .add_xaxis(drugkey_types_display)  # 添加X轴数据
           .add_yaxis('药品种类数量', drug_counts, bar_width=80)  # 添加Y轴数据
           .set_global_opts(title_opts=opts.TitleOpts(title='营养性辅助性重点关注药品种类数量',
                                                      pos_left='30%',
                                                      pos_top='95%',
                                                      title_textstyle_opts=opts.TextStyleOpts(
                                                                                              font_size=20,
                                                                                              font_family='KaiTi'),),


                            legend_opts=opts.LegendOpts(pos_top='2%',
                                                        item_height=20,
                                                        item_gap=20,
                                                       ),  # 设置图例位置

                            xaxis_opts=opts.AxisOpts(name='是否是重点药品',  # 坐标轴名称
                                                     name_location='center',  # 坐标轴位置
                                                     name_gap=25,  # 坐标轴名称距离坐标标签的位置
                                                     ),
                            tooltip_opts=opts.TooltipOpts(
                                trigger='axis', axis_pointer_type='cross', background_color='white')
                            )
           )

    drugun_counts = models.Drug.objects.values('drugun').annotate(count=Count('id'))

    drugun_types = [un['drugun'] for un in drugun_counts]
    drugun_types_display = [dict(models.Drug.drugun_choices)[un] for un in drugun_types]
    drugun_counts = [num['count'] for num in drugun_counts]

    bar_2 = (Bar(init_opts=opts.InitOpts(
        width='600px', theme=ThemeType.INFOGRAPHIC))  # 设置图像的长高，以及主题
           .add_xaxis(drugun_types_display)  # 添加X轴数据
           .add_yaxis('药品种类数量', drugun_counts, bar_width=80)  # 添加Y轴数据
           .set_global_opts(title_opts=opts.TitleOpts(title='一致性检验药品种类数量',
                                                      pos_left='30%',
                                                      pos_top='95%',
                                                      title_textstyle_opts=opts.TextStyleOpts(
                                                          font_size=20,
                                                          font_family='KaiTi'), ),

                            legend_opts=opts.LegendOpts(pos_top='2%',
                                                        item_height=20,
                                                        item_gap=20,
                                                        ),  # 设置图例位置

                            xaxis_opts=opts.AxisOpts(name='是否通过',  # 坐标轴名称
                                                     name_location='center',  # 坐标轴位置
                                                     name_gap=25,  # 坐标轴名称距离坐标标签的位置
                                                     ),
                            tooltip_opts=opts.TooltipOpts(
                                trigger='axis', axis_pointer_type='cross', background_color='white')
                            )
           )



    context = {
        'charts': bar.render_embed(),
        'charts_2': bar_2.render_embed(),
    }

    return render(request, 'datapic_zhong.html', context)





# 各个价格区间
def datapic_money(request):
    money_ranges = ['0-20', '20-50', '50-100', '100-200', '200-500', '500-1000', '1000']
    drug_counts = []
    # 计算每个区间的数量
    for i in range(len(money_ranges)):
        # 0-20
        if i == 0:
            min_price = 0
            max_price = 20
            count = models.Drug.objects.filter(money__gte=min_price, money__lt=max_price).aggregate(count=Count('id'))[
                'count']
            drug_counts.append(count)
        # 1000以上
        elif i == len(money_ranges) - 1:
            min_price = float(money_ranges[i].split('-')[0])
            count = models.Drug.objects.filter(money__gte=min_price).aggregate(count=Count('id'))['count']
            drug_counts.append(count)
        # 中间的
        else:
            min_price = float(money_ranges[i].split('-')[0])
            max_price = float(money_ranges[i].split('-')[1])
            count = models.Drug.objects.filter(money__gte=min_price, money__lt=max_price).aggregate(count=Count('id'))[
                'count']
            drug_counts.append(count)

    bar = (Bar(init_opts=opts.InitOpts(
        width='600px',height='550px', theme=ThemeType.INFOGRAPHIC))  # 设置图像的长高，以及主题
           .add_xaxis(money_ranges)  # 添加X轴数据
           .add_yaxis('药品种类数量', drug_counts,bar_width=60)  # 添加Y轴数据
           .set_global_opts(title_opts=opts.TitleOpts(title='各价格区间药品种类',
                                                      pos_left='32%',
                                                      pos_top='94%',
                                                      title_textstyle_opts=opts.TextStyleOpts(
                                                                                              font_size=20,
                                                                                              font_family='KaiTi'),),
                            legend_opts=opts.LegendOpts(pos_top='2%',
                                                        item_height=20,
                                                        item_gap=20,
                                                       ),  # 设置图例位置
                            xaxis_opts=opts.AxisOpts(name='价格',  # 坐标轴名称
                                                     name_location='center',  # 坐标轴位置
                                                     name_gap=25,  # 坐标轴名称距离坐标标签的位置
                                                     ),
                            tooltip_opts=opts.TooltipOpts(
                                trigger='axis', axis_pointer_type='cross', background_color='white')))

    pie = (Pie(init_opts=opts.InitOpts(width='600px',height='550px'))
           .add(series_name='药品种类数量', data_pair=[list(z) for z in zip(money_ranges, drug_counts)],
                label_opts=opts.LabelOpts(formatter="{b}:{c} ({d}%)"),
                radius=['30%', '60%'],
                center=['50%', '50%'],
                # rosetype='radius'
                )
           .set_global_opts(title_opts=opts.TitleOpts(title='各价格药品种类占比',
                                                      pos_top='94%',
                                                      pos_left='200px',
                                                      title_textstyle_opts=opts.TextStyleOpts(font_size=20,
                                                                                              font_family='KaiTi')), )
           .set_colors(['#990033', '#660099', '#FFCC00', '#339933', '#666666', '#00CCFF', '#996600'])
           )

    context = {
        'charts': bar.render_embed(),
        'charts_2': pie.render_embed(),
    }

    return render(request, 'datapic_money.html', context)

