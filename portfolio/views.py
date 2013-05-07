# portfolio.views.py
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from portfolio.models import Item, Project, ItemForm, ProjectForm
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
    project_list = Project.objects.order_by('end_date').reverse()
    basics = {
              'project_list':project_list,
              'navlinks':navs(page_name),
              'embed_types':('iframe','template'),
                    }
    if context:
        context.update( basics )
        return context
    else:
        return basics


def index(request):
    return render_to_response(
            'portfolio_index.html',
            add_basics({},'portfolio'),
            )

def project(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    data = {
            'item_list':[],
            'project':project,
            'extra_css':[],
            'extra_js':[],
            }
    item_list = project.item_set.order_by('order_key')
    for i, item in enumerate(item_list):
        """Here is where I can process porjects and project items as they are
        retrieved form the database.

        If I have something very dynamic, how should I return it?
        should I give myself the option of a python script portfolio item?
        That would be the ultimate in flexibility. But it adds complexity.
        """
        if item.media_type == 'template':
            """If it is a template type object it needs a context
                and a template to render it in. I think I should just stick to
                making simple context dictionaries and pasting them in for now.

                template items need a json-like object that has two keys:
                "template" and "context". "context" must contain a json-like
                dictionary object. I can make these from scripts.

                in it's context, it can include 'extra_js' and 'extra_css' keys
                with list values of filenames (assuming the static/js or
                static/css prefix) that are necessary for rendering the
                template.
            """
            embed_data = json.loads(item.embed_field)
            t = embed_data['template']
            c = embed_data['context']
            item.embed_field = get_template(t).render(Context(c))
            if 'extra_js' in c:
                data['extra_js'].extend(c['extra_js'])
            if 'extra_css' in c:
                data['extra_css'].extend(c['extra_css'])
        obj = [i+1, item]
        data['item_list'].append(obj)

    return render_to_response(
            'portfolio_project.html',
            add_basics(data, 'portfolio'),
            )



