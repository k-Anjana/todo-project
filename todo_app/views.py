from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.views import APIView
import jwt
from django.conf import settings
from rest_framework.response import Response
from .models import Tasks
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse('index')

def insert(request,username,task,description,status):
    record=Tasks.objects.create(username=username,task=task,description=description,status=status)
    response_data={"message":"insertion successfull"}
    return response_data

def fetch_pending(request,username):
    record=Tasks.objects.filter(username=username,status="pending").values()
    task_list=[]
    for item in record:
        task_list.append(item['task'])
    response_data={"tasklist":task_list}
    return response_data

def fetch_total(request,username):
    record=Tasks.objects.filter(username=username).values()
    task_list=[]
    status_list=[]
    for item in record:
        task_list.append(item['task'])
        status_list.append(item['status'])
    response_data={"tasklist":task_list,"statuslist":status_list}
    return response_data

def update(request,username,task,description,status,upload_file):
    record=Tasks.objects.filter(username=username,task=task,status='pending').first()
    record.description=description
    record.status='done'
    save_directory = 'taskfiles/'
    record.file = default_storage.save(save_directory + upload_file.name, upload_file)
    record.save()
    response_data={"message":"Task status updated successfully"}
    return response_data

def delete(request,username,task):
    record=Tasks.objects.filter(username=username,task=task)
    response_data={'message':'Task deleted successfully'}
    return response_data

class Todo(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        try:
            response ={"WOW":"get"}
            Type = self.request.GET.get('type')
            username = self.request.GET.get('username')
            task = self.request.GET.get('task')
            status = self.request.GET.get('status')
            description = self.request.GET.get('description')

            if Type=='fetch_pending':
                response=fetch_pending(request,username)
            if Type=='fetch_total':
                response=fetch_total(request,username)


            return JsonResponse(response)
            
        except Exception as e:
            return Response({'error': str(e)})

    def post(self,request,*args,**kwargs):
        try:
            response ={"WOW":"post"}
            Type = self.request.GET.get('type')
            
            username = self.request.GET.get('username')
            task = self.request.GET.get('task')
            status = self.request.GET.get('status')
            description = self.request.GET.get('description')
            upload_file = self.request.FILES.get('file')
            
            if Type == 'insert':
                response=insert(request,username,task,description,status)
            if Type == 'update':
                response=update(request,username,task,description,status,upload_file)
            if Type == 'delete':
                response=delete(request,username,task)

            return JsonResponse(response)
                
        except Exception as e:
            return Response({'error': str(e)})
        
class DataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            token = request.META['HTTP_AUTHORIZATION'].split()[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
            data = {"Userid":user_id}
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=401)
