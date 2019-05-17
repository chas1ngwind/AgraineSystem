from Seed.models import RoleInfo, DetailInfo
# from Seed.models import RoleInfo, SeedInfo, GenerationInfo, DetailInfo
# Create your views here.
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from Seed import models
from django import forms

# def generationlist(request, RoleInfo_id, SeedInfo_id):
#
# #def generationlist(request, SeedInfo_id):
#
#     #role = RoleInfo.objects.get(id=RoleInfo)
#     type = SeedInfo.objects.get(id=SeedInfo_id)
#     generation= GenerationInfo.objects.filter(selectRole=role，selectType=type)
#
#     #type1= SeedInfo.objects
#     #type1 = SeedInfo.objects.get(id=SeedInfo_id)
#     #role1 = SeedInfo.objects.get(id=RoleInfo_id)
#     generation_list = generation.generationinfo_set.all()
#
#     context = {
#         'generation_list': generation_list,
#
#     }
#
#     return render(request, 'Seed/generationlist.html', context)
#
#
#
# def seedlist(request, RoleInfo_id):
#
#     # get role_id
#
#     # query the selected role
#
#     role = RoleInfo.objects.get(id=RoleInfo_id)
#
#     # check the selected role
#     seed_list = role.seedinfo_set.all()
#
#     context = {
#         'seed_list': seed_list
#     }
#
#     return render(request, 'Seed/seedlist.html', context)
#
#
# def rolelist(request):
#
#     #provide role information
#
#     #sql all role information
#
#     role_list = RoleInfo.objects.all()
#     context = {
#         'role_list': role_list
#     }
#
#     return render(request, 'Seed/rolelist.html', context)
#
# def info(request):
#
#
#
#     #do not using template
#     #return HttpResponse ('test')
#
#     #using templates
#     #return render(request, 'Seed/info.html')
#
#     #context
#
#     Context = {
#         'info' :'seed'
#     }
#
#     return render(request,'Seed/info.html',Context)


def rolelist(request):

    #provide role information

    #sql all role information

    role_list = RoleInfo.objects.all()
    context = {
        'role_list': role_list
    }

    return render(request, 'Seed/rolelist.html', context)

def detaillist(request, RoleInfo_id):

    # get role_id

    # query the selected role

    role = RoleInfo.objects.get(id=RoleInfo_id)

    # check the selected role
    detail_list = role.detailinfo_set.all()

    context = {
        'detail_list': detail_list
    }

    return render(request, 'Seed/detailIist.html', context)


# class UserForm(forms.Form):
#     name = forms.CharField()
#
# def register(req):
#     if req.method =='POST':
#         form = UserForm(req.POST)
#         if form.is_valid():
#             print (form.cleaned.data)
#             return HttpResponse('ok')
#     else :
#         form = UserForm()
#     return render_to_response('register.html', {'form':form})

# class MyForm(forms.Form):
#     amount = forms.IntegerField(null=True)
#     type = forms.CharField(max_length=10)
#     generation = forms.CharField(max_length=10)
#     role = forms.CharField(max_length=10)
# def reg2(request):
#     errors_obj = " "
#     if request.method == "POST":
#         form_post = MyForm(request.POST)
#         if form_post.is_valid():
#             print("data", form_post.cleaned_data)
#         else:errors_obj = form_post.errors
#     form_obj = MyForm()
#     return render(request, "reg2.html", {"form_obj": form_obj, "errors_obj": errors_obj})


# def addinfo(request, RoleInfo_id):
def addinfo(request, RoleInfo_id):
    if request.method == "GET":
        return render(request, 'Seed/addinfo.html')
    elif request.method == 'POST':
        #d=DetailInfo()
        #d=DetailInfo(amount=request.POST.get['amount'],type = request.POST.get['type'],generation = request.POST.get['generation'] )
        # amount = request.POST.get('amount')
        # models.DetailInfo.objects.create(amount=amount)
        # type = request.POST.get('type')
        # models.DetailInfo.objects.create(type=type)
        # generation = request.POST.get('generation')
        # generation .DetailInfo.objects.create(generation =generation)
        # return redirect("detail.html")
        # amount = request.POST.get('amount')
        #
        # type = request.POST.get('type')
        #
        # generation = request.POST.get('generation')
        # role = request.POST.get('role')
        # info={"amount": amount,"type":type, "generation":generation,"role":role}
        # models.DetailInfo.objects.create(**info)
        #
        # # models.DetailInfo.objects.create(amount=d.amount, type=d.type, generation=d.generation)
        # info_list=models.DetailInfo.objects.all()
        # #d.save()
        # return render(request, 'Seed/detaillist.html', {"info_list":info_list})

        amount = request.POST['amount']
        type = request.POST['type']
        generation = request.POST['generation']
        contactnumber = request.POST['contactnumber']
        name = request.POST['name']
        role = request.POST['role']
        models.RoleInfo.objects.create(role=role)
        models.DetailInfo.objects.create(amount=amount, type=type, generation=generation,contactnumber=contactnumber,name=name)

        role1 = RoleInfo.objects.get(id=RoleInfo_id)
        detail_list = role1.detailinfo_set.all()
        context = {
            'amount': amount, 'type': type, 'generation': generation, 'detail_list': detail_list, 'role': role, 'name': name, 'contactnumber':contactnumber

        }
        return render(request, 'Seed/postTest2.html', context)

def postTest2(request, RoleInfo_id):
    amount = request.POST['amount']
    type = request.POST['type']
    generation = request.POST['generation']
    role = request.POST['role']
    contactnumber = request.POST['contactnumber']
    name = request.POST['name']
    role1=models.RoleInfo.objects.create(role=role)
    models.DetailInfo.objects.create(amount=amount, type=type, generation=generation,role=role1,contactnumber=contactnumber,name=name)

    role1 = RoleInfo.objects.get(id=RoleInfo_id)
    detail_list = role1.detailinfo_set.all()
    context = {
        'amount': amount, 'type': type, 'generation': generation, 'detail_list': detail_list, 'role': role,'name': name, 'contactnumber':contactnumber

    }
    return render(request, 'Seed/postTest2.html', context)

def delinfo(request, RoleInfo_id):
    nid = request.GET.get('nid')
    models.DetailInfo.objects.filter(id=nid).delete()
    return redirect('Seed/detaillist.html')


def editinfo(request, RoleInfo_id):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.DetailInfo.objects.filter(id=nid).first()
        return render(request, 'editinfo.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        amount = request.POST.get('amount')
        models.DetailInfo.objects.filter(id=nid).update(amount=amount)
        return redirect('Seed/detaillist.html')