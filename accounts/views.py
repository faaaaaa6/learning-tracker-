from rest_framework import generics
#ready made view(generics)
from rest_framework.permissions import AllowAny
#allowany=anyone can hit this url-even without logging in.
from .serializers import RegisterSerializer
#importing rs.

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

