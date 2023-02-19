from  django import forms

class EmailPostForm(forms.Form):
    """ 
    Inherits from the base Form class
    """
    # an instance of CharField rendered as <input type="text>
    name = forms.CharField(max_length=25)
    # requires valid email address; else, forms.ValidationError exception is raised
    email = forms.EmailField()
    to = forms.EmailField()
    # displays as <textarea>, and field is optional
    comment = forms.CharField(required=False, 
                              widget=forms.Textarea)