from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Worker, Shop, Visit
from .authentication import PhoneAuthentication
from django.contrib.auth.models import AnonymousUser


class ShopListView(APIView):
    authentication_classes = [PhoneAuthentication]

    def get(self, request):
        if isinstance(request.user, AnonymousUser):
            return Response({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)

        worker = request.user
        shops = Shop.objects.filter(worker=worker)

        if not shops.exists():
            return Response({'error': 'No shops found for this worker'}, status=status.HTTP_404_NOT_FOUND)

        shop_list = [{'pk': shop.pk, 'name': shop.name} for shop in shops]
        return Response(shop_list, status=status.HTTP_200_OK)


class VisitCreateView(APIView):
    authentication_classes = [PhoneAuthentication]

    def post(self, request):
        if isinstance(request.user, AnonymousUser):
            return Response({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)

        worker = request.user
        shop_pk = request.data.get('shop_pk')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        try:
            shop = Shop.objects.get(pk=shop_pk)
        except Shop.DoesNotExist:
            return Response({'error': 'Shop not found'}, status=status.HTTP_404_NOT_FOUND)

        if shop.worker != worker:
            return Response({'error': 'Worker not assigned to this shop'}, status=status.HTTP_403_FORBIDDEN)

        visit = Visit.objects.create(shop=shop, worker=worker, latitude=latitude, longitude=longitude)
        visit_data = {
            'pk': visit.pk,
            'datetime': visit.datetime
        }
        return Response(visit_data, status=status.HTTP_201_CREATED)
