'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from django.contrib import admin


from SocialBookApp.models.bookmodels import (Book,TextBook,BookComments,OwnBook)
from SocialBookApp.models.usermodels import (App_User,friendlist,profileComment,profileTXTPost,TXTPostComments)

admin.site.register(Book)
admin.site.register(TextBook)
admin.site.register(BookComments)
admin.site.register(OwnBook)
admin.site.register(App_User)
admin.site.register(friendlist)
admin.site.register(profileComment)
admin.site.register(profileTXTPost)
admin.site.register(TXTPostComments)
