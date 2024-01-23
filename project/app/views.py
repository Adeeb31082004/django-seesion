# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app/home.html')
def about(request):
    return render(request,'app/about.html')
def registration(request):
    return render(request,'app/registration.html')
def login(request):
    return render(request,'app/login.html')
def dash(request):
    return render(request,'app/dash.html')

def Savedata(request):
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']
    password = request.POST['password']
    confirmpassword= request.POST['cpassword']

    request.session['fname']=firstname
    request.session['lname']=lastname
    request.session['email']=email
    request.session['contact']=contact
    request.session['password']=password
    request.session['cpassword']=confirmpassword
    return render(request,'app/login.html')

    # response=render(request,'app/login.html')
    # response.set_cookie('firstname',firstname)
    # response.set_cookie('lastname',lastname)
    # response.set_cookie('email',email)
    # response.set_cookie('contact',contact)
    # response.set_cookie('password',password)
    # response.set_cookie('cpassword',confirmpassword)
    # return response

def LoginPage(request):

    # email=request.POST['email']
    # password=request.POST['password']

    # email_id=request.COOKIES['email']
    # pwd=request.COOKIES['password']

    email_id=request.session['email']
    pwd=request.session['password']
    email=request.session['email']
    password=request.session['password']

    if(email_id==email and pwd==password):
        name=request.session['fname']
        adeeb=request.session['lname']
        
        return render(request,'app/dash.html',{"data":name,"ad":adeeb})
def delete(request):
    del request.session['fname']
    del request.session['lname']
    del request.session['email']
    del request.session['contact']
    del request.session['password']
    del request.session['cpassword']
    return render(request,'app/home.html')
def get(request):
    if 'name' in request.session:
        request.session.modified=True
        return render(request,'home.html',{"data": __name__})
    

    
