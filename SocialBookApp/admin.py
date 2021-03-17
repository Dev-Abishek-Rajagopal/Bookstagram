'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from django.contrib import admin
from treenode.admin import TreeNodeModelAdmin
from treenode.forms import TreeNodeForm

from SocialBookApp.models.bookmodels import (Book,TextBook,BookComments,OwnBook,BookWishlist,BookUserTree,BookTreeDB,BookTreeConnect,BookNewsFeed,FriendNewsFeed,CommentsNewsFeed)
from SocialBookApp.models.usermodels import (App_User,friendlist,profileComment,profileTXTPost,TXTPostComments)

admin.site.register(Book)
admin.site.register(TextBook)
admin.site.register(BookComments)
admin.site.register(OwnBook)
admin.site.register(BookWishlist)
admin.site.register(App_User)
admin.site.register(friendlist)
admin.site.register(profileComment)
admin.site.register(profileTXTPost)
admin.site.register(TXTPostComments)
admin.site.register(BookTreeDB)
admin.site.register(BookTreeConnect)
admin.site.register(BookNewsFeed)
admin.site.register(FriendNewsFeed)
admin.site.register(CommentsNewsFeed)
class BookUserTreeAdmin(TreeNodeModelAdmin):

    # set the changelist display mode: 'accordion', 'breadcrumbs' or 'indentation' (default)
    # when changelist results are filtered by a querystring,
    # 'breadcrumbs' mode will be used (to preserve data display integrity)
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_BREADCRUMBS
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_INDENTATION

    # use TreeNodeForm to automatically exclude invalid parent choices
    form = TreeNodeForm

admin.site.register(BookUserTree, BookUserTreeAdmin)
