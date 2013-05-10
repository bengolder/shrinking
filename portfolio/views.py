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


def add_basics(context=None, page_name=None):
    projects = Project.objects.all()
    basics = {
              'projects':projects,
              'page_title': page_name,
                    }
    if context:
        context.update( basics )
        return context
    else:
        return basics


def index(request):
    return render_to_response(
            'home.html',
            add_basics({},'Shrinking Cities Studio 2013 - DUSP - MIT'),
            )

def work(request):
    return render_to_response(
            'work.html',
            add_basics({},'Student Work - Shrinking Cities Studio 2013 - DUSP - MIT'),
            )

def people(request):
    return render_to_response(
            'people.html',
            add_basics({},'People - Shrinking Cities Studio 2013 - DUSP - MIT'),
            )

def project(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    item_list = project.item_set.order_by('order_key')
    context = {
            'item_list':item_list
            'project':project,
            }
    return render_to_response(
            'project.html',
            add_basics(context, project.title + ' - Shrinking Cities Studio 2013 - DUSP - MIT'),
            )



