# coding=utf8

"""
api util. rely on Django.
"""

__author__ = 'didicout <i@julin.me>'

from django.http import HttpResponse
from django.http import HttpResponseBadRequest

import json


def render_json_success(data, sort_keys=False):
    result = dict()
    result['success'] = True
    result['code'] = 0
    result['message'] = 'success'
    result['data'] = data

    return HttpResponse(json.dumps(result, sort_keys=sort_keys, indent=4),
                        content_type='application/json')


def render_json_p(data, call_back, sort_keys=False):
    result = dict()
    result['success'] = True
    result['code'] = 0
    result['message'] = 'success'
    result['data'] = data
    json_str = json.dumps(result, sort_keys=sort_keys, indent=4)
    return HttpResponse("%s(%s)" % (call_back, json_str), content_type='text/javascript; charset=utf-8')


def render_json_failure(message, code=1):
    result = dict()
    result['success'] = False
    result['code'] = code
    result['message'] = message
    return HttpResponseBadRequest(json.dumps(result, sort_keys=False),
                                  content_type='application/json')


def render_text(message):
    return HttpResponse(message, content_type='text/plain')


def render_text_400(message):
    return HttpResponseBadRequest(message, content_type='text/plain')


def render_html(html):
    return HttpResponse(html, content_type='text/html')