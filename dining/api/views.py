from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import User, Place
from .serializers import *

# Create your views here.

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = DiningSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def signup(request):
    serializer = DiningSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("User Registered")
    return Response(serializer.data)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        curr_user = serializer.data.get("username")
        curr_pwd = serializer.data.get("password")
        try:
            user = User.objects.get(username=curr_user)
            if user.password == curr_pwd:
                data = {
                "status": "Login successful",
                "status_code": 200,
                "user_id": "12345",
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
                }
                return Response(data)
            else:
                data = {
                "status": "Incorrect username/password provided. Please retry",
                "status_code": 401
            }
            return Response(data)
        except User.DoesNotExist:
            data = {
                "status": "Incorrect username/password provided. Please retry",
                "status_code": 401
            }
            return Response(data)
    return Response("Invalid Data Sent")

@api_view(['GET'])
def display(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)
        
@api_view(['POST'])
def create(request):
    serializer = PlaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
            "message": "Place added successfully",
            "place_id": "12345",
            "status_code": 200
        }
        return Response(data)
    return Response("Invalid Data")

@api_view(['POST'])
def search(request):
    users = User.objects.all()
    serializer = PlaceSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def availability(request):
    users = User.objects.all()
    serializer = PlaceSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book(request):
    users = User.objects.all()
    serializer = PlaceSerializer(users, many=True)
    return Response(serializer.data)