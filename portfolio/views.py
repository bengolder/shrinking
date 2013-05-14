# portfolio.views.py
import os
import json
import random
import django
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from portfolio.models import Item, Project
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpRequest
import datetime
from django.template import Context
from django.template.defaultfilters import slugify
from django.template.loader import get_template
from shrinking.settings import STATIC_URL, MEDIA_URL
from shrinking.views import navs
from people.models import Person

def projects(context={}):
    c = {'projects': Project.objects.all()}
    return context.update(c)

def title(page_name, context={}):
    basics = {
              'page_title': page_name,
                    }
    return context.update(basics)

def index(request):
    return render_to_response(
            'home.html',
            title('Shrinking Cities Studio 2013 - DUSP - MIT'),
            )

def work(request):
    return render_to_response(
            'work.html',
            title('Student Work - Shrinking Cities Studio 2013 - DUSP - MIT',
                projects()
                )
            )

def people(request):
    bios = Person.objects.all()
    c = {
            'people': bios
            }
    return render_to_response(
            'people.html',
            title('People - Shrinking Cities Studio 2013 - DUSP - MIT',
                c)
            )

def project(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    item_list = project.item_set.order_by('order_key')
    context = {
            'item_list':item_list,
            'project':project,
            }
    return render_to_response(
            'project.html',
            title(
                project.title + ' - Shrinking Cities Studio 2013 - DUSP - MIT',
                context),
            )



