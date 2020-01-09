from django.http import HttpRequest, JsonResponse
from .models import *
from order.models import OrderDetail
from activity.models import RelActivityCommodity
import simplejson
from rest_framework.decorators import api_view

b_response_body = {
    "code": 0,
    "msg": "success",
    "success": True,
    "data": []
}


# Create your views here.
@api_view(['POST'])
def list(request: HttpRequest):  # 根据筛选条件，获取商品[简要信息]列表
    body = simplejson.loads(request.body)
    category = int(body['three_category_id'])
    datalist = []
    commodities = CommodityDetail.objects.filter(commodity_type_id=category)
    for commodity in commodities:
        data = {}
        data["product_id"] = commodity.id
        data["product_name"] = commodity.commodity_name
        data["price"] = commodity.commodity_price
        data["amount"] = 100
        data["description"] = commodity.commodity_info
        data["image_url"] = CommodityImage.objects.filter(commodity_id=commodity.id).first().image_url.url
        data["status"] = commodity.commodity_status
        data["three_category_id"] = commodity.commodity_type.id
        two_category = commodity.commodity_type.parent
        if two_category:
            data["two_category_id"] = two_category.id
            one_category = two_category.parent
            if one_category:
                data["one_category_id"] = one_category.id
            else:
                data["one_category_id"] = None
        else:
            data["two_category_id"] = None
            data["one_category_id"] = None
        data["sold_out"] = len(OrderDetail.objects.filter(commodity_id=commodity.id).all())
        datalist.append(data)

    response_body = b_response_body
    response_body['data'] = datalist
    return JsonResponse(response_body)


def get_by_id(request: HttpRequest, id):
    commodity = CommodityDetail.objects.get(id=id)
    url_list = []
    if commodity.commodity_pics:
        commodity_img_ids = commodity.commodity_pics.split(',')
        for _id in commodity_img_ids:
            url = CommodityImage.objects.get(id=_id).image_url.url
            url_list.append(url)
    data = {}
    data["product_id"] = commodity.id
    data["product_name"] = commodity.commodity_name
    data["price"] = commodity.commodity_price
    data["amount"] = 100
    data["description"] = commodity.commodity_info
    if len(url_list) != 0:
        data["image_url"] = url_list[0]
        url_list = url_list[1:]
    else:
        data["image_url"] = None
    data["status"] = commodity.commodity_status
    data["three_category_id"] = commodity.commodity_type.id
    two_category = commodity.commodity_type.parent
    if two_category:
        data["two_category_id"] = two_category.id
        one_category = two_category.parent
        if one_category:
            data["one_category_id"] = one_category.id
        else:
            data["one_category_id"] = None
    else:
        data["two_category_id"] = None
        data["one_category_id"] = None
    data["sold_out"] = len(OrderDetail.objects.filter(commodity_id=commodity.id).all())
    data["sub_image_url_list"] = url_list
    activity_ids = RelActivityCommodity.objects.filter(commodity_id=id).values("activity")
    id_list = []
    for id in activity_ids:
        id_list.append(id['activity'])
    data['activity_ids'] = str(id_list)

    response_body = b_response_body
    response_body['data'] = data
    return JsonResponse(response_body)


def get_category_tree(request: HttpRequest, id):
    if int(id) == 0:
        data = {}
        data["category_id"] = 0
        data["category_name"] = '商品类别'
        data["parent_id"] = -1
        data["category_level"] = 0
        data["category_status"] = 1
        data["children"] = []
        categories = CommodityType.objects.filter(parent_id=None)
        for category in categories:
            data["children"].append(get_tree(category.id))
    else:
        data = get_tree(int(id))

    response_body = b_response_body
    response_body['data'] = data
    return JsonResponse(response_body)


class CategoryNode():

    def __init__(self, id, level=0):
        self.category = CommodityType.objects.get(id=id)
        self.children = CommodityType.objects.filter(parent_id=id)
        self.level = level

    def __str__(self):
        return simplejson.dumps(get_tree(self.category.id))


def get_tree(id: int, level: int = 1):
    data = {}
    node = CategoryNode(id)
    node.level = level
    data["category_id"] = node.category.id
    data["category_name"] = node.category.type_name
    data["parent_id"] = node.category.parent_id
    data["category_level"] = node.level
    data["category_status"] = 1
    c_list = []
    for c in node.children:
        c_list.append(get_tree(c.id, node.level + 1))

    data["children"] = c_list
    return data
