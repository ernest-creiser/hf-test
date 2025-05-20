from rest_framework import filters, permissions, serializers, viewsets

from app.models import Game, Platform, Studio


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class GameViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing books.
    """

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "studio__name", "platform__name"]


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = "__all__"


class StudioViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing books.
    """

    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    permission_classes = [permissions.AllowAny]


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = "__all__"


class PlatformViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing books.
    """

    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [permissions.AllowAny]
