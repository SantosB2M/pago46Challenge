from rest_framework import serializers
from finance.models import IOU


class IOUSerializer(serializers.ModelSerializer):
    class Meta:
        model = IOU
        fields = ["value", "expiration"]

class IOUModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IOU
        fields = ["lender","borrower","value","expiration",]
