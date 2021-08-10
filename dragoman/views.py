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

def home(request):
    return render(request,'home.html')

def translate(request):
    original = request.GET['initial_text']
    selection = request.GET['type']
    translation=""
    if selection=="English-Hindi":
         translation = translator.translate(original,src='en',dest='hi')
    else:
        translation = translator.translate(original,src='hi',dest='en')
    return render(request,'translate.html',{'original': original,'translation':translation.text})

