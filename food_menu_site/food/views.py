from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic.list import ListView
# Create your views here.
def index(request):
    item_list=Item.objects.all()
    return render(request,'food/index.html',{'item_list': item_list})




def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    content={'item':item}
    return render(request,'food/detail.html',content)
def add_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',{'form':form})


def update_item(request,item_id):
    item=Item.objects.get(pk=item_id)
    form=ItemForm(request.POST or None ,instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request,'food/item-form.html',{'form':form,'item':item})
def delete_item(request,item_id):
    item=Item.objects.get(pk=item_id)

    if request.method=='POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/delete_item.html',{'item':item})