from rest_framework import serializers

# from watchlist_app.models import WatchList,SteamPlatform

class MovieSerializers(serializers.Serializer):
  id = serializers.IntegerField(read_only = True)
  name = serializers.CharField()
  description = serializers.CharField()
  active = serializers.BooleanField()

#   class Meta:
#     model = SteamPlatform
#     fields = "__all__"

# class WatchListSerializers(serializers.ModelSerializer):
#   # len_name = serializers.SerializerMethodField()
  
#   class Meta:
#     model =  WatchList
#     fields = "__all__"