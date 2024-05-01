from django.test import TestCase


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer

class VendorAPITestCase(APITestCase):
    def setUp(self):
        self.vendor_data = {
            'name': 'Vendor 1',
            'contact_details': 'Contact details 1',
            'address': 'Address 1',
            'vendor_code': 'VENDOR001'
        }
        self.vendor = Vendor.objects.create(**self.vendor_data)
        self.vendor_url = reverse('vendor-detail', args=[self.vendor.id])

    def test_create_vendor(self):
        response = self.client.post(reverse('vendor-list-create'), self.vendor_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 2)  # Assuming one vendor already exists

    def test_retrieve_vendor(self):
        response = self.client.get(self.vendor_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, VendorSerializer(self.vendor).data)

   
class PurchaseOrderAPITestCase(APITestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(name='Vendor 1', contact_details='Contact details 1', address='Address 1', vendor_code='VENDOR001')
        self.purchase_order_data = {
            'po_number': 'PO001',
            'vendor': self.vendor.id,
            'order_date': '2024-05-01T00:00:00Z',
            'delivery_date': '2024-05-10T00:00:00Z',
            'items': [{'name': 'Item 1', 'quantity': 10}],
            'quantity': 10,
            'status': 'pending'
        }
        self.purchase_order = PurchaseOrder.objects.create(**self.purchase_order_data)
        self.purchase_order_url = reverse('purchaseorder-detail', args=[self.purchase_order.id])

    def test_create_purchase_order(self):
        response = self.client.post(reverse('purchaseorder-list-create'), self.purchase_order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 2)  # Assuming one purchase order already exists

    def test_retrieve_purchase_order(self):
        response = self.client.get(self.purchase_order_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, PurchaseOrderSerializer(self.purchase_order).data)
