from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import *
from django.db.models import Q, F
import simplejson
from rest_framework.decorators import api_view
from commodity.models import CommodityImage

b_response_body = {
    "code": 0,
    "msg": "success",
    "success": True,
    "data": {}
}


# Create your views here.
def register(request: HttpRequest):
    body = simplejson.loads(request.body)
    name = body['login_name']
    psd = body['password']
    nickname = body['nickname']
    email = body['email']
    UserInfo.objects.create(username=name, password=psd, nickname=nickname, email=email)
    return JsonResponse(b_response_body)


def login(request: HttpRequest):
    body = simplejson.loads(request.body)
    name = body['login_name']
    psd = body['password']
    data = {}
    try:
        qs = UserInfo.objects.get(Q(username=name) & Q(password=psd))
        if qs:
            data["user_id"] = qs.id
        response_body = b_response_body
        response_body['data'] = data
        return JsonResponse(response_body)
    except Exception as e:
        print(e)
        return HttpResponse("用户名或密码错误")


@api_view(['GET', 'PUT'])
def get_user_info(request: HttpRequest, id):
    user = UserInfo.objects.filter(id=id)

    if request.method == 'GET':
        data = {}
        data['email'] = user[0].email
        data['nickname'] = user[0].nickname
        if user[0].gender == 0:
            data['sex'] = "男"
        else:
            data['sex'] = "女"
        data['phone'] = int(user[0].phone)
        data['user_id'] = id
        response_body = b_response_body
        response_body['data'] = data
        return JsonResponse(response_body)

    elif request.method == 'PUT':
        body = simplejson.loads(request.body)
        email = body['email']
        nickname = body['nickname']
        phone = body['phone']
        sex = body['sex']
        if sex == '男':
            gender = 0
        else:
            gender = 1

        user.update(email=email, nickname=nickname, phone=phone, gender=gender)
        response_body = b_response_body
        return JsonResponse(response_body)


def add2cart(request: HttpRequest):
    body = simplejson.loads(request.body)
    amount = body['add_amount']
    commodity_id = body['product_id']
    user_id = body['user_id']
    item = CartDetail.objects.filter(user_id=user_id, commodity_id=commodity_id, is_deleted=0)
    if item:
        item.update(commodity_amount=F('commodity_amount') + amount)
        # item.update(commodity_amount=amount)
    else:
        CartDetail.objects.create(user_id=user_id, commodity_id=commodity_id, commodity_amount=amount)
    response_body = b_response_body
    return JsonResponse(response_body)


def modify(request: HttpRequest):
    body = simplejson.loads(request.body)
    amount = body['modified_amount']
    commodity_id = body['product_id']
    user_id = body['user_id']
    item = CartDetail.objects.filter(user_id=user_id, commodity_id=commodity_id, is_deleted=0)
    item.update(commodity_amount=amount)
    response_body = b_response_body
    return JsonResponse(response_body)


@api_view(['DELETE'])
def del_cart_items(request: HttpRequest):
    body = simplejson.loads(request.body)
    ids = eval(body['ids'])
    for id in ids:
        CartDetail.objects.filter(id=id).update(is_deleted=1)
    response_body = b_response_body
    return JsonResponse(response_body)


def get_cart_list(request: HttpRequest, id):
    cart_items = CartDetail.objects.filter(user_id=id, is_deleted=0)
    data_list = []
    for item in cart_items:
        data = {}
        data['add_amount'] = item.commodity_amount
        data['id'] = item.id

        commodity = item.commodity
        data['price'] = commodity.commodity_price
        data['product_id'] = commodity.id
        if commodity.commodity_pics:
            commodity_img_id = commodity.commodity_pics.split(',')[0]
            url = CommodityImage.objects.get(id=commodity_img_id).image_url.url
        else:
            url = None
        data['image_url'] = url
        data['product_name'] = commodity.commodity_name
        data['product_status'] = commodity.commodity_status
        data_list.append(data)
    response_body = b_response_body
    response_body['data'] = data_list
    return JsonResponse(response_body)


@api_view(['DELETE'])
def del_cart_item(request: HttpRequest, id):
    CartDetail.objects.filter(id=id).update(is_deleted=1)
    response_body = b_response_body
    return JsonResponse(response_body)
