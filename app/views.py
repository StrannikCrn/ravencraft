from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

NEWS_COUNT = 9


def index(request):
    all_bottles = Bottle.objects.all()
    news_list = News.objects.all().order_by("-date")[:6]
    return render(request, 'app/index.html', {
        'bottles': all_bottles,
        'news': news_list,
        'f_news':news_list[:6]
    })


def contacts(request):
    all_bottles = Bottle.objects.all()
    news_list = News.objects.all().order_by("-date")[:6]
    return render(request, 'app/contacts.html', {
        'bottles': all_bottles,
        'f_news': news_list[:6]
    })


def where_buy(request):
    all_bottles = Bottle.objects.all()
    news_list = News.objects.all().order_by("-date")[:6]
    return render(request, 'app/where_buy.html', {
        'bottles': all_bottles,
        'f_news': news_list[:6]
    })


def news(request):
    all_bottles = Bottle.objects.all()
    page = int(request.GET.get("p", 1))
    all_news = News.objects.all()
    result_news = []
    need_to_hide = False
    if len(all_news) > 0:
        result_news = get_for_page(page, all_news, NEWS_COUNT)

        if result_news[len(result_news)-1] == all_news.last():
            need_to_hide = True
    else:
        need_to_hide = True
    return render(request, 'app/news.html', {
        'news_list': result_news,
        'need_to_hide': need_to_hide,
        'bottles': all_bottles,
        'f_news': all_news[:6]
    })


def news_item(request,url):
    all_bottles = Bottle.objects.all()
    news_list = News.objects.all().order_by("-date")[:6]
    result = get_object_or_404(News,url=url)
    bottles_specifs = result.news_item_specif.all()
    gallery_photos = result.gallery_photos.all()
    bottles = []
    for bottles_specif in bottles_specifs:
        bottles.append(bottles_specif.bottle)
    return render(request, 'app/news_item.html', {
        'news_item': result,
        'bottles_news': bottles,
        'gallery_photos': gallery_photos,
        'bottles': all_bottles,
        'f_news': news_list[:6]
    })


def get_news_block(request):
    page = int(request.GET.get("p", 1))
    all_news = News.objects.all()
    result_news = get_for_page(page, all_news, NEWS_COUNT)
    if len(result_news) == 0:
        return HttpResponse("")
    need_to_hide = False
    if result_news[len(result_news)-1] == all_news.last():
        need_to_hide = True
    return render(request, 'app/news_block.html', {
        'news_list': result_news,
        'need_to_hide': need_to_hide
    })


def about_us(request):
    all_news = News.objects.all()
    return render(request, 'app/about_us.html',{
        'f_news': all_news[:6]
    })


def catalog_ajax(request, group,sub_group):
    result_bottles = Bottle.objects.all()
    if group != "":
        group = get_object_or_404(BeerGroup,url=group)
        result_bottles = result_bottles.filter(group=group)
    if sub_group != "" and sub_group != "all" and sub_group != "undefined":
        tag = get_object_or_404(FilterTag,url=sub_group)
        result_bottles = result_bottles.filter(tag__tag=tag)
    all_groups = BeerGroup.objects.all()
    if group != "":
        for group_item in all_groups:
            if group_item == group:
                group_item.current = True
    else:
        if len(all_groups) > 0:
            all_groups[0].current = True
    all_sub_groups = FilterTag.objects.filter(group_id=group.id)
    first_group = FilterTag()
    first_group.url = "all"
    first_group.name = "Все виды"
    first_group.current = True
    result_subs = [first_group]
    result_subs.extend(all_sub_groups)
    if sub_group != "" and sub_group != "all":
        first_group.current = False
        for group_it in all_sub_groups:
            if group_it.url == sub_group:
                group_it.current = True
    return render(request, 'app/catalog_ajax.html', {
        'bottles': result_bottles,
    })



def catalog(request, group,sub_group):
    all_bottles = Bottle.objects.all()
    news_list = News.objects.all().order_by("-date")[:6]
    result_bottles = Bottle.objects.all()
    if group != "":
        group = get_object_or_404(BeerGroup,url=group)
        result_bottles = result_bottles.filter(group=group)
    if sub_group != "" and sub_group != "all":
        tag = get_object_or_404(FilterTag,url=sub_group)
        result_bottles = result_bottles.filter(tag__tag=tag)
    all_groups = BeerGroup.objects.all()
    if group != "":
        for group_item in all_groups:
            if group_item == group:
                group_item.current = True
    else:
        if len(all_groups) > 0:
            all_groups[0].current = True
    all_sub_groups = FilterTag.objects.filter(group_id=group.id)
    first_group = FilterTag()
    first_group.url = "all"
    first_group.name = "Все виды"
    first_group.current = True
    result_subs = [first_group]
    result_subs.extend(all_sub_groups)
    if sub_group != "" and sub_group != "all":
        first_group.current = False
        for group_it in all_sub_groups:
            if group_it.url == sub_group:
                group_it.current = True
    return render(request, 'app/catalog.html', {
        'bottles_catalog': result_bottles,
        'sub_groups': result_subs,
        'groups': all_groups,
        'cur_group': group,
        'bottles': all_bottles,
        'f_news': news_list[:6],
    })


def get_for_page(page, list, count):
    result = []
    left_elems = count*page - count
    i = 0
    for elem in list:
        if i >= left_elems and i <= left_elems + count:
            result.append(elem)
        i += 1

    return result