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

    return render(request, 'Seed/detaillist.html', context)


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
        amount = request.POST.get('amount')
        #models.DetailInfo.objects.create(amount=amount)
        type = request.POST.get('type')
        #models.DetailInfo.objects.create(type=type)
        generation = request.POST.get('generation')
        models.DetailInfo.objects.create(amount=amount, type=type, generation=generation)
        #dic = {'amount':amount, 'type':type, 'generation':generation}
        #models.DetailInfo.objects.create(**dic)
        #detaillist = models.DetailInfo.objects.all()
        #return redirect("detail.html")
        #return render(request, 'Seed/detailinfo.html')
        return render(request, 'Seed/detaillist.html')

def postTest2(request, RoleInfo_id):
    role = RoleInfo.objects.get(id=RoleInfo_id)
    amount = request.POST['amount']
    type = request.POST['type']
    generation = request.POST['generation']
    #dic = {'amount':amount, 'type':type, 'generation':generation}
    #models.DetailInfo.objects.create(**dic)
    context={
        'amount': amount, 'type': type, 'generation':generation
    }
    detail_list = role.detailinfo_set.all()
    role.detailinfo_set.create(amount=amount, type=type, generation=generation)
    #models.DetailInfo.objects.create(amount=amount, type=type, generation=generation)
    #detaillist = models.DetailInfo.objects.all()
    return render(request, 'Seed/detaillist.html',{'detail_list':detail_list})

def delinfo(request, RoleInfo_id):
    role = RoleInfo.objects.get(id=RoleInfo_id)
    nid = request.GET.get('nid')
    role.detailinfo_set.filter(id=nid).delete()
    return render(request, 'Seed/delinfo.html')


def editinfo(request, RoleInfo_id):
    role = RoleInfo.objects.get(id=RoleInfo_id)
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = role.detailinfo_set.filter(id=nid)
        return render(request, 'Seed/editinfo.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        amount = request.POST['amount']
        type = request.POST['type']
        generation = request.POST['generation']
        obj = role.detailinfo_set.filter(id=nid)
        role.detailinfo_set.filter(id=nid).update(amount=amount, type=type, generation=generation)
        return render(request, 'Seed/detaillist.html')
