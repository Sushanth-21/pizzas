from pizzaInfo.models import Toppings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Pizza
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializer import UserSerializer, RegisterSerializer, ToppingsSerializer, PizzaSerializer, PizzaCreateSerializer
from rest_framework import status


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user1 = serializer.save()
    return Response({
        "user": UserSerializer(user1).data,
        "token": str(Token.objects.create(user=user1))
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    user.save()
    token = Token.objects.get_or_create(user=user)
    user_serializer = UserSerializer(user)
    return Response({'token': str(token), 'user': user_serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        token = Token.objects.get(user=request.user)
        token.delete()
    except Token.DoesNotExist:
        pass
    return Response({"logout": "User logged out"})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_square(request):

    size = request.data.get("size").lower()
    lst = Pizza.objects.filter(size=size)
    if len(lst) == 0:
        return Response({"message": "Please choose other size"}, status=status.HTTP_400_BAD_REQUEST)

    data = {"created_by": request.user.id,
            "type": "square",
            "size": size}

    toppings = request.data.get("toppings")
    pizza_serializer = PizzaCreateSerializer(data=data)

    if pizza_serializer.is_valid():
        pizza = pizza_serializer.save()

        for top in toppings:
            topping = Toppings.objects.filter(name=top.lower())
            if len(topping) == 0:
                topping = Toppings.objects.create(name=top.lower())
                pizza.toppings.add(topping)
            else:
                pizza.toppings.add(topping[0])
        pizza.save()

        data = PizzaSerializer(pizza).data
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_regular(request):

    size = request.data.get("size").lower()
    lst = Pizza.objects.filter(size=size)
    if len(lst) == 0:
        return Response({"message": "Please choose other size"}, status=status.HTTP_400_BAD_REQUEST)

    data = {"created_by": request.user.id,
            "type": "regular",
            "size": size}

    toppings = request.data.get("toppings")
    pizza_serializer = PizzaCreateSerializer(data=data)

    if pizza_serializer.is_valid():
        pizza = pizza_serializer.save()

        for top in toppings:
            topping = Toppings.objects.filter(name=top)
            if len(topping) == 0:
                topping = Toppings.objects.create(name=top)
                pizza.toppings.add(topping)
            else:
                pizza.toppings.add(topping[0])
        pizza.save()

        data = PizzaSerializer(pizza).data
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def all(request):
    pizzas = Pizza.objects.all()
    data = []
    for pza in pizzas:
        pza_info = PizzaSerializer(pza).data
        data.append(pza_info)
    return Response(data, status=status.HTTP_202_ACCEPTED)


@api_view(['DELETE', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update(request, pk):
    try:
        pizza = Pizza.objects.get(id=pk)
    except:
        return Response({"message": "Invalid pizza id"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        pizza.delete()
        return Response({"message": "Deleted"}, status=status.HTTP_202_ACCEPTED)

    if request.method == 'PUT':

        type = request.data["type"].lower()
        if type != "regular" and type != "square":
            return Response({"message": "Please choose other type"}, status=status.HTTP_400_BAD_REQUEST)

        size = request.data.get("size").lower()
        lst = Pizza.objects.filter(size=size)
        if len(lst) == 0:
            return Response({"message": "Please choose other size"}, status=status.HTTP_400_BAD_REQUEST)

        data = {"created_by": request.user.id,
                "type": type,
                "size": size}

        toppings = request.data.get("toppings")
        pizza_serializer = PizzaCreateSerializer(pizza, data=data)

        if pizza_serializer.is_valid():
            pizza = pizza_serializer.save()
            pizza.toppings.clear()

            for top in toppings:
                topping = Toppings.objects.filter(name=top)
                if len(topping) == 0:
                    topping = Toppings.objects.create(name=top)
                    pizza.toppings.add(topping)
                else:
                    pizza.toppings.add(topping[0])
            pizza.save()

            data = PizzaSerializer(pizza).data
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def filterByType(request, pk):
    lst = Pizza.objects.filter(type=pk.lower())
    data = []
    for i in lst:
        serialized = PizzaSerializer(i).data
        data.append(serialized)
    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def filterBySize(request, pk):
    lst = Pizza.objects.filter(size=pk.lower())
    data = []
    for i in lst:
        serialized = PizzaSerializer(i).data
        data.append(serialized)
    return Response(data, status=status.HTTP_201_CREATED)
