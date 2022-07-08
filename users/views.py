from django.shortcuts import render, redirect
from companies.models import Companies
from docs.models import Docs
from .models import Users
from .forms import UsersForm

def listUsers(request):
	users = Users.objects.raw('SELECT u.id, u.email, u.password, u.created_at, c.name as company_name, c.created_at, c.locale, c.lang FROM users_users as u INNER JOIN companies_companies as c')
	return render(request, 'users-list.html', {'users': users})

def listInfoUsers(request, id):
	usersdocs = Docs.objects.raw('SELECT doc.id, doc.nome, doc.created_at, doc.signed, user.email FROM docs_docs as doc INNER JOIN users_users as user ON doc.user_id == user.id WHERE user.id = ' + str(id))
	companiesUsers = Companies.objects.raw(
		'SELECT users.id, users.email, comp.name FROM companies_companies_users as ccu INNER JOIN companies_companies as comp ON comp.id == ccu.companies_id INNER JOIN users_users as users ON users.id == ccu.users_id WHERE users.id = ' + str(id))

	return render(request, 'users-list-info.html', {'usersdocs': usersdocs, 'companies': companiesUsers })

def listCompaniesUsers(request, id):
	companiesUsers = Companies.objects.raw(
		'SELECT users.email, comp.name FROM companies_companies_users as ccu INNER JOIN companies_companies as comp ON comp.id == ccu.companies_id INNER JOIN users_users as users ON users.id == ccu.users_id WHERE users.id = ' + str(id))
	return render(request, 'users-list-info.html', {'companies': companiesUsers})

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

