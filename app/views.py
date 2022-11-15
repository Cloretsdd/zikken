# from django.shortcuts import render

# # Create your views here.
from django.views.generic import TemplateView
from requests import request
from .application import recieve


class IndexView(TemplateView):
    template_name = 'app/index.html'

    # def get_context_data(self, **kwargs): # 追加
    #     x = recieve.recieve()
    #     context = super().get_context_data(**kwargs)
    #     context['recieve'] = x
    #     return context