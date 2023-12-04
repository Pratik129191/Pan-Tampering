from django.forms import ModelForm
from django.contrib.auth.models import AnonymousUser
from .models import Pancard, PancardImage


class PancardForm(ModelForm):
    user = AnonymousUser()
    
    def save(self, commit=True):
        self.instance = Pancard.objects.create(
            number=self.cleaned_data['number'],
            user=self.user
        )
        return self.instance

    class Meta:
        model = Pancard
        fields = ['number']


class PancardImageForm(ModelForm):
    user = AnonymousUser()

    def save(self, commit=True):
        pan = Pancard.objects.select_related('user').filter(user=self.user).latest()
        self.instance = PancardImage.objects.create(
            image=self.cleaned_data['image'],
            pancard=pan
        )
        return self.instance

    class Meta:
        model = PancardImage
        fields = ['image']


