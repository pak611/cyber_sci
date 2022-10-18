from django.contrib import admin

# Register your models here.
from .models import Image_Axes
from .models import graph_input


admin.site.register(graph_input)

admin.site.register(Image_Axes)