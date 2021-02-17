'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from django.conf.urls import url

from SocialBookApp.views.views import (BookVeiwSet,UserVeiwSet,activate_User,create_User,friendlistVeiwSet,profileTXTPostVeiwSet,TXTPostCommentsVeiwSet)
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

friend = friendlistVeiwSet.as_view({
    'post' : 'create_relationship',
     'get' : 'get_allUsers'
})

friendprofile = friendlistVeiwSet.as_view({

     'get' : 'get_profile'
})

friendtype = friendlistVeiwSet.as_view({

     'get' : 'get_allUserstype'
})

friend_id = friendlistVeiwSet.as_view({
    'put' : 'update_relationship',
                        #change friendship status
    'get' : 'get_friendlist'
})

notfriend_id = friendlistVeiwSet.as_view({

    'get' : 'get_notfriendlist'
                         #pending friend request sent by user
})

addfriend_id = friendlistVeiwSet.as_view({

    'get': 'get_acceptfriendlist'
})
                            #pending request to accept friend
unfriend_id = friendlistVeiwSet.as_view({

    'get': 'Unfriend'
})

listfriend_id = friendlistVeiwSet.as_view({

    'get': 'list_friendlist'
})

login = LoginCheckSet.as_view({
    'post' : 'login',

})

txtpost = profileTXTPostVeiwSet.as_view({

    'post' : 'create_profileTXTPost',

})

txtpostchange = profileTXTPostVeiwSet.as_view({

    'put': 'update_Post',
    'delete': 'delete_Post',

})

txtpostbyuser = profileTXTPostVeiwSet.as_view({

    'get': 'list_profile_post',
})

txtposthomuser = profileTXTPostVeiwSet.as_view({

    'get': 'list_home_post',
})

postcomment_id = TXTPostCommentsVeiwSet.as_view({
    'get' : 'get_TXTPostComments',
    'put': 'update_TXTPostComments',
    'delete': 'delete_TXTPostComments'
})

postcomment = TXTPostCommentsVeiwSet.as_view({
    'get' : 'list_TXTPostComments',
    'post' : 'create_TXTPostComments',

})


urlpatterns = [
    url(r'^book/$', book),
    url(r'^book/(?P<pk>\d+)/$', book_id),

    url(r'^book/login/$', login),

    url(r'^user/$', user),
    url(r'^user/(?P<pk>\d+)/$', user_id),

    url(r'^activate_user/$', activate_User),
    url(r'^create_user/$', create_User),

    url(r'^friend/$', friend),
    url(r'^friendlist/(?P<pk>\d+)/$', friend_id),
    url(r'^notfriend/(?P<pk>\d+)/$', notfriend_id),
    url(r'^acceptfriend/(?P<pk>\d+)/$', addfriend_id),
    url(r'^unfriend/(?P<pk>\d+)/$', unfriend_id),
    url(r'^listfriend/$', listfriend_id),
    url(r'^usertype/$', friendtype),
    url(r'^profile/$', friendprofile),

    url(r'^txtpost/$', txtpost),
    url(r'^txtpostchange/(?P<pk>\d+)/$', txtpostchange),
    url(r'^txtpostbyuser/$', txtpostbyuser),
    url(r'^txtposthomuser/$', txtposthomuser),

    url(r'^postcomment/$', postcomment),
    url(r'^postcomment/(?P<pk>\d+)/$', postcomment_id),
]