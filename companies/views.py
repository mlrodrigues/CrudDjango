from django.shortcuts import render, redirect
from .models import Companies
from .forms import companiesForms

def listCompanies(request):
	companies = Companies.objects.all()
	return render(request, 'companies-list.html', {'companies': companies})

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
