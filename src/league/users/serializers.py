from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.serializers import CharField, EmailField, ModelSerializer, ValidationError

User = get_user_model()


class CreateUserSerializer(ModelSerializer):
    password = CharField(label='Password',
                         write_only=True,
                         required=True,
                         help_text='',
                         style={'input_type': 'password', 'placeholder': 'Password'}
                         )
    password2 = CharField(label='Confirm Password',
                          write_only=True,
                          required=True,
                          help_text='',
                          style={'input_type': 'password', 'placeholder': 'Password'}
                          )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return validated_data

    def validate_password2(self, value):
        data = self.get_initial()
        password = data.get('password')

        if password != value:
            raise ValidationError('Password Mismatch')

        return value

    def validate_email(self, value):
        data = self.get_initial()
        email = data.get('email')

        user_qs = User.objects.filter(email=email)

        if user_qs.exists():
            raise ValidationError('This email is taken')

        return value


class UserLoginSerializer(ModelSerializer):
    email = EmailField(label='Email Address', required=False, allow_blank=True)
    token = CharField(allow_blank=True, read_only=True)
    password = CharField(label='Password',
                         write_only=True,
                         required=True,
                         help_text='',
                         style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = ['email', 'password', 'token']

    def validate(self, attrs):
        email = attrs.get('email', None)
        password = attrs['password']
        if not email:
            raise ValidationError('email is required to login')

        user = User.objects.filter(email=email).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('this email is not valid')
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Incorrect credentials please try again')
        attrs['token'] = 'some random token'
        return attrs
