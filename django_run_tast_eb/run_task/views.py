from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from run_task.serializers import UserSerializer, GroupSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



@api_view(['GET', 'POST'])
def run_task(request):
    """
    run task
    """
    if request.method == 'GET':
        print("------------------")
        return Response({"response":"ok"})