from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label = "Your name", max_length=100, error_messages={
        "required":"Your name must not be empty",
        "max_length": "Please enter a shorter name"
    })

    review_text = forms.CharField(label = "Your Feeback", widget = forms.Textarea, max_length=200)
    rating = forms.IntegerField(min_value=1,max_value=5)
    
    