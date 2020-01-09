from django.http import HttpRequest, JsonResponse
from commodity.models import CommodityDetail, CommodityImage
from .models import *
from rest_framework.decorators import api_view
import simplejson
from CMS.settings import MEDIA_ROOT

b_response_body = {
    "code": 0,
    "msg": "success",
    "success": True,
    "data": {}
}


# Create your views here.
@api_view(['POST'])
def order(request: HttpRequest):
    body = simplejson.loads(request.body)
    payment = body['pay_method']
    user_id = body['user_id']
    order_list = eval(body['order_product_list'])
    for order in order_list:
        amount = order['amount']
        commodity_id = order['product_id']
        commodity = CommodityDetail.objects.get(id=commodity_id)
        if commodity.commodity_pics:
            commodity_img_id = commodity.commodity_pics[0]
            url = CommodityImage.objects.get(id=commodity_img_id).image_url.url
        else:
            url = None
        UserOrder.objects.create(user_id=user_id, price=(amount * commodity.commodity_price), payment_type=payment)
        order = UserOrder.objects.first()
        OrderDetail.objects.create(order_id=order.id, commodity_id=commodity_id,
                                   commodity_name=commodity.commodity_name,
                                   commodity_price=commodity.commodity_price, commodity_amount=amount,
                                   commodity_image=url)
    response_body = b_response_body
    return JsonResponse(response_body)


@api_view(['GET'])
def get_order_detail(request: HttpRequest, id):
    order_items = OrderDetail.objects.filter(order_id=id)
    data_list = []
    for item in order_items:
        data = {}
        data['amount'] = item.commodity_amount
        data['image_url'] = item.commodity_image
        data['order_id'] = id
        data['price'] = item.commodity_price
        data['product_id'] = item.commodity_id
        data['product_name'] = item.commodity_name
        data_list.append(data)
    response_body = b_response_body
    response_body['data'] = data_list

    print(MEDIA_ROOT)
    return JsonResponse(response_body)


@api_view(['GET'])
def get_order(request: HttpRequest, id):
    pass
