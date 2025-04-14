@login_required(login_url="login")
def about(request):
    return render(request, 'about.html')