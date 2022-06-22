from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

# importing Views for routing
from . import views

urlpatterns = [
    #  path(r'^$', views.apiloginview),
    # # match all other pages
    # path(r'^(?:.*)/?$', views.apiloginview),
    path("", TemplateView.as_view(template_name="index.html")),
    path("costumercollection", TemplateView.as_view(template_name="index.html")),
    path("viewcostumers", TemplateView.as_view(template_name="index.html")),
    path("updateCostumer", TemplateView.as_view(template_name="index.html")),
    path("reports", TemplateView.as_view(template_name="index.html")),
    path("Settings", TemplateView.as_view(template_name="index.html")),
    path("collectionDetails", TemplateView.as_view(template_name="index.html")),
    path("addCostumer", TemplateView.as_view(template_name="index.html")),
    path("updateCostumer", TemplateView.as_view(template_name="index.html")),
    path("addCollection", TemplateView.as_view(template_name="index.html")),
    path("planclac", TemplateView.as_view(template_name="index.html")),
    path("addPlace", TemplateView.as_view(template_name="index.html")),
    path("ccloans", TemplateView.as_view(template_name="index.html")),
    path("cclist", TemplateView.as_view(template_name="index.html")),
    # path("", views.apiloginview, name="login"),
    # path("", views.api_docs, name="api_docs"),
    # costumer Data urls
    path("getcostumer/<str:pk>/", views.getCostumer, name="getcostumer"),
    path(
        "getcostumer/<str:tk>/<str:start>/<str:end>/",
        views.getCostumerRange,
        name="getcostumerrange",
    ),
    path("createcostumer/<str:pk>/", views.createcostumer, name="createcostumer"),
    path(
        "deletecostumer/<str:pk>/<str:tk>/", views.deletecostumer, name="deletecostumer"
    ),
    path("updatecostumer/<str:pk>/", views.updatecostumer, name="updatecostumer"),
    path("costumerdetail/<str:pk>/", views.getcostumerdetail, name="costumerdetail"),
    # Collection List Data URLS
    path("createcollection/<str:tk>/", views.createcollection, name="createcollection"),
    path("getcollection/<str:tk>/", views.getcollection, name="getcollection"),
    path(
        "getcollectiondetail/<str:pk>/",
        views.getcollectiondetail,
        name="getcollectiondetail",
    ),
    path(
        "getcollectionbydate/<str:tk>/<str:pk>/",
        views.getcollectionbydate,
        name="getcollectionbydate",
    ),
    path("deletecollection/<str:pk>", views.deletecollection, name="deletecollection"),
    path("updatecollection/<str:pk>", views.updatecollection, name="updatecollection"),
    path(
        "getcostumercollectionbydate/<str:tk>/<str:pk>/<str:date>/",
        views.getCostumerCollectionbyDate,
        name="getcostumercollectionbydate",
    ),
    path(
        "getcostumercollectionlatest/<str:tk>/<str:pk>/",
        views.getcostumerlastCollection,
        name="getcostumercollectionlatest",
    ),
    # expece table data urls
    path("getexpence/", views.getExpence, name="getexpence"),
    path("getexpencedetail/", views.getExpencedetail, name="getexpencedetail"),
    path("createexpence/", views.createExpence, name="createexpence"),
    path("deleteexpence/<str:pk>", views.deleteExpence, name="deleteexpence"),
    path("updateexpence/<str:pk>", views.updateExpence, name="updateexpence"),
    path(
        "getexpence/<str:start>/<str:end>/",
        views.getExpenceRange,
        name="getexpencerange",
    ),
    # expece total table data urls
    path("getexpencetotal/", views.getExpencetotal, name="getexpencetotal"),
    path(
        "getexpencetotal/<str:start>/<str:end>/",
        views.getExpencetotalrange,
        name="getExpencetotalrange",
    ),
    path(
        "getexpencedetailtotal/<str:pk>/",
        views.getExpencedetailtotal,
        name="getexpencedetailtotal",
    ),
    path("createexpencetotal/", views.createExpencetotal, name="createexpencetotal"),
    path(
        "deleteexpencetotal/<str:pk>",
        views.deleteExpencetotal,
        name="deleteexpencetotal",
    ),
    path(
        "updateexpencetotal/<str:pk>/",
        views.updateExpencetotal,
        name="updateexpencetotal",
    ),
    # Dl ammount  table data urls
    path("getdl/", views.getDl, name="getdl"),
    path("getdl/<str:start>/<str:end>/", views.getDlrange, name="getDlrange"),
    path("getdldetail/<str:pk>/", views.getDldetail, name="getdldetail"),
    path("createdl/", views.createDl, name="createdl"),
    path("deletedl/<str:pk>/", views.deleteDl, name="deletedl"),
    path("updatedl/<str:pk>/", views.updateDl, name="updatedl"),
    # Ammount In hand  table data urls
    path("getaih", views.getaih, name="getammountinhand"),
    path("getaihdetail/<str:pk>", views.getaihdetail, name="getaihdetail"),
    path("getaihrange/<str:date>/", views.getaihrange, name="getaihrange"),
    path("createaih", views.createaih, name="createaih"),
    path("updateaih/<str:pk>", views.updateaih, name="updateaih"),
    path("getaihlatest", views.getaithlatest, name="getaihlatest"),
    # Close up  table data urls
    path("getcloseup/", views.getcloseup, name="getcloseup"),
    path(
        "getcloseuprange/<str:start>/<str:end>/",
        views.getclosedateRange,
        name="getclosedateRange",
    ),
    path("getcloseupdetail/<str:pk>", views.getcloseupdetail, name="getcloseupdetail"),
    path("createcloseup", views.createcloseup, name="createcloseup"),
    path("updatecloseup/<str:pk>", views.updatecloseup, name="updatecloseup"),
    path("deletecloseup/<str:pk>", views.deletecloseup, name="deletecloseup"),
    # Close down  table data urls
    path("getclosedown", views.getclosedown, name="getclosedown"),
    path(
        "getclosedownrange/<str:start>/<str:end>/",
        views.getclosedowndateRange,
        name="getclosedowndateRange",
    ),
    path(
        "getclosedowndetail/<str:pk>",
        views.getclosedowndetail,
        name="getclosedowndetail",
    ),
    path("createclosedown", views.createclosedown, name="createclosedown"),
    path("updateclosedown/<str:pk>", views.updateclosedown, name="updateclosedown"),
    path("deleteclosedown/<str:pk>", views.deleteclosedown, name="deleteclosedown"),
    # other Ammount in table data urls
    path("getoai", views.getoai, name="getoai"),
    path("getoai/<str:start>/<str:end>/", views.getoairange, name="getoairange"),
    path("getoaidetail/<str:pk>", views.getoaidetails, name="getoaidetail"),
    path("createoai", views.createoai, name="createoai"),
    path("updateoai/<str:pk>", views.updateoai, name="updateoai"),
    path("deleteoai/<str:pk>", views.deleteoai, name="deleteoai"),
    # Ammount other out table data urls
    path("getoao", views.getoao, name="getoao"),
    path("getoao/<str:start>/<str:end>/", views.getoaoRange, name="getoaoRange"),
    path("getoaodetail/<str:pk>", views.getoaodetails, name="getoaodetail"),
    path("createoao", views.createoao, name="createoao"),
    path("updateoao/<str:pk>", views.updateoao, name="updateoao"),
    path("deleteoao/<str:pk>", views.deleteoao, name="deleteoao"),
    # Inversment table data urls
    path("getinversment", views.getinversment, name="getinversment"),
    path(
        "getinversment/<str:start>/<str:end>/",
        views.getinversmentRange,
        name="getinversmentRange",
    ),
    path(
        "getinversmentdetail/<str:pk>",
        views.getinversmentdetails,
        name="getinversmentdetail",
    ),
    path("createinversment", views.createinversment, name="createinversment"),
    path("deleteinversment/<str:pk>", views.deleteinversment, name="deleteinversment"),
    path("updateinversment/<str:pk>", views.updateinversment, name="updateinversment"),
    # others data urls
    path("getothers", views.getothers, name="getothers"),
    path(
        "getothers/<str:start>/<str:end>/", views.getothersRange, name="getothersRange"
    ),
    path("getothersdetail/<str:pk>", views.getothersdetails, name="getothersdetail"),
    path("createothers", views.createothers, name="createothers"),
    path("updateothers/<str:pk>", views.updateothers, name="updateothers"),
    path("deleteothers/<str:pk>", views.deleteothers, name="deleteothers"),
]
