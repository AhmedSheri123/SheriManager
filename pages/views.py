from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserPaymentData, User
import datetime
from .forms import AddUserForm, AddUserProfileForm
# Create your views here.
def index(request, selected_date):
    payed_obj = {}
    not_payed_obj= {}
    
    date_value = selected_date
    year = date_value.split("-")[0]
    month = date_value.split("-")[1]
    if request.method == 'POST':
        date = request.POST['date']
        return redirect("index", selected_date=date)
    payed_obj = UserPaymentData.objects.filter(pay_date__month=month, pay_date__year=year)
    not_payed_obj =User.objects.exclude(id__in=[o.user.id for o in payed_obj])

    return render(request, 'pages/index.html', {"payed_obj":payed_obj, "not_payed_obj":not_payed_obj, "date_value":date_value})

def Pay(request, id):
    if request.method == "POST":
        comment = request.POST['comment']
        date_value = request.POST['date']
        date = datetime.datetime.strptime(date_value, '%Y-%m')
        print(date)
        user = User.objects.get(id=id)
        user_payment_data = UserPaymentData.objects.create(user=user, speed=user.userprofile.speed.name, comment=comment, pay_date=date)
        user_payment_data.save()
        return redirect("index", selected_date=date_value)

def GetDate(request):
    date_now = datetime.datetime.now()
    year = date_now.strftime('%Y')
    month = date_now.strftime('%m')
    date_value = year + '-' + month
    return redirect("index", selected_date=date_value)

def RemovePayment(request, id, selected_date):
    UserPaymentData.objects.get(id=id).delete()
    return redirect("index", selected_date=selected_date)

def AddUser(request):
    add_user_form = AddUserForm
    add_user_profile_form = AddUserProfileForm
    if request.method == 'POST':
        add_user_form = AddUserForm(request.POST)
        add_user_profile_form = AddUserProfileForm(request.POST)
        if add_user_form.is_valid() and add_user_profile_form.is_valid():
            user = add_user_form.save(commit=False)
            user.set_password("1234")
            user.save()
            userprofile = add_user_profile_form.save(commit=False)
            userprofile.user = user
            userprofile.save()
            messages.success(request, "تم الاضافة بنجاح")
        else:
            messages.error(request, "هناك خطاء في المدخلات")
    return render(request, 'pages/AddUser.html', {"add_user_form":add_user_form, "add_user_profile_form":add_user_profile_form})
