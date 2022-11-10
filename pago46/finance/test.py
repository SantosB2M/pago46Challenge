import unittest
from django.urls import reverse
from model_bakery import baker
from finance.models import IOU
from rest_framework.test import APIClient
from rest_framework.status import HTTP_201_CREATED
from datetime import datetime
from graphene_django.uils.testing import GraphQLTestCase
import freezegun

class TestIOU(unittest.TestCase):
    def test_iou_list(self):
        lender, borrower = baker.make('users.User', _quantity=2)
        iou = baker.make('finance.IOU', lender=lender, borrower=borrower)
        expected_response = []
        all_iou = IOU.objects.all().order_by('value')
        for iou in all_iou:
            expected_response.append({
                "lender": iou.lender.id,
                "borrower": iou.borrower.id,
                "value": iou.value,
                "expiration": iou.expiration.isoformat()[:-6]+'Z'
            })
        client = APIClient()
        response = client.get(reverse("iou-list"))
        received_response = response.json()
        self.assertListEqual(
            expected_response,
            received_response
        )
        assert True
    def test_iou_insert(self):
        lender, borrower = baker.make('users.User', _quantity=2)
        expiration = datetime.now()
        client = APIClient()
        payload = {
            "lender":lender.id,
            "borrower":borrower.id,
            "value":100.00,
            "expiration": expiration.isoformat()+"Z"
        }
        expected_response = payload
        expected_status_code = HTTP_201_CREATED 
        response = client.post(reverse('iou-list'), data=payload)
        received_response = response.json()
        received_status_code = response.status_code
        self.assertDictEqual(expected_response,received_response)
        self.assertEqual(expected_status_code, received_status_code)