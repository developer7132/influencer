from django import forms

class UserForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] = "Please Input valid email address"
        self.fields["email"].widget.attrs["class"] = "form-control"

class ReferUserForm(forms.Form):
    email = forms.EmailField()
    code = forms.CharField(max_length=6)
    def __init__(self, *args, **kwargs):
        super(ReferUserForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] = "Please Input valid email address"
        self.fields["email"].widget.attrs["class"] = "form-control"

        self.fields["code"].widget.attrs["placeholder"] = "Please Input referer's code. (6 characters)"
        self.fields["code"].widget.attrs["class"] = "form-control"