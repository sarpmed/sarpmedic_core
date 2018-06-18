from django.shortcuts import render

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        # return render(request, ACTIVE_APP+'/dashboard.html')
        #return redirect('create-product')
        pass


    # contact_form = ContactForm()
    # context = {'contact_form': contact_form}

    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about_us.html')


def screen(request):
    return render(request, 'core/screening.html')


def contact(request):
    return render(request, 'core/contact.html')

#
# def contact(request):
#     return render(request, 'core/index.html')
