from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label = "Your name", max_length=100, error_messages={
#         "required":"Your name must not be empty",
#         "max_length": "Please enter a shorter name"
#     })

#     review_text = forms.CharField(label = "Your Feeback", widget = forms.Textarea, max_length=200)
#     rating = forms.IntegerField(min_value=1,max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name','review_text','rating']
        # fields = '__all__'
        # exclude = ['']
        labels = {
            "user_name":"Your name",
            "review_text":"Review Text",
            "rating": "Rating"
        }
        error_messages={
            "user_name":{
                "required":"Your name must not be empty",
                "max_length":"Please enter a shorter name"
            }
        }

    
    