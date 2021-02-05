'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from django.conf.urls import url

from SocialBookApp.views.views import (BookVeiwSet)
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

login = LoginCheckSet.as_view({
    'post' : 'login',

})

urlpatterns = [
    url(r'^book/$', book),
    url(r'^book/(?P<pk>\d+)/$', book_id),
    url(r'^book/login/$', login),
]