from django.conf.urls import url

#from Seed.views import info, rolelist, seedlist, generationlist

from Seed.views import rolelist, detaillist, addinfo, delinfo, editinfo, postTest2
# from Seed.views import rolelist, detaillist, register,reg2

urlpatterns = [
    #
    # url(r'^info/$', info),
    #
    # #http://127.0.0.1:8888/rolelist/
    # url(r'^rolelist/$', rolelist),
    #
    # #http://127.0.0.1:8888/1/
    # url(r'^(\d)+/$', seedlist),
    #
    # #http://127.0.0.1:8888/1/1/
    # url(r'^(\d+)/(\d)+/$', generationlist)



    url(r'^$', rolelist),
    url(r'^(?P<RoleInfo_id>\d+)/$', detaillist),
#(\d+)/
    url(r'^(\d+)/addinfo/$', addinfo),
    url(r'^(\d+)/addinfo/postTest2/$', postTest2),
    url(r'^(\d+)/delinfo/$', delinfo),
    url(r'^(\d+)/editinfo/$', editinfo),
    url(r'^(\d+)/editinfo/editinfo/$', detaillist),





]
