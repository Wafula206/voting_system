from django.urls import path
from .views import vote, vote_success  

urlpatterns = [
    path("", vote, name="home"),  # Homepage loads the voting page
    path("vote/", vote, name="vote"),  
    path("vote/success/", vote_success, name="vote_success"),
]
