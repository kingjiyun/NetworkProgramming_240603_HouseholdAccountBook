import json

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from accountbook.models import Category, AccountBook


class CategoryListView(ListView):
    model = Category  # Category 테이블 모든 Category 가져와서 -> category_list라는 context에 담아 category_list.html에 넘긴다


class AccountBookListView(ListView):
    model = AccountBook


class AccountBookCreateView(CreateView):
    model = AccountBook
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('accountbook:accountbook_dashboard')


class AccountBookUpdateView(UpdateView):
    model = AccountBook
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('accountbook:accountbook_list')


class AccountBookDeleteView(DeleteView):
    model = AccountBook
    success_url = reverse_lazy('accountbook:accountbook_list')


def show_chart(request):
    # open(파일경로, 모드(r=읽기, w=쓰기, a=내용추가, b= 바이너리파일, x=파일생성), 인코딩)
    with open('data/data.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)

        #데이터 분해하기
    name = [item['name'] for item in json_data]
    price = [item['price'] for item in json_data]
    ctgColor = [item['ctgColor'] for item in json_data]

    context = {
        'name': name,
        'price': price,
        'ctgColor': ctgColor
    }
    return render(request, 'chart_test/chart_view.html', context=context)
