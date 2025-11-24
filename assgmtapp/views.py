from django.shortcuts import render,redirect
from .forms import AddForm
from .models import crud
from django.contrib.auth import authenticate ,login as log,logout

# Create your views here.

def home(request):
    return render(request,"home.html")

def register(request):
    form = AddForm()
    if request.method =="POST":
        form = AddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,"reg.html",{'form':form})

def login(request):
    return render(request,"login.html")

def userlog(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        cr = crud.objects.filter(username=username,password=password)
        if cr:
            user_details = crud.objects.get(username=username,password=password)
            id=user_details.id
            name=user_details.name

            request.session['id']=id
            request.session['name']=name
            return redirect('logindetail')
        else:
            return render(request,'login.html',{'error':'Incorrect Username or Password'})       
    else:
        return render(request,'home.html')
    
def logindetail(request):
    id = request.session['id']
    name = request.session['name']
    return render(request,"logindetail.html",{'id':id,'name':name})


def userlogout(request):
    logout(request)
    return redirect('login')

def view(request):
    cr = crud.objects.all()
    return render(request,"view.html",{'cm':cr})

def update(request,pk):
    cr = crud.objects.get(id = pk)
    form = AddForm(instance = cr)
    if request.method == "POST":
        form = AddForm(request.POST,instance = cr)
        if form.is_valid:
            form.save()
            return redirect("view")
    return render(request,"update.html",{'form':form}) 

def delete(request,pk):
    cr = crud.objects.get(id = pk)
    cr.delete()
    return redirect("view")

def detailview(request,pk):
    cr = crud.objects.get(id=pk)
    return render(request,"detailview.html",{'cm':cr})