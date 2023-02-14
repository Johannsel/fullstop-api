from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Deps outside django:
import json


# Custom classes and functions:
from .punctuation import Punctuation
from .dev import Helper

# Create your views here.
@csrf_exempt
def api(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            raw_data = payload['data']
            status = 200

            if "to_compare" in raw_data:
                # Debug
                punctall = Punctuation.punctall(raw_data['to_process'])
                fstop = Punctuation.fstop(raw_data['to_process'])
                data = {
                    'ideal': raw_data['to_compare'],
                    'punctall': [punctall, Helper.cer(punctall, raw_data['to_compare'])],
                    'fstop': [fstop, Helper.cer(fstop, raw_data['to_compare'])],
                    'original': [raw_data['to_process'], Helper.cer(raw_data['to_process'], raw_data['to_compare'])],
                    }
            else:
                # Production
                try:
                    if raw_data['model'] == 'fullstop':
                        data = {'processed': [raw_data['to_process'], Punctuation.fstop(raw_data['to_process']), 'fullstop'],}
                    elif raw_data['model'] == 'punctall':
                        data = {'processed': [raw_data['to_process'], Punctuation.punctall(raw_data['to_process']), 'punctall'],}
                except Exception:
                    data = {'processed': [raw_data['to_process'], Punctuation.fstop(raw_data['to_process']), 'fullstop'],}

            o=dict(data = data)

        except Exception:
            o=dict(data = {'Error':'Internal Server Error!'})
            status = 500
        
        # Convert response to JSON:
        body = json.dumps(o)

        # Construct response:
        response = HttpResponse(body)
        response.headers['Content-Type'] = 'application/json'
        #response.headers['Content-Lenght'] = len(body)
        response.status_code = status
        return response