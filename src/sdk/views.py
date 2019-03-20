import requests
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from sdk.serializers import TransferSerializer


class StartView(APIView):
    def get(self, request, format=None):
        return Response('API works')


class SampleAuthView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response({'name': request.user.user_name})


class TransferView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        request_data = {}
        request_data.update(request.data)
        request_data['user_id'] = request.user.user_id
        request_data['api_token'] = request.user.api_token

        serializer = TransferSerializer(data=request_data)
        serializer.is_valid(True)

        url = '{}/{}'.format(settings.CONST_EXCHANGE_API['URL'], 'public-transfer/')
        resp = requests.post(url, headers={
            'Authorization': 'Bearer {}'.format(settings.CONST_EXCHANGE_API['TOKEN'])
        }, data=serializer.validated_data, verify=False)

        return Response(resp.json(), status=resp.status_code)
