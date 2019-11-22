from django.shortcuts import render
from .final import final
from django.http import HttpResponseRedirect ,HttpResponse
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from keras.models import model_from_json
import re
import numpy
import h5py
import tweepy
#import xlrd
import array
#import xlwt
import matplotlib.pyplot as plt

def index(request):
    return render(request,'sentimental/index.html')

def index2(request):
    return render(request,'sentimental/result.html')

def index3(request):
    return render(request,'sentimental/applications.html')

def index1(request):
    if 'search' in request.GET:
        message=request.GET['search']
        m=final(message)
        ex=m.sentiment()
        context={
            'search':message,
            'ex':ex[0],
            'ex1': ex[1],
            'ex2': ex[2],
        }
        return render(request, 'sentimental/result.html',context)


def index4(request):
        m = final('uri movie')
        ex = m.sentiment()
        context = {
            'search': 'uri movie',
            'ex': ex[0],
            'ex1': ex[1],
            'ex2': ex[2],
        }
        return render(request, 'sentimental/result.html', context)


def index5(request):
    m = final('elon musk ashlee vance')
    ex = m.sentiment()
    context = {
        'search': 'elon musk ashlee vance',
        'ex': ex[0],
        'ex1': ex[1],
        'ex2': ex[2],
    }
    return render(request, 'sentimental/result.html', context)

def index6(request):
    m = final('apex legends')
    ex = m.sentiment()
    context = {
        'search': 'apex legends',
        'ex': ex[0],
        'ex1': ex[1],
        'ex2': ex[2],
    }
    return render(request, 'sentimental/result.html', context)
def index7(request):
    m = final('stranger things')
    ex = m.sentiment()
    context = {
        'search': 'stranger things',
        'ex': ex[0],
        'ex1': ex[1],
        'ex2': ex[2],
    }
    return render(request, 'sentimental/result.html', context)
def index8(request):
    m = final('air pods')
    ex = m.sentiment()
    context = {
        'search': 'air pods',
        'ex': ex[0],
        'ex1': ex[1],
        'ex2': ex[2],
    }
    return render(request, 'sentimental/result.html', context)
def index9(request):
    m = final('india election 2019')
    ex = m.sentiment()
    context = {
        'search': 'india election 2019',
        'ex': ex[0],
        'ex1': ex[1],
        'ex2': ex[2],
    }
    return render(request, 'sentimental/electionresult.html', context)
def index10(request):
    m = final('cricket world cup 2019')
    ex = m.sentiment()
    context = {
        'search': 'cricket world cup 2019',
        'ex': ex[0],
        'ex1': ex[1],
        'ex2': ex[2],
    }
    return render(request, 'sentimental/worldresult.html', context)

def index11(request):
    m = final('smart phones')
    ex = m.sentiment()
    context = {
        'search': 'smart phones',
        'ex': ex[0],
        'ex1': ex[1],
        'ex2': ex[2],
    }
    return render(request, 'sentimental/productresult.html', context)