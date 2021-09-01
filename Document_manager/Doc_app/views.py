from django.http import request
from Doc_app.models import Document
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.conf import settings
from . forms import DocumentForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils import timezone

        
@login_required
def save(request):
    """
    this function will save document given by user
    """
    breakpoint()
    form = DocumentForm(request.POST, request.FILES)
    if request.method == 'POST':
        if request.user.is_authenticated:
            """"
            if xyz > 52345:
                message.error(request, "Size > 5mb")
                redirect('save')
            """
            user=request.user.id
            print(user)
            user_obj=User.objects.get(pk=user)
            print(user_obj)
            pdf_per_day_limit=Document.objects.filter(user=user_obj.pk).filter(uploaded_at__date=timezone.now()).count()
            print(pdf_per_day_limit)
            # breakpoint()
            if request.FILES['document'].size > 5242880:
                messages.info(request,"you have reached the daily limit wait unitill 12 pm to upload more")
                return redirect('log')
            else:    
                if form.is_valid():
                    
                    new_doc=Document.objects.create(
                        user_id=user,
                        description=form.cleaned_data['description'],
                        document=form.cleaned_data['document'],
                    )
                    new_doc.save()
                    messages.success(request, 'Document Uploaded Successfully')
                    return redirect('log')
                
    else:
        form = DocumentForm()
    return render(request, 'Doc_app/upload.html', {
        'form': form
    })


def index(request):
    """
    this function will render login page
    """
    form=DocumentForm
    return render(request, 'Doc_app/login.html')


@login_required
def log(request):
    """
    this function will render upload page to user
    """
    form=DocumentForm
    doc=Document.objects.all()
    
    if request.user.is_authenticated:
            user=request.user.id
            user_obj=User.objects.get(pk=user)
            print(user_obj)
            pdf_list=Document.objects.all().filter(user=user_obj.pk)
            print(pdf_list)
            return render(request, 'Doc_app/upload.html',{'form':form,'context':doc,'pdf_list':pdf_list})

def login(request):
    """
    this function will validate wether the user is valid or not
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('log')
        else:
            messages.error(request,'Invalid Credantials')
            return redirect('log')
    else:
        return render(request,'Doc_app/login.html')
    

def report(request):
	"""
	function to generate report of documents
	and sort by name, date, year, month
	"""
	user_docs = Document.objects.filter(user=User.objects.get(username=request.user.username))
	# breakpoint()
	daily_uploads = user_docs.filter(uploaded_at__day=timezone.now().strftime("%d"))
	monthly_uploads = user_docs.filter(uploaded_at__month=timezone.now().strftime("%m"))
	yearly_uploads = user_docs.filter(uploaded_at__year=timezone.now().strftime("%Y"))

	daily_count = daily_uploads.count()
	monthly_count = monthly_uploads.count()
	yearly_count = yearly_uploads.count()
	# breakpoint()

	if 'description' in request.GET:
		pdf_list = user_docs.filter(description__icontains=request.GET['description'])
	elif 'month' in request.GET:
		pdf_list = user_docs.filter(uploaded_at__month=request.GET['month'])
		# breakpoint()
	elif 'year' in request.GET:
		pdf_list = user_docs.filter(uploaded_at__year=request.GET['year'])
	elif 'from' in request.GET and 'to' in request.GET:
		# breakpoint()
		pdf_list = user_docs.filter(uploaded_at__range=[request.GET['from'],request.GET['to']])

	else:
		pdf_list = user_docs
	context = {'daily_count': daily_count, 'monthly_count': monthly_count, 'yearly_count': yearly_count, 'pdf_list':pdf_list}

	return render(request, 'Doc_app/report.html', context)


@login_required
def logout(request):
    """
    this function will logout user
    """
    auth.logout(request)
    messages.success(request,'You have been logout!!')
    return redirect("index")


@login_required
def list_doc(requset):
    """
    filtering work will be done here
    """
    if request.method == 'GET':
        if request.user.is_authenticated:
            user=request.user.id
            user_obj=User.objects.get(pk=user)
            print(user_obj)
            pdf_list=Document.objects.all().filter(user=user_obj.pk)
            return render(request,'Doc_app/upload.html',{'pdf_list':pdf_list})