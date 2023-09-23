from django.shortcuts import render, redirect
from .forms import UserRegisterForm

# Create your views here.
def register(request):   
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')

        # továbbo validációs lépések
    else:
        # amikor megnyitom a register oldalt, hogy generálja ki az üres form-ot
        form = UserRegisterForm()

    return render(request, 'user_registration/registration_form.html', {'form': form})