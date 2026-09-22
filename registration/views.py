from django.shortcuts import render, redirect

# Create your views here.


from .forms import RegistrationForm


def register(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():

            person = form.save()

            return render(
                request,
                'registration/success.html',
                {
                    'person': person
                }
            )

    else:

        form = RegistrationForm()

    return render(
        request,
        'registration/register.html',
        {
            'form': form
        }
    )