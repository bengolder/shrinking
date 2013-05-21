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

def projects(context=None):
    c = {'projects': Project.objects.all()}
    if not context:
        return c
    else:
        return context.update(c)

def title(page_name, context=None):
    c = {
              'page_title': page_name,
                    }
    if not context:
        return c
    else:
        return context.update(c)

def index(request):
    return render_to_response(
            'home.html',
            title('Shrinking Cities Studio 2013 - DUSP - MIT'),
            )

def work(request):
    c = projects()
    c.update( title('Student Work - Shrinking Cities Studio 2013 - DUSP - MIT')
            )
    return render_to_response(
            'work.html',
            c
            )

def people(request):
    bios = Person.objects.order_by('name')
    c = {
            'page_title':'People - Shrinking Cities Studio 2013 - DUSP - MIT',
            'people': bios,
            }
    return render_to_response(
            'people.html',
            c
            )

def project(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    item_list = project.item_set.order_by('order_key')
    context = {
            'page_title': project.title + ' - Shrinking Cities Studio 2013 - DUSP - MIT',
            'item_list':item_list,
            'project':project,
            }
    return render_to_response(
            'project.html',
            context,
            )



