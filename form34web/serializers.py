from .models import Region, Pdfpath

from rest_framework import serializers
from rest_framework.response import Response


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 2
        model = Region
        fields = "__all__"
        read_only_fields = ('region_id',)


class PdfpathSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        depth = 2
        model = Pdfpath
        fields = "__all__"
        read_only_fields = ('url', 'form_34_path',
                            'polling_station_code',
                            'date_posted')
