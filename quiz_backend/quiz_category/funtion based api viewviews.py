from .models import Category
from .serializers import CategorySerializer
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category  # Import your Category model

@api_view(['GET'])  # Decorate the view with the allowed HTTP methods
def quiz_allcat_view(request):
    categories = Category.objects.all()  # Fetch all categories from the database
    serializer = CategorySerializer(
        categories, many=True)  # Serialize the categories
    # Return serialized data in a Response object
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def quiz_singlecat_view(request, id):
    cat = get_object_or_404(Category, id=id)
    serializer = CategorySerializer(cat)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])  # Decorate the view with the allowed HTTP methods
def quiz_create_category_view(request):
    if request.method == 'POST':  # Ensure the request method is POST
        # Create a serializer instance with request data
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():  # Check if the data is valid
            serializer.save()  # Save the data to the database
            # Return serialized data with status 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Return errors if data is invalid
        print("Data is invalid:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Return 405 (Method Not Allowed) for other HTTP methods
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def test(request):
    if request.method == 'GET':
        return Response({"msg": "get request"})
    if request.method == 'POST':
        return Response({"msg": "post request", "data": request.data})


@api_view(['GET', 'PUT'])
def update(request, id):
    if request.method == "GET":
        category = Category.objects.get(pk=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        try:
            category = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return Response("Category does not exist", status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
