from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.
def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()  

        return redirect("/home")      

    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})

# name: tim123
# password: !34fRbmJQ7Xu@hE

# name: javascript
# password: !34fRbmJQ7Xu@hE