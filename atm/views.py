import uuid
from .models import customer, register_acc, transaction
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.


def index(request):
    return render(request, 'index.html')

########################################################
########################################################


def bank(request):
    return render(request, 'bank.html')

##############################################
##############################################


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if customer.objects.filter(Email=email).exists():
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    # {'x': 'user name taken'}
                    messages.error(request, 'username taken')
                    print('username taken')
                    return redirect('signup')
                elif User.objects.filter(email=email).exists():
                    # {'x': 'email taken'}
                    messages.error(request, 'email taken')
                    print('email taken')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(
                        username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('login')

            else:
                # {'x': 'password notmatching'}
                messages.error(request, 'password not matching')
                print('password not matching')
                return redirect('signup')

        else:
            messages.error(
                request, 'email not associated with the bank account')
            return render(request, 'signup.html')

    else:
        return render(request, 'signup.html')

#########################################################
#########################################################


def login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return render(request, 'bank.html', {'username': request.user.username, 'email': request.user.email})

        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')

#################################################################
#################################################################


def register_account(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        account_number = request.POST.get('account_number')
        Current_PIN = request.POST.get('Current_PIN')
        New_PIN = request.POST.get('New_PIN')
        if register_acc.objects.filter(Email=email).exists():
            messages.error(request, 'account is already registered')
            return redirect('register_account')

        else:
            v5 = User.objects.get(email=email)
            if v5.email == email:
                v = customer.objects.get(Email=email)
                if v.account_number == account_number:

                    if v.PIN == Current_PIN:
                        v1 = register_acc()
                        v1.Email = email
                        v1.account_number = account_number
                        v1.New_PIN = New_PIN
                        v1.save()
                        return render(request, 'bank.html', {'username': request.user.username, 'email': request.user.email})
                    else:
                        messages.error(request, 'Entered current PIN is wrong')
                        return render(request, 'register_account.html')
                else:
                    messages.error(request, "account number doesn't exist")
                    return render(request, 'register_account.html')
            else:
                messages.error(
                    request, 'invalid email associated with the signup detials')
                return render(request, 'register_account.html')
    else:
        return render(request, 'register_account.html')

####################################################################
####################################################################


def withdraw(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        PIN = request.POST.get('PIN')


        
        try:
            v3 = customer.objects.get(Email=request.user.email)
            v2 = register_acc.objects.get(Email=request.user.email)

            if v2.New_PIN == PIN:
                if int(amount) <= int(v3.balance):
                    unique_code = uuid.uuid4()
                    v4 = transaction()
                    v4.unique_code_s = unique_code
                    v4.amount = amount
                    v4.Email = request.user.email
                    v4.save()

                    return render(request, 'qr.html', {'uniquecode': unique_code})

                else:
                    messages.error(request, 'insufficient balance')
                    return render(request, 'withdraw.html')

            else:
                messages.error(request, 'incorrect PIN')
                return render(request, 'withdraw.html')
        except:
            messages.warning(request,'Please Register your account before withdrawing the money')
            return render(request,'withdraw.html')

    else:
        return render(request, 'withdraw.html')

######################################################################
######################################################################


def logout(request):
    auth.logout(request)
    return redirect('login')
