from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import News, Category
from .forms import CategoryForm, NewForm, SearchForm
from django.views.generic import ListView


# class HomeNews(ListView):
#     model = News
#     template_name = 'news/index.html'
#     context_object_name = 'news'
#     # extra_context = {
#     #     'title':'NEWS'
#     # }
#     def get_context_data(self, *, object_list=None, **kwargs):
#         content = super().get_context_data(**kwargs)
#         content['title']='NEWS_LIST'
#         content['categories']=Category.objects.all()
#         return content
#     def get_queryset(self):
#         # return News.objects.filter(is_published=True,category=self.kwargs['pk'])
#         # return News.objects.filter(is_published=True)
#         return News.objects.all()

class HomeCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'CATEGORY_LIST'
        content['categories'] = Category.objects.all()
        return content

    def get_queryset(self):
        return News.objects.filter(is_published=True, category=self.kwargs['pk'])


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    form = SearchForm()
    content = {
        'form': form,
        'news': news,
        'categories': categories,
    }
    return render(request, 'news/index.html', context=content)


# def category(request,pk):
#     news = News.objects.filter(category=pk)
#     categories = Category.objects.all()
#     content = {
#         'news':news,
#         'categories':categories,
#     }
#     return render(request,'news/category.html',context=content)

def detail(request, pk):
    news = News.objects.get(pk=pk)
    categories = Category.objects.all()
    content = {
        'news': news,
        'categories': categories,
    }
    return render(request, 'news/detail.html', context=content)


def n_del(request, pk):
    news = News.objects.get(pk=pk)
    news.delete()
    return redirect('home')


def add_new(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            News.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = NewForm()
    categories = Category.objects.all()
    content = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'news/add_new.html', context=content)


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CategoryForm()
    content = {
        'form': form
    }
    return render(request, 'news/add_category.html', context=content)


def new_update(request, pk):
    news = News.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = NewForm(instance=news)
    content = {
        'news': news,
        'form': form,
    }
    return render(request, 'news/new_update.html', context=content)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        news = News.objects.filter(title__icontains=form.data.get('title'))
        categories = Category.objects.all()
        form = SearchForm()
        content = {
            'news': news,
            'form': form,
            'categories': categories
        }
        return render(request, 'news/index.html', context=content)
