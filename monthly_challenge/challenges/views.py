from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(reqeust):
    return HttpResponse('Home Page')
# def january(request):
#     return HttpResponse('this is january challange')
# def february(request):
#     return HttpResponse('this is february challange')
# def march(request):
#     return HttpResponse('this is march challange')
# def april(request):
#     return HttpResponse('this is april challange')
# def may(request):
#     return HttpResponse('this is may challange')
# def june(request):
#     return HttpResponse('this is june challange')
# def july(request):
#     return HttpResponse('this is july challange')
# def august(request):
#     return HttpResponse('this is august challange')
# def september(request):
#     return HttpResponse('this is september challange')
# def october(request):
#     return HttpResponse('this is october challange')
# def november(request):
#     return HttpResponse('this is november challange')
# def december(request):
#     return HttpResponse('this is december challange')




# def monthly_challenge(request,month):
#     challenge_text = None
#     if month == 'january':
#         challenge_text = 'this is january challange'
#     elif month == 'february':
#         challenge_text = 'this is february challange'
#     elif month == 'march':
#         challenge_text = 'march'
#     elif month == 'april':
#         challenge_text = 'april'
#     else:
#         return HttpResponseNotFound('this month is not supported')
#     return HttpResponse(challenge_text)



monthly_challenges = {
    'january':'this is january challange',
    'february':'this is february challange',
    'march':'this is march challange',
    'april':'this is april challange',
    'may':'this is may challange',
    'june':'this is june challange',
    'july':'this is july challange'

}

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text) 
    except:
        return HttpResponseNotFound('Month not supported')





def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound('Invalid month')
    redirect_month = months[month-1]
    redirect_path = reverse('monthly_challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)