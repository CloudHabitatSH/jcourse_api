from django.urls import include, path
from rest_framework.routers import DefaultRouter

from jcourse_api.views import *

router = DefaultRouter()
router.register('course', CourseViewSet, basename='course')
router.register('review', ReviewViewSet, basename='review')
router.register('semester', SemesterViewSet, basename='semester')
router.register('course-in-review', CourseInReviewViewSet, basename='course-in-review')
router.register('notice', NoticeViewSet, basename='notice')
router.register('search', SearchViewSet, basename='search')
router.register('lesson', EnrollCourseViewSet, basename='lesson')

urlpatterns = [
    path('', include(router.urls)),
    path('me/', UserView.as_view(), name='me'),
    path('filter/', FilterView.as_view(), name='filter'),
    path('statistic/', StatisticView.as_view(), name='statistic'),
    path('report/', ReportView.as_view(), name='report'),
    path('user-summary/', user_summary, name='user-summary'),
    path('sync-lessons/<str:term>/', sync_lessons, name='sync-lessons'),
    path('sync-lessons/', sync_lessons, name='sync-lessons'),
]
