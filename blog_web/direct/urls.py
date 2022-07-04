from django.urls import path
from direct.views import Inbox, UserSearch, NewConversation, SendDirect
urlpatterns = [
   	path('', Inbox, name='inbox'),
   	path('new/', UserSearch, name='usersearch'),
   	path('new/<username>', NewConversation, name='newconversation'),
   	path('send/', SendDirect, name='send_direct'),

]