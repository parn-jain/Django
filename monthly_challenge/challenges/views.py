from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
# def home(reqeust):
#     list_item = ""
#     for i in list(monthly_challenges.keys()):
#         month_path = reverse('monthly_challenge', args = [i])
#         list_item = list_item + f"<li><a href = \"{month_path}\">{i}</a></li>"
#     response_data =f"""
#         <ul>{list_item}</ul>
#     """
#     return HttpResponse(response_data)

def home(request):
    months = list(monthly_challenges.keys())
    return render(request,'challenges/index.html',{
        "months": months
    })
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
    'july':None

}

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)  
        return render(request,'challenges/challenge.html',{
            "text": challenge_text,
            "month":month
        })
    except:
        return HttpResponseNotFound('Month not supported')



def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound('Invalid month')
    redirect_month = months[month-1]
    redirect_path = reverse('monthly_challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
# .\virt\Scripts\activate  