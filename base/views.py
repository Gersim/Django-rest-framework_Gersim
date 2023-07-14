import http

from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer

from rest_framework.views import APIView
from django.db.models import Q

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates','advocates/:username']
    return Response(data)

@api_view(['GET','POST'])
def advocate_list(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query == None:
            query = ''
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        advocate = Advocate.objects.create(
            username=request.data['username'], bio=request.data['bio'])
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)



# -------------***** Django model view class *****-------------------------

class AdvocateDetail(APIView):

    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except:
            raise Advocate

    def get(self, request, username):
        advocate = self.get_object(username)
        serializers = AdvocateSerializer(advocate, many=False)
        return Response(serializers.data)

    def put(self,request, username):
        advocate = self.get_object(username)
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()
        serializers = AdvocateSerializer(advocate, many=False)
        return Response(serializers.data)

    def delete(self, request, username):
        advocate = self.get_object(username)
        advocate.delete()
        return Response('User was deleted')

# -----------------------***END***---------------------------------------------


# --------------------***Company**------------------------------------------
class CompanyList(APIView):
    def get(self, request):
        companie = Company.objects.all()
        serializers = CompanySerializer(companie, many=True)
        return Response(serializers.data)


    def post(self,request):
        company = Company.objects.create(
            name=request.data['name'], bio=request.data['bio']
        )
        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data)




class CompanyDetails(APIView):

    def get_object(self, name):
        try:
            return Company.objects.get(name=name)
        except:
            raise Company


    def get(self,request,name):
        company = self.get_object(name)
        serilization = CompanySerializer(company, many=False)
        return Response(serilization.data)

    def delete(self,request,name):
        company = self.get_object(name)
        company.delete()
        return Response("The company was deleted")


# -----------------------***END***-----------------------