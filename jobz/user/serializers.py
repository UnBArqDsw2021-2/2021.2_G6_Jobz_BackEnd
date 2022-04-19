import re
from rest_framework import serializers

from .models import User, Provider


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["cpf", "name", "phone", "email", "password", "photo"]

    def save(self):
        if self.context['request'].method != 'PATCH':
            user = User(
                cpf=self.validated_data["cpf"],
                name=self.validated_data["name"],
                phone=self.validated_data["phone"],
                email=self.validated_data["email"],
                photo=self.validated_data["photo"],
            )
            password = self.validated_data["password"]
            if re.match("^[a-zA-Z0-9/*-+.,!-@#$%&*()_=]{8,50}$", password) == None:
                raise serializers.ValidationError(
                    "A senha deve conter no minimo 8 caracteres."
                )
            else:
                user.set_password(password)
                user.save()
                return user
        
        else:
            user = User.objects.get(cpf=self.data['cpf'])

            if 'name' in self.context['request'].data:
                name = self.validated_data['name']
                user.name = name

            if 'phone' in self.context['request'].data:
                phone = self.validated_data['phone']
                user.phone = phone

            if 'photo' in self.context['request'].data:
                photo = self.validated_data['photo']
                user.photo = photo

            if 'password' in self.context['request'].data:
                password = self.validated_data['password']

                if re.match("^[a-zA-Z0-9/*-+.,!-@#$%&*()_=]{8,50}$", password) == None:
                    raise serializers.ValidationError(
                        "A senha deve conter no minimo 8 caracteres."
                    )
                else:
                    user.set_password(password)
                    user.save()
                    return user
            else:
                user.save()
                return user


class ProviderSerializers(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Provider
        fields = ["cpf", "name", "phone", "email", "password", "occupation", "photo"]

    def save(self):
        provider = Provider(
            cpf=self.validated_data["cpf"],
            name=self.validated_data["name"],
            phone=self.validated_data["phone"],
            email=self.validated_data["email"],
            occupation=self.validated_data["occupation"],
            photo=self.validated_data["photo"],
        )
        password = self.validated_data["password"]
        if re.match("^[a-zA-Z0-9/*-+.,!-@#$%&*()_=]{8,50}$", password) == None:
            raise serializers.ValidationError(
                "A senha deve conter no minimo 8 caracteres."
            )
        else:
            provider.set_password(password)
            provider.save()
            return provider
