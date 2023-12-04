from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.home_page, name="home"),
    path('about/', views.about, name="about"),
    path('feature/', views.feature, name="feature"),
    path('team/', views.team, name="team"),
    path('faq/', views.faq, name="faq"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('error/', views.error_404, name="error"),
    path('service/', views.service, name="service"),
    path('project/', views.project, name="project"),
    path('contact/', views.contact, name='contact'),

    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),

    path('reset_password/',
         views.PasswordResetView.as_view(template_name='password_reset_form.html'),
         name="reset_password"),
    path('reset_password_sent/',
         views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name="password_reset_complete"),

    path('change_password/',
         views.PasswordChangeView.as_view(template_name='password_change_form.html'),
         name="password_change"),
    path('change_password/done/',
         views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name="password_change_done")
]


