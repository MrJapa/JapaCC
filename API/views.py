
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Japa.models import NyBestilling
from .serializers import NyBestillingSerializer

@api_view(['POST'])
def create_order(request):
    serializer = NyBestillingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)