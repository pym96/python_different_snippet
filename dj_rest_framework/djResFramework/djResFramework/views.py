'''
    This manual file will let us use
    the APIViews from rest_framework django library
'''

from django.shortcuts import render
from rest_framework.views import APIView

# Give the user the response of the rest data
from rest_framework.response import Response


# By using rest_framework library and some stuff in it, we use the proxy mode to let our back-end data visible
class TestView(APIView):
    def get(self,request,*args,**kwargs):
        data = {
            'user':'admin'
            ,'years_active':10
        }
        return Response(data)