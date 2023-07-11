from todolist.serializers import TodoSerializer
from todolist.models import Todo
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
    
class TodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    # this will create a todo 
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    # this will list todos 
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)