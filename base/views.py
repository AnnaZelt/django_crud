# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Product
import json

@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = [{'desc': product.desc, 'price': str(product.price), 'cat': product.cat, 'image': product.image.url} for product in products]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        product = Product(desc=data['desc'], price=data['price'], cat=data['cat'], image=data.get('image', '/placeholder.png'))
        product.save()
        return JsonResponse({'message': 'Product created successfully'}, status=201)

@csrf_exempt
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

    if request.method == 'GET':
        data = {'desc': product.desc, 'price': str(product.price), 'cat': product.cat, 'image': product.image.url}
        return JsonResponse(data)
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        product.desc = data['desc']
        product.price = data['price']
        product.cat = data['cat']
        product.image = data.get('image', '/placeholder.png')
        product.save()
        return JsonResponse({'message': 'Product updated successfully'})
    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully'})
