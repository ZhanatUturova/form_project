from django.urls import path
from . import views
urlpatterns = [
    path('', views.FeedBackView.as_view()),
    path('done', views.DoneView.as_view()),
    path('detail/<int:pk>', views.DetailFeedBack.as_view(), name='feedback-detail'),
    path('update/<int:pk>', views.FeedBackViewUpdate.as_view()),
    path('list', views.ListFeedBack.as_view()),
    # path('<int:id_feedback>', views.FeedBackUpdateView.as_view()),
]