from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentProfileSerializer

class CreateStudentProfileView(APIView):
    def get(self, request):
        return Response({"message": "Use POST to create a profile."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = StudentProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile created successfully!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
