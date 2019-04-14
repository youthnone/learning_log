from django.shortcuts import render
from .models import Topic,Entry
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicFrom,EntryForm

# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request,'learning_logs/index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('alters_data')
    context = {'topics':topics}
    return  render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-data_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicFrom()
    else:
        # POST 提交的数据，对数据进行处理
        form = TopicFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

def new_entry(request,topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if  form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',args=[topic_id]))

    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

def edit_entry(request,entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method !='POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form =EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic',args=[topic.id]))

    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)

