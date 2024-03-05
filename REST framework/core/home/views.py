from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializers(student_objs,many=True)
    return Response({'status':200,'patlod':serializer.data })


class StudentAPI(APIView):
    def get(self,request):
        student_objs = Student.objects.all()
        serializer = StudentSerializers(student_objs,many = True)
        return Response({"status":200,"paylod":serializer.data})
    
    def post(self,request):
        serializer = StudentSerializers(data = request.data)
        if not serializer.is_valid():
            return Response({"status":403,"message":"gadbad hay "})
        serializer.save()
        return Response({'status':200,'paylod':serializer.data,'message':'hello' })
        
    def put(self,request):
        pass
    def patch(self,request):
        try:
            student_objs = Student.objects.get(id = request.data.get('id'))
            # serializer = StudentSerializers(student_objs,many = True)
            serializer = StudentSerializers(student_objs,data = request.data,partial = True)
            print('hellooooooooooo world')
            if not serializer.is_valid():
                return Response({'status':403,'message':'something went wronggggggg','errors':serializer.errors})
            serializer.save()    
            return Response({'status':200,'paylod':serializer.data,'message':'your response is saved'})
        except Exception as e:
            print("exceprion",e)
            print("hat BC")
            return Response({'status':403,'messages':"This id is invalidaaaaaaaaaa"})
    def delete(self,request):
        try:
            id = request.data.get('id')
            student_objs = Student.objects.get(id = id)
            # serializer = StudentSerializers(student_objs,data = request.data,partial = True)
            # if not serializer.is_valid():
                # return Response({'status':403,'message':'something went wronggggggg','errors':serializer.errors})
            # serializer.save()    
            student_objs.delete()
            return Response({'status':200,'message':'your response is saved'})
        except:
            return Response({'status':403,'messages':"This id is invalid"})





# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serializer = StudentSerializers(data = request.data)
#     if not serializer.is_valid():
#         return Response({'status':403,'message':'something went wronggggggg'})
#     serializer.save()    
#     print(data)
#     return Response({'status':200,'paylod':serializer.data,'message':'hello' })

# @api_view(['PUT'])
# def update_student(request,id):
#     try:
#         student_objs = Student.objects.get(id = id)
#         # serializer = StudentSerializers(student_objs,many = True)
#         serializer = StudentSerializers(student_objs,data = request.data,partial = True)
#         if not serializer.is_valid():
#             return Response({'status':403,'message':'something went wronggggggg','errors':serializer.errors})
#         serializer.save()    
#         return Response({'status':200,'payload':serializer.data,'message':'your response is saved'})
#     except:
#         return Response({'status':403,'messages':"This id is invalid"})
    

# @api_view(['DELETE'])
# def delete_student(request):
#     try:
#         id = request.GET.get('id')
#         student_objs = Student.objects.get(id = id)
#         # serializer = StudentSerializers(student_objs,data = request.data,partial = True)
#         # if not serializer.is_valid():
#             # return Response({'status':403,'message':'something went wronggggggg','errors':serializer.errors})
#         # serializer.save()    
#         student_objs.delete()
#         return Response({'status':200,'message':'your response is saved'})
#     except:
#         return Response({'status':403,'messages':"This id is invalid"})