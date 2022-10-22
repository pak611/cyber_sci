
from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

from django.urls import include, path, re_path





urlpatterns = [
    path('', views.graph_to_df, name='graph_to_df'),
    #re_path(r'^delete_Image_Axes/<Image_Axes_id>', views.delete_Image_Axes, name='delete-Image_Axes'),
    re_path(r'^api/data/$', views.get_data, name='api-data'),
    re_path(r'^api/chart/data/$', views.ChartData.as_view(), name=''),
    re_path(r'^api/chart/data/get_csv/$', views.get_csv, name = 'get_csv'),
    ]

