# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import redis
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("hw index")

def set_data(request):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('The Godfather','Al Pacino, Marlon Brando, Robert Duvall')
    r.set('Schindler\'s list','Liam Neeson, Ralph Fiennes, Ben Kingsley')
    r.set('Saving Private Ryan','Tom Hanks, Matt Damon, Vin Diesel')
    r.set('Back to the Future', 'Michael J. Fox, Christopher Lloyd, Lea Thompson')
    r.set('Casablanca','Ingrid Bergman, Humphrey Bogart, Peter Lorre')
    r.set('The Big Lebowski', 'Julianne Moore, Jeff Bridges, Tara Reid')
    return HttpResponse("database opgevuld")
