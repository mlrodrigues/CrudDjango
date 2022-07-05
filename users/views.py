from django.shortcuts import render, redirect
from .models import Users
from .forms import UsersForm

def listUsers(request):
	users = Users.objects.all()
	return render(request, 'users-list.html', {'users': users})

def createUsers(request):
	form = UsersForm(request.POST or None)

	if(form.is_valid()):
		form.save()
		return redirect('listUsers')

	return render(request, 'users-form.html', {'form': form})

def updateUsers(request, id):
	user = Users.objects.get(id=id)
	form = UsersForm(request.POST or None, instance=user)

	if(form.is_valid()):
		form.save()
		return redirect('listUsers')
	
	return render(request, 'users-form.html', {'form': form, 'user': user})

def deleteUsers(request, id):
    user = Users.objects.get(id=id)

    if request.method == 'POST':
        user.delete()
        return redirect('listUsers')

    return render(request, 'user-delete-confirm.html', {'user': user})
