from django.shortcuts import render, redirect
from .models import Docs
from .forms import docsForms

def listDocs(request):
	docs = Docs.objects.all()
	return render(request, 'docs-list.html', {'docs': docs})

def createDocs(request):
	form = docsForms(request.POST or None)

	if(form.is_valid()):
		form.save()
		return redirect('listDocs')

	return render(request, 'docs-form.html', {'form': form})

def updateDocs(request, id):
	doc = Docs.objects.get(id=id)
	form = docsForms(request.POST or None, instance=doc)

	if(form.is_valid()):
		form.save()
		return redirect('listDocs')
	
	return render(request, 	'users-form.html', {'form': form, 'doc': doc})

def deleteDocs(request, id):
    doc = Docs.objects.get(id=id)

    if request.method == 'POST':
        doc.delete()
        return redirect('listDocs')

    return render(request, 'doc-delete-confirm.html', {'doc': doc})
