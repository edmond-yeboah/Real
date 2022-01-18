from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('register/',views.register, name="register"),
    path('login/',views.login, name="login"),
    path('profile/',views.profile, name="profile"),
    path('logout/',views.logoutUser),
    path('addlisting/',views.addlisting, name="addlisting"),
    path('mylisting/',views.mylisting, name="mylisting"),
    path('deletelisting/',views.deletelisting, name="delete_listing"),
    path('editlisting/',views.editlisting, name="edit_listing"),
    path('listing/',views.listings, name="listing"),
    path('single_listing/',views.singlelisting, name="single_listing"),
    path('compare_listing/',views.comparelisting, name="compare_listing"),
    path('bookmark_list/',views.bookmarklist, name="bookmark_list"),
    path('messages/',views.messages, name="messages"),
    path('accra/',views.accra, name="accra"),
    path('ashanti/',views.ashanti, name="ashanti"),
    path('central/',views.central, name="central"),
    path('eastern/',views.eastern, name="eastern"),
    path('volta/',views.volta, name="volta"),
    path('western/',views.western, name="western"),
    path('uppereast/',views.uppereast, name="uppereast"),
    path('upperwest/',views.upperwest, name="upperwest"),
    path('compare_region/',views.CompareRegion, name="region_compare"),
    path('search_results/',views.SearchResults, name="search_results"),
    path('locations_template/',views.LocationTemplate, name="locations"),
    path('schools_template/',views.SchoolsTemplate, name="schools"),
    path('industry_template/',views.IndustryTemplate, name="industry"),
]

# ADDED TO HELP US FETCH ALL PICTURES
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)