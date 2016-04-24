import re
from django import template
from django.core.urlresolvers import Resolver404, resolve

register = template.Library()


@register.simple_tag
def active_page(request, view_name):
    if not request:
        return ""
    try:
        if resolve(request.path_info).view_name == view_name:
            return "active"
        else:
            return ""
    except Resolver404:
        return ""