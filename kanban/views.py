from django.shortcuts import render
def index(request):
    return render(request, "kanban/index.html")
    
def home(request):
    return render(request, "kanban/home.html")
    

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("kanban:home")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'kanban/signup.html', context)