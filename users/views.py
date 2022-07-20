#This file manages the front-end of the website, we can create our own front-end and then pass it down to functions that will render the docFile sent to them while the correct router has been chosen
#The input to the render function is the path to out html template that we created in our templtes folder which contains the folder of same name as the app(convention)

   
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):                                                      #renders the register page of our website
    if request.method == 'POST':                                            #if the request generated in the form was POST then enters this if 
        form = UserRegisterForm(request.POST)                               #creater a new form with the same data as recieved from the form                      
        if form.is_valid():                                                 #checks if the form is valid, enters if valid, valid-strong password, no same username
            form.save()                                                     #saves the user, adds to the users table, database
            username = form.cleaned_data.get('username')                    
            messages.success(request, f'Account created for {username}')    #flash message for the user on success
            return redirect('login')
    else:
        form = UserRegisterForm()                                           #here we are using a modified form, made from a form inhereted from django which can be used to take user Registration details and save them to the database
    
    return render(request, 'users/register.html', {'form':form})            #we return the rendered html doc here which is rendered by the render function, takes up request as the first argument and the location to the template containing the html as second, next you can pass on some extra info as a dictionary to the html doc 

@login_required
def profile(request):
    if request.method == 'POST': 
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' :  p_form
    }

    return render(request, 'users/profile.html', context)