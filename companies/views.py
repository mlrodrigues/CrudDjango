from django.shortcuts import render, redirect
from .models import Companies
from .forms import companiesForms


def listCompanies(request):
	companies = Companies.objects.raw(
		'SELECT u.id, u.email, u.password, u.created_at, c.name, c.created_at, c.locale, c.lang FROM companies_companies as c LEFT JOIN users_users as u')
	return render(request, 'companies-list.html', {'companies': companies})

def listCompaniesUsers(request, id):
	companiesUsers = Companies.objects.raw(
		'SELECT users.email, comp.name FROM companies_companies_users as ccu INNER JOIN companies_companies as comp ON comp.id = ccu.companies_id INNER JOIN users_users as users ON users.id = ccu.users_id WHERE ccu.companies_id = ' + id)
	return render(request, 'company-list-html', {'company': companiesUsers})

def createCompanies(request):
    form = companiesForms(request.POST or None)

    if(form.is_valid()):
        form.save()
        return redirect('listCompanies')

    return render(request, 'companies-form.html', {'form': form})


def updateCompanies(request, id):
    company = Companies.objects.get(id=id)
    form = companiesForms(request.POST or None, instance=company)

    if(form.is_valid()):
        form.save()
        return redirect('listCompanies')

    return render(request, 	'users-form.html', {'form': form, 'company': company})


def deleteCompanies(request, id):
    company = Companies.objects.get(id=id)

    if request.method == 'POST':
        company.delete()
        return redirect('listCompanies')

    return render(request, 'company-delete-confirm.html', {'company': company})
