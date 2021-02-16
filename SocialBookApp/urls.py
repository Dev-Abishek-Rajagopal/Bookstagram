'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from django.conf.urls import url

from SocialBookApp.views.views import (BookVeiwSet,UserVeiwSet,activate_User,create_User)
from SocialBookApp.views.process import (LoginCheckSet)



book = BookVeiwSet.as_view({
    'get' : 'list_Book',
    'post' : 'create_Book',
})

book_id = BookVeiwSet.as_view({
    'get' : 'get_Book',
    'put': 'update_Book',
    'delete': 'delete_Book'
})

user = UserVeiwSet.as_view({
    'get' : 'list_User',

})

user_id = UserVeiwSet.as_view({
    'get' : 'get_User',
    'put': 'update_User',
    'delete': 'delete_User'
})




login = LoginCheckSet.as_view({
    'post' : 'login',

})

urlpatterns = [
    url(r'^book/$', book),
    url(r'^book/(?P<pk>\d+)/$', book_id),

    url(r'^book/login/$', login),

    url(r'^user/$', user),
    url(r'^user/(?P<pk>\d+)/$', user_id),
    url(r'^activate_user/$', activate_User),
    url(r'^create_user/$', create_User),

]