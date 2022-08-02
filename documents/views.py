from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from documents.forms import DocFileForm
from documents.models import DocFile
from django.contrib.auth.decorators import login_required
from django.db.models import Max


def index(request):
    return HttpResponseRedirect(reverse('documents:reviews'))

@login_required
def reviews(request):
    docfiles = DocFile.objects.filter(author=request.user)
    names = []
    for docfile in docfiles:
        if not docfile.name in names:
            names.append(docfile.name)

    return render(request, "documents/index.html", {'names': names, 'docfiles': docfiles})

@login_required
def revision(request, name):
    if request.GET.get('revision'):
        version = request.GET.get('revision')
        docfileToReturn = DocFile.objects.get(author=request.user, version=version, name=name)
    else:
        version = DocFile.objects.filter(author=request.user, name=name).aggregate(Max('version'))['version__max']
        docfileToReturn = DocFile.objects.get(author=request.user, version=version, name=name)

    response = FileResponse(docfileToReturn.docfile)

    return response

@login_required
def add_docfile(request):
    data = {}
    form = DocFileForm()
    
    if request.method == "POST":
        form = DocFileForm(request.POST, request.FILES)

        if form.is_valid():
            print(form['docfile'].value())
            
            docfiles = DocFile.objects.filter(name=form['docfile'].value())
            num = 0
            for doc in docfiles:
                if doc.version >=num:
                    num = doc.version + 1
            docfileform = form.save(commit=False)
            docfileform.version = num
            docfileform.name = form['docfile'].value()
            docfileform.author = request.user
            docfileform.save()
            form.save_m2m() 
            # form.save()
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['docfile_form'] = render_to_string("documents/docfile_form.html", {'form': form}, request=request)
      
    data['docfile_form'] = render_to_string("documents/docfile_form.html", {'form': form}, request=request)
    
    return JsonResponse(data)