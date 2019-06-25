from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View


class BlogsIndex(View):
    def get(self,request):
        return HttpResponse('h5')
