from django.shortcuts import render, redirect
from companies.models import Companies
from docs.models import Docs
from .models import Users
from .forms import UsersForm

def listUsers(request):
	users = Users.objects.raw('SELECT u.id, u.email, u.password, u.created_at, c.name as company_name, c.created_at, c.locale, c.lang FROM users_users as u INNER JOIN companies_companies as c')
	return render(request, 'users-list.html', {'users': users})

def listDocsUsers(request, id):
	usersdocs = Docs.objects.raw('SELECT doc.nome, doc.created_at, doc.signed, comp.name FROM docs_docs as doc INNER JOIN companies_companies as comp WHERE doc.id = ' + id)
	return render(request, 'users-list.html', {'usersdocs': usersdocs})

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

