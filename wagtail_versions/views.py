from django.shortcuts import render, get_object_or_404
from .models import Version

import re

# Create your views here.
def version_list(request):
    versions = list(Version.objects.all())
    new_versions = []
    for version in versions:
        if re.search('^\w\w-', str(version)):
            new_versions.append(version)
    return render(request, 'wagtail_versions/versions_list.html', {'versions': new_versions})

def version(request, version):
    specific_version = get_object_or_404(Version, versions=version)
    return render(request, 'wagtail_versions/version.html', {'version': specific_version})

def error_404(request, exception):
    versions = list(Version.objects.all())
    new_versions = []
    for version in versions:
        if re.search('^\w\w-', str(version)):
            new_versions.append(version)
    return render(request, 'wagtail_versions/versions_list.html', {'versions': new_versions})