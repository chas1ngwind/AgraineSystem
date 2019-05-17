from ..models import RoleInfo, DetailInfo
# from Seed.models import RoleInfo, SeedInfo, GenerationInfo, DetailInfo
# Create your views here.
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect


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

    return render(request, 'rolelist.html', context)