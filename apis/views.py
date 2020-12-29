from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from apis.models import CustomUser, Contacts
from apis.serializers import CustomuserSerializer, ContactsSerializer
from django_filters.rest_framework import DjangoFilterBackend


class GetUsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        object = CustomUser.objects.filter(id=kwargs['pk'])
        serializer = CustomuserSerializer(object, many=True)
        return Response(serializer.data)




class ContactCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


    def perform_create(self, serializer):
        serializer.save()





class GetUsersContactListView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        object = Contacts.objects.filter(user_id=kwargs['pk'])
        serializer = ContactsSerializer(object, many=True)
        return Response(serializer.data)



class ContactSearch(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'email', 'phone']
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer




