from django.conf import settings

from .forms import ChangePasswordForm, LoginForm, MyPasswordResetForm,MyPasswordConfirmForm
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('',views.home,name = "home"),
    
    path('',views.ProductView.as_view(),name ="home"),
    path('mobile/',views.mobile,name = "mobile"),
    path('mobile/<slug:data>',views.mobile,name = "mobiledata"),
    path('profile/',views.profile,name = "profile"),
    path('orders/',views.orders,name = "orders"),
    path('add-to-cart/',views.addtocart,name = "add-to-cart"),
    path('customerregistration/',views.CustomerRegistrationView.as_view(),name = "customerregistration"),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='realstore/login.html',authentication_form= LoginForm),name = "login"),
    path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='realstore/passwordchange.html',form_class= ChangePasswordForm,success_url = '/changepassworddone/'),name = "changepassword"),
    
    path('resetpassword/',auth_views.PasswordResetView.as_view(template_name='realstore/resetpassword.html',form_class= MyPasswordResetForm),name = "resetpassword"),
    
    path('resetpassword/done/',auth_views.PasswordResetDoneView.as_view(template_name='realstore/resetpassworddone.html',),name = "resetpassworddone"),
    
    path('resetpassword/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='realstore/resetpasswordconfirm.html',form_class= MyPasswordConfirmForm),name = "resetpasswordconfirm"),
    
    path('resetpassword/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='realstore/resetpasswordcomplete.html'),name = "resetpasswordcomplete"),
    
    path('changepassword/done/',auth_views.PasswordChangeDoneView.as_view(template_name='realstore/passwordchangedone.html'),name = "changepassworddone"),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name = "logout"),
    path('product-detail/<int:pk>',views.productdetailview.as_view(),name = "product-detail"),
    path('address/',views.address,name = "address"),
    path('checkout/',views.checkout,name = "checkout"),
    path('buy-now/',views.buynow,name = "buy-now"),
    
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)