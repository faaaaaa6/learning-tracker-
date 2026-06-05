from rest_framework import serializers
from django.contrib.auth import get_user_model
# fetching our customer model.

#we store that variale in User for calling easly if needed.
User = get_user_model()

# created a Serializer class , borrowing DRF built in serializer tools(inhertance)
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
        #extra rule/don't return the password
        extra_kwargs = {'password':{'write_only': True}}  
    
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)#** for unpacking into keyword arguments
        return user