from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Balance, Points_table, Reward, Request, best_pic, quote


def home(request):
    return render(request, 'home.html')

def login_app(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_app(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required(login_url = '/login/')
def profile(request):
    balance = Balance.objects.all()
    current_balance = Balance.objects.get(id=len(balance))
    quo = quote.objects.get(id=len(quote.objects.all()))
    return render(request, 'profile.html', {'current_balance':current_balance, 'quote' : quo})

@login_required(login_url = '/login/')
def preview_html(request):
    image = best_pic.objects.get(id=len(best_pic.objects.all()))
    return render(request, 'image_preview.html', {'image' : image})

@login_required(login_url = '/login/')
def history(request):
    balance = []
    last = 0
    for b in Balance.objects.all():
        b.cum = b.points - last
        balance.append(b)
        last = b.points
    return render(request, 'history.html', {'history' : balance})

@login_required(login_url = '/login/')
def table(request):
    table = Points_table.objects.all()
    return render(request, 'table.html', {'table' : table})

@login_required(login_url = '/login/')
def rewards(request):
    rewards_table = Reward.objects.all()
    return render(request, 'rewards.html', {'rewards' : rewards_table})

@login_required(login_url = '/login/')
def requests(request):
    REQUESTS = Request.objects.all()
    return render(request, 'requests.html', {'requests' : REQUESTS})

@login_required(login_url = '/login/')
def req_detail(request, req_id):
    return render(request, 'req_detail.html', {'req_id' : req_id, 'request' : Request.objects.get(id=req_id)})
