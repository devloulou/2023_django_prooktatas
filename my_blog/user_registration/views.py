from django.shortcuts import render
from .forms import UserRegisterForm

# Create your views here.
def register(request):   
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print("megnyomtam a Sign Up gombot :D")
        # továbbo validációs lépések
    else:
        # amikor megnyitom a register oldalt, hogy generálja ki az üres form-ot
        form = UserRegisterForm()

    return render(request, 'user_registration/registration_form.html', {'form': form})