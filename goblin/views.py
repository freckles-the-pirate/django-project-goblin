from django.shortcuts import render
from goblin.settings import GOBLIN_TEMPLATE_DIR

from goblin.models import *

# Create your views here.

def list_projects(request):
    template = '%s/project_list.html'%settings.GOBLIN_TEMPLATE_DIR
    return render(request, template)

def show_project(request, project_slug):
    template = '%s/project.html'%settings.GOBLIN_TEMPLATE_DIR
    p = Project.objects.get(slug=project_slug)
    context = {
        'project' : p,
    }
    return render(request, context, template)

def project_release(request, project_slug, version):
    p = Project.objects.get(slug=project_slug)
    v = Version.from_str(version)
    release = Release.objects.get(project=project, version=v)
    context = {
        'project' : p,
        #'version' : v,
        'release' : release,
    }
    template = '%s/release.html'%settings.GOBLIN_TEMPLATE_DIR
    return render(request, context, template)
