from __future__ import unicode_literals

from django.conf import settings
from django.urls import include, path, re_path
from rest_framework import routers
from tastypie.api import Api

from ldb import viewsets
from ldb.export import ExportResource
from ldb.views import PersonDetailView, PersonDeleteView, OrganizationDetailView, OrganizationDeleteView, \
    PersonEditView, OrganizationEditView, ResultsView, CommitteeMembershipFilterView, IndexView, ExportView

api = Api(api_name='v2')
api.register(ExportResource())

router = routers.DefaultRouter()
router.register(r'people', viewsets.PersonViewSet)
router.register(r'organizations', viewsets.OrganizationsViewSet)

urlpatterns = [
    path('api/', include(api.urls), name='ldb_old_api'),

    path('api/v3/', include(router.urls)),
    # url(r'^api/v3/api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    path('index/', IndexView.as_view(), name='ldb_index'),

    path('people/search/', ResultsView.as_view(), name='ldb_people_search'),

    re_path(r'^people/(?P<pk>\d+)/$', PersonDetailView.as_view(), name='ldb_people_detail'),
    re_path(r'^people/(?P<pk>\d+)/delete/$', PersonDeleteView.as_view(), name='ldb_people_delete'),
    re_path(r'^people/(?P<pk>\d+)/edit/$', PersonEditView.as_view()),
    path('people/create/', PersonEditView.as_view(), name='ldb_people_create'),

    re_path(r'^organizations/(?P<pk>\d+)/$', OrganizationDetailView.as_view(),
         name='ldb_organizations_detail'),
    re_path(r'^organizations/(?P<pk>\d+)/delete/$', OrganizationDeleteView.as_view(),
         name='ldb_organizations_delete'),
    re_path(r'^organizations/(?P<pk>\d+)/edit/$', OrganizationEditView.as_view()),
    path('organizations/create/', OrganizationEditView.as_view(), name='ldb_organizations_create'),
    path('committees/', CommitteeMembershipFilterView.as_view(), name='ldb_committees'),

    path('export/', ExportView.as_view(), name="ldb_export"),
]
