from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

# Create your views here.

class ReviewView(View):
    # this get and post are predifined name (methods) you cannot change it.
    def get(self,request):
        form = ReviewForm()
        return render(request,"reviews/review.html",{
        "form_key": form
        })
    
    def post(self,request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request,"reviews/review.html",{
        "form_key": form
        }) 
            # return render(request,"reviews/tnak")






def review(request):
    # has_error = False
    # if request.method == 'POST':
    #     entered_username = request.POST['usernamename']
    #     print(entered_username)
    #     if entered_username=="":
    #         return render(request,"reviews/review.html",{
    #             "has_error" : True
    #         })
    #     return HttpResponseRedirect("/thank-you")



    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # review = Review(user_name = form.cleaned_data['user_name'], review_text = form.cleaned_data['review_text'],rating = form.cleaned_data['rating'])
            # review.save()
            form.save()
            # print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()  

    return render(request,"reviews/review.html",{
        "form_key": form
        })
 


# class tyView(View):
#     def get(self,request):
#         return render(request,"reviews/thankyou.html")
        
# you can do that by dorectly template view

class tyView(TemplateView):
    template_name = "reviews/thankyou.html"

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     return super().get_context_data(**kwargs) 
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['message'] = "This works"
        return context



def thank_you(request):
    return render(request,"reviews/thankyou.html")



# class ReviewsListView(TemplateView):
#     template_name = "reviews/review-list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context
    

class ReviewsListView(ListView):
    template_name = "reviews/review-list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query =  super().get_queryset()      
    #     data = base_query.filter(rating__gt=4)
    #     return data
    



class SingleReviewView(TemplateView):
    template_name = "reviews/single-review.html"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk = review_id)      #since <int:"id" we use id here
        context["ididid"] = review_id
        context["review"] = selected_review 
        print(review_id)
        return context
    

# class SingleReviewView(DetailView):
#     template_name = "reviews/single-review.html"
#     model = Review

    