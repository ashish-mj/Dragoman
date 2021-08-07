#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:31:10 2021

@author: ashish
"""

from django.http import HttpResponse
from django.shortcuts import render
from googletrans import Translator
translator = Translator()

def hello(request):
    return render(request,'home.html')

def translate(request):
    data=request.GET['initial_text']
    translations = translator.translate(data,dest='hi')
    print(translations.text)
    return HttpResponse(translations.text)

