from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView as BasePasswordResetView, \
    PasswordResetDoneView as BasePasswordResetDoneView, \
    PasswordResetConfirmView as BasePasswordResetConfirmView, \
    PasswordResetCompleteView as BasePasswordResetCompleteView, \
    PasswordChangeView as BasePasswordChangeView, \
    PasswordChangeDoneView as BasePasswordChangeDoneView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from .forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


def register_user(request):
    form = UserCreationForm()
    context = {
        'form': form,
        'login': reverse('core:login')
    }

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account is Successfully Created for ' + form.cleaned_data.get('username'))
            return redirect('core:login')
        else:
            return HttpResponse([form.errors, form.error_messages])
    return render(request, 'register.html', context)


def login_user(request):
    form = AuthenticationForm()
    context = {
        'form': form,
        'register': reverse('core:register'),
        'forgot_password': reverse('core:reset_password')
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('core:home')
        else:
            return HttpResponse(form.errors)

    return render(request, 'login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('core:home')


def about(request):
    context = {
        'home': reverse('core:home'),
        'about': reverse('core:about'),
        'service': reverse('core:service'),
        'project': reverse('core:project'),
        'feature': reverse('core:feature'),
        'team': reverse('core:team'),
        'faq': reverse('core:faq'),
        'testimonial': reverse('core:testimonial'),
        'error': reverse('core:error'),
        'contact': reverse('core:contact')
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'home': reverse('core:home'),
        'about': reverse('core:about'),
        'service': reverse('core:service'),
        'project': reverse('core:project'),
        'feature': reverse('core:feature'),
        'team': reverse('core:team'),
        'faq': reverse('core:faq'),
        'testimonial': reverse('core:testimonial'),
        'error': reverse('core:error'),
        'contact': reverse('core:contact')
    }
    return render(request, 'contact.html', context)


def feature(request):
    context = {
        'home': reverse('core:home'),
        'about': reverse('core:about'),
        'service': reverse('core:service'),
        'project': reverse('core:project'),
        'feature': reverse('core:feature'),
        'team': reverse('core:team'),
        'faq': reverse('core:faq'),
        'testimonial': reverse('core:testimonial'),
        'error': reverse('core:error'),
        'contact': reverse('core:contact')
    }
    return render(request, 'feature.html', context)


def team(request):
    context = {
        'home': reverse('core:home'),
        'about': reverse('core:about'),
        'service': reverse('core:service'),
        'project': reverse('core:project'),
        'feature': reverse('core:feature'),
        'team': reverse('core:team'),
        'faq': reverse('core:faq'),
        'testimonial': reverse('core:testimonial'),
        'error': reverse('core:error'),
        'contact': reverse('core:contact')
    }
    return render(request, 'team.html', context)


def faq(request):
    context = {
        'home': reverse('core:home'),
        'about': reverse('core:about'),
        'service': reverse('core:service'),
        'project': reverse('core:project'),
        'feature': reverse('core:feature'),
        'team': reverse('core:team'),
        'faq': reverse('core:faq'),
        'testimonial': reverse('core:testimonial'),
        'error': reverse('core:error'),
        'contact': reverse('core:contact')
    }
    return render(request, 'faq.html', context)


def testimonial(request):
    context = {
        'home': reverse('core:home'),
        'about': reverse('core:about'),
        'service': reverse('core:service'),
        'project': reverse('core:project'),
        'feature': reverse('core:feature'),
        'team': reverse('core:team'),
        'faq': reverse('core:faq'),
        'testimonial': reverse('core:testimonial'),
        'error': reverse('core:error'),
        'contact': reverse('core:contact')
    }
    return render(request, 'testimonial.html', context)


def error_404(request):
    context = {
        'home': reverse('core:home'),
        'about': reverse('core:about'),
        'service': reverse('core:service'),
        'project': reverse('core:project'),
        'feature': reverse('core:feature'),
        'team': reverse('core:team'),
        'faq': reverse('core:faq'),
        'testimonial': reverse('core:testimonial'),
        'error': reverse('core:error'),
        'contact': reverse('core:contact')
    }
    return render(request, '404.html', context)


def service(request):
    context = {
        'home': reverse('core:home'),
        'about': reverse('core:about'),
        'service': reverse('core:service'),
        'project': reverse('core:project'),
        'feature': reverse('core:feature'),
        'team': reverse('core:team'),
        'faq': reverse('core:faq'),
        'testimonial': reverse('core:testimonial'),
        'error': reverse('core:error'),
        'contact': reverse('core:contact'),
        'pan': reverse('service:detail')
    }
    return render(request, 'service.html', context)


def project(request):
    context = {
        'home': reverse('core:home'),
        'about': reverse('core:about'),
        'service': reverse('core:service'),
        'project': reverse('core:project'),
        'feature': reverse('core:feature'),
        'team': reverse('core:team'),
        'faq': reverse('core:faq'),
        'testimonial': reverse('core:testimonial'),
        'error': reverse('core:error'),
        'contact': reverse('core:contact')
    }
    return render(request, 'project.html', context)


def home_page(request):
    context = {
        'home': reverse('core:home'),
        'about': reverse('core:about'),
        'feature': reverse('core:feature'),
        'team': reverse('core:team'),
        'faq': reverse('core:faq'),
        'testimonial': reverse('core:testimonial'),
        'error': reverse('core:error'),
        'service': reverse('core:service'),
        'project': reverse('core:project'),
        'contact': reverse('core:contact'),
        'login': reverse('core:login'),
        'logout': reverse('core:logout'),
        'reset': reverse('core:reset_password')
    }
    return render(request, 'index.html', context)



class PasswordResetView(BasePasswordResetView):
    email_template_name = "password_reset_email.html"
    extra_email_context = None
    from_email = None
    html_email_template_name = None
    subject_template_name = "my_password_reset_subject.txt"
    success_url = reverse_lazy("core:password_reset_done")
    template_name = "password_reset_form.html"


class PasswordResetDoneView(BasePasswordResetDoneView):
    template_name = "password_reset_done.html"


class PasswordResetConfirmView(BasePasswordResetConfirmView):
    success_url = reverse_lazy("core:password_reset_complete")
    template_name = "password_reset_confirm.html"


class PasswordResetCompleteView(BasePasswordResetCompleteView):
    template_name = "password_reset_complete.html"


class PasswordChangeView(BasePasswordChangeView):
    success_url = reverse_lazy("core:password_change_done")
    template_name = "password_change_form.html"


class PasswordChangeDoneView(BasePasswordChangeDoneView):
    template_name = "password_change_done.html"


# def reset_password(request):
#     form = PasswordResetForm()
#     context = {
#         'form': form
#     }
#
#     if request.method == 'POST':
#         form.save(
#             request=request,
#             subject_template_name='password_reset_subject.txt',
#             email_template_name='password_reset_email.html',
#         )
#         print("Done")
#     return render(request, 'reset.html', context)
#     return render(request, 'registration/password_reset_email.html', context)


