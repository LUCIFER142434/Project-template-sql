from django.shortcuts import render,get_object_or_404,redirect
from .forms import UserForm
from .models import User


def creat(argument):
    if argument.method == 'POST':
        user_form = UserForm(argument.POST)
        
        if user_form.is_valid():
            user_form.save()
            return redirect('list')
    else:
        user_form = UserForm()
        
    return render(argument,'form.html',{'user_form':user_form})

def list(argument):
    users = User.objects.all()
    return render(argument, 'list.html', {'users':users})

def detail(argument,user_id):
    user = get_object_or_404(User, id=user_id)
    return render(argument,'detail.html',{'user':user})

def update(argument,user_id):
    user = get_object_or_404(User, id=user_id)
    
    if argument.method == 'POST':
        user_form = UserForm(argument.POST,instance=user)
        
        if user_form.is_valid():
            user_form.save()
            return redirect('list')
    else:
        user_form = UserForm(instance=user)
    return render(argument,'form.html',{'user_form':user_form})

def delete(argument,user_id):
    user = get_object_or_404(User,id=user_id)
    if argument.method == 'POST':
        user.delete()
        return redirect('list')
    return render(argument,'form.html',{'user':user})
    