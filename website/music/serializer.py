from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import album

user=get_user_model()

class AlbumSerializer(serializers.ModelSerializer):
#    url=serializers.HyperlinkedIdentityField(view_name="detail", lookup_field='title')
    class Meta:
        model = album
        fields = ["title","artist"]

class AlbumSerializerlist(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name="detail", lookup_field='title')
    class Meta:
        model = album
        fields = ["title","url"]

class UserCreateSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(label='Email')  #this is going to override the default email field in the user model and it will make it required instead of being optional by django
    # email2=serializers.EmailField(label='confirm Email')
    class Meta:
        model=user
        fields=[    #attributes predefined in user model
        "username",
        "password",
        "email",
        # "email2"

        ]
        extra_kwargs = {'password': {'write_only': True}}


        def validate(self,data): #email has to be unique
            email=data["email"]
            userqs=Users.objects.filter(email=email)
            if userqs.exists():
                raise serializers.ValidationError("This user already exists")

        # def validate_email2(self,value): #value is the actual value that is being passed to email2
        #     data=self.get_initial() #it's only passing the value itself , self.get_initial will give u the data (the dictionary) and then with the .get("email") u can get the email itself
        #     print(data)
        #     email1=data.get("email")
        #     email2=value
        #     if email1 != email2:
        #         raise serializers.ValidationError("Emails must match") #it'll be raised under email2 because of the methods name
        #     return value

            # def validate_email(self,value):
            #     data=self.get_initial()
            #     email1=data.get("email2")
            #     email2=value
            #     if email1 != email2:
            #         raise ValidationError("Emails must match")
            #     return value


        def create(self,validated_data): #it's the same CreateAPIView but we're overriding it to add things
            username=validated_data["username"]
            password=validated_data["password"]
            email=validated_data["email"]
            print(username, password,email)

            user_obj=User(username=username,email=email )
            user_obj.set_password(password)
            user_obj.save()
            #return user_obj
            return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    token=serializers.CharField(allow_blank=True,read_only=True)
    username=serializers.CharField()
    email=serializers.EmailField(label='Email')  #this is going to override the default email field in the user model and it will make it required instead of being optional by django

    class Meta:
        model=user
        fields=[    #attributes predefined in user model
        "username",
        "email",
        "password",
        "token"
        ]
        extra_kwargs = {'password': {'write_only': True}}


        def validate(self,data): #email has to be unique
            email=data["email"]
            userqs=Users.objects.filter(email=email)
            if userqs.exists():
                raise ValidationError("This user already exists")



# item1={"name":"item","type":"new"}
# ser=AlbumSerializer(item1)
# if ser.is_valid():
#     ser.save()
# else: ser.errors()
