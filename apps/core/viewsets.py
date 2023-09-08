from rest_framework import viewsets


class BaseViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
