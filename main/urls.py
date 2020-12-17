from django.urls import path, include
from main.views import (
        homeView,
        addUserView,
        referUserView,
        countReferalsView,
        getRefererView,
        biggestInfluencerView,
    )


urlpatterns = [
    path('', homeView, name='home'),
    path('add-user', addUserView, name='add_user'),
    path('refer-user', referUserView, name='refer_user'),
    path('count-referals', countReferalsView, name='count_referals'),
    path('get-referer', getRefererView, name='get_referer'),
    path('biggest-influener', biggestInfluencerView, name='biggest_influencer')
]