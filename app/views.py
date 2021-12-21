from django.shortcuts import render
from django_filters import filterset
from rest_framework import viewsets,filters
from .serializers import CategorySerializer,RandomListSerializer
from .models import Category,RandomList
from django_filters.rest_framework import DjangoFilterBackend
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class RandomListViewSet(viewsets.ModelViewSet):
    serializer_class = RandomListSerializer
    queryset = RandomList.objects.all()
    #adding filters to admin page for testing api and search query also
    # filter_backends = [DjangoFilterBackend,filters.SearchFilter] #seach field by name
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]  #ordering fields 1
    filterset.fields=["category","id","name"]
    search_fields=['name']
    #2 acceding descending orders for name,category,and so on
    ordering_fields="__all__"

def index(request):
    queryset = RandomList.objects.all().order_by('name')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 5)  # specify here how much record u want to show
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    # return render(request,"index.html")
    return render(request,"index.html",{"users":users})

def index_js(request):
    return render(request, "index_js.html")