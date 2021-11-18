from django.shortcuts import redirect, render, get_object_or_404

from UpWithS3.forms import upload_form
from UpWithS3.models import upload

def index(request):
    form=upload_form
    return render(request,'index.html',{'form':form})

def makeupload(request):
    foto_receita=request.FILES['foto_receita']
    receita=upload.objects.create(foto_receita=foto_receita)   
    receita.save()
    return redirect('showupload')

def showupload(request):
    foto= get_object_or_404(upload, pk='36')
    return render(request,'show.html',{'foto':foto})

     
       
   