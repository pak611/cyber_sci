
from http.client import responses
#from tkinter import Image
from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm
from .forms import UploadImageForm, ConvertImageForm
from hplc_app.models import Image_Axes
from .backend_functions import get_range
from .models import Image_Axes

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render


from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from hplc_app.models import Image_Axes

from .HPLC_transform import plot_to_df

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd

import csv






# Create your views here.


def graph_to_df(request):

    alert_message = False


    if request.method == 'POST':

        
        form = UploadImageForm(request.POST, request.FILES)


        if form.is_valid():
            print('IMAGE IS VALID')
            form.save()
            obj=form.instance

            global x_max
            global y_max

            global x_min
            global y_min

            x_min = form.cleaned_data.get("x_min")
            x_max = form.cleaned_data.get("x_max")
            y_min = form.cleaned_data.get("y_min")
            y_max = form.cleaned_data.get("y_max")

            #global(filename)



            print('image name is', form.cleaned_data['image'])

            filename = form.cleaned_data['image']
            title = form.cleaned_data['title']



            global image_path

            image_path = 'media/images/' + str(filename)

            #pathname = 'media/images/'

            #image_path = pathname + str(filename)

            alert_message = {
            'status': True,
            'message': 'Successfully saved the image'
            }

            context = {
                'alert_data': alert_message,
                'form': form,
                'images': Image_Axes.objects.all
            }

            # create the instance

            ins = Image_Axes(title=title, image=filename, x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)

            ins.save()

            print('data has been written to db')

        


        else:
            alert_message = {
                'status': False,
                'message': 'Form data is invalid. Please check if your image / title is repeated'
            }

        form = UploadImageForm()
        context = {
            'alert_data': alert_message,
            'form': form,
            'images': Image_Axes.objects.all
        }

    else:

        form = UploadImageForm()


        context = {
            'form': form,
            'images': Image_Axes.objects.all
        }

    return render(request, 'hplc_page/hplc.html', context=context)


            

User = get_user_model()


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


def get_csv(request):


    pathname = 'media/'

    #filename = Image_Axes.objects.filter(image)

    field_name = 'image'
    obj = Image_Axes.objects.first()
    field_object = Image_Axes._meta.get_field(field_name)
    field_value = field_object.value_from_object(obj)


    image_path = pathname + str(field_value)

    field_name = 'x_max'
    obj = Image_Axes.objects.first()
    field_object = Image_Axes._meta.get_field(field_name)
    field_value = field_object.value_from_object(obj)


    x_max = field_value


    field_name = 'y_max'
    obj = Image_Axes.objects.first()
    field_object = Image_Axes._meta.get_field(field_name)
    field_value = field_object.value_from_object(obj)


    y_max = field_value



    out_df = plot_to_df(image_path, x_max, y_max)

    x_coords = out_df.iloc[:,1].tolist()
    y_coords = out_df.iloc[:,0].tolist()

    x_coords.reverse()
    y_coords.reverse()

    

    #print('y_coords are',y_coords)

    #data = [x_coords, y_coords]

    
    results = pd.DataFrame({
            "x_coords": x_coords,
            "y_coords": y_coords,
    })
    
    
    #results = pd.DataFrame(data, columns=['x_coords', 'y_coords'])


   

    #response = HttpResponse(content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename=filename.csv'

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)
    #writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    for i in range(1, results.shape[0]):

        print('RESULTS SHAPE IS', results.shape[0])
        
     
        writer.writerow([results.iloc[i,0], results.iloc[i,1]])



   # results.to_csv(path_or_buf=response,sep=';',float_format='%.2f',index=False,decimal=",")


    #return results
    return response



class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hplc.html', {})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    #def __init__(self, x_max, y_max, pathname):
    #    self.x_max = x_max
    #    self.y_max = y_max
    #    self.pathname = pathname

    def get(self, format = False):



        
        pathname = 'chemdataprowebsite/media/'



        '''
        field_name = 'image'
        obj = Image_Axes.objects.first()
        field_object = Image_Axes._meta.get_field(field_name)
        field_value = field_object.value_from_object(obj)


        print('field_value is', field_value)
        '''


        



        #image_path = pathname + str(field_value)

       

        out_df = plot_to_df(image_path, x_max, y_max)

        x_coords = out_df.iloc[:,0].tolist()
        y_coords = out_df.iloc[:,1].tolist()

        x_coords.reverse()
        y_coords.reverse()

        data = {
                    "x_coords": x_coords,
                    "y_coords": y_coords,
            }



        return Response(data)