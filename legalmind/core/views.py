from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import google.generativeai as genai
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-1.5-flash")
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def ragbot(request):
    return render(request, 'core/ragbot.html')
def register(request):
    return render(request, 'core/signup.html')
def login(request):
    return render(request, 'core/login.html')
@csrf_exempt
def ragchat(request):
    if request.method == 'POST':
        #data=json.loads(request.body.POST.get("message"))
        #print(data)
        user_message=request.POST.get('message')
        print(user_message)
        response=model.generate_content(f'Generate A  concise reply for the following message from user:{user_message}.STRICTLY AVOID USING SYMBOLS IN RESPONSE<MAKE SURE THE RESPONS IS CLEAN RAW FORMATTED TEXT')
        print(response.text)
        return JsonResponse({"botReply":response.text})