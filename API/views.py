from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from Japa.models import NyBestilling
from .serializers import NyBestillingSerializer

@api_view(['POST'])
def create_order(request):
    serializer = NyBestillingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PATCH'])
def take_order(request):
    if request.method == 'PATCH':
        nybestilling_id = request.data.get('nybestilling_id')
        nybestilling = NyBestilling.objects.get(id=nybestilling_id)

        # Set the courier_id to the ID of the logged-in user
        nybestilling.courier_id = request.user.id
        nybestilling.save()

        serializer = NyBestillingSerializer(nybestilling)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)
    

class NyBestillingUpdateAPIView(generics.UpdateAPIView):
    queryset = NyBestilling.objects.all()
    serializer_class = NyBestillingSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        courier_id = self.request.data.get('Courier_id')
        if courier_id:
            serializer.instance.Courier_id = courier_id
        serializer.save()