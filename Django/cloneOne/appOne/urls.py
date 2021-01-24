from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view(),name='post_delete'),
    url(r'^drafts/$',views.PostDraftListView.as_view(),name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish$',views.post_publish,name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comments_to_post,name='add_comment_to_post'),
    url(r'^comments/(?P<pk>\d+)/approve/$',views.comment_approved,name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.comment_publish,name='comment_publish'),
]
