from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from . import models
import json

# Create your views here.
def home(request):
    print('*****************************')
    return index(request, '0')

def index(request, trig):
    langFlag = models.statusFlags.objects.get(descriptor='Language')
    emailFlag = models.statusFlags.objects.get(descriptor='Email1')
    emailBool = emailFlag.stage == '1'
    if langFlag.stage =='1' and trig!='1':
        trig='2'
    template = loader.get_template('virtualpc/home.html')
    context = {}
    context['emailBool'] = emailBool
    print(trig)
    if trig=='0':
        context['flag'] = True
        context['emailBool'] = False
        context['fade'] = True
    elif trig=='1':
        print('sdfdsfdf')
        context['flag'] = False
        context['fade'] = False
    elif trig=='2':
        context['flag'] = False
        context['fade'] = True

    return HttpResponse(template.render(context, request))


def notableCaptives(request, captiveid):
    captiveStage = models.statusFlags.objects.get(descriptor='CaptiveStage')
    batch = captiveStage.stage
    allCaptives = models.captive.objects.filter(batch=batch).order_by("id")
    ids=[x.id for x in allCaptives]
    print(ids)
    captiveid=int(captiveid)
    try:
        pos = ids.index(captiveid)
        print('howdy do')
    except:
        pos = 0
    template = loader.get_template('virtualpc/NotableCaptives.html')
    context = {}
    if pos == 0:
        captive= models.captive.objects.get(id=ids[0])
        nxt=ids[1]
        pre=ids[-1]
    elif pos+1==len(ids):
        captive= models.captive.objects.get(id=ids[-1])
        nxt=ids[0]
        pre=ids[-2]
    else:
        captive= models.captive.objects.get(id=ids[pos])
        nxt=ids[pos+1]
        pre=ids[pos-1]
    print(captive)
    context['captive'] = captive
    context['previd'] = pre
    context['nextid'] = nxt
    return HttpResponse(template.render(context, request))


def incomingCall(request):
    status_obj = models.statusFlags.objects.get(descriptor = 'Phone Call 1')
    json_data = json.dumps({'stage':status_obj.stage})
    return HttpResponse(json_data, content_type="application/json")
