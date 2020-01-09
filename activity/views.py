from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import *
from commodity.models import CommodityImage,CommodityDetail
from order.models import OrderDetail
from django.db.models import Q, F
import simplejson
from rest_framework.decorators import api_view

b_response_body = {
    "code": 0,
    "msg": "success",
    "success": True,
    "data": {}
}


# Create your views here.
@api_view(['GET'])
def get_commodities(request: HttpRequest, status):
    items = ActivityDetail.objects.filter(activity_status=status)
    datalist = []
    for item in items:
        data = {}
        data['activity_id'] = item.id
        data['activity_name'] = item.activity_name
        data['activity_type'] = item.activity_type.id
        data['description'] = item.activity_info
        data['status'] = item.activity_status
        data['start_time'] = "2020-01-04 12:00:00"
        data['end_time'] = "2020-01-10 12:00:00"
        if status == '2':
            commodity_list = RelActivityCommodity.objects.filter(activity_id=item.id).values('commodity')
            commoditylist = []
            for commodity_dic in commodity_list:
                commodity = CommodityDetail.objects.get(id=commodity_dic['commodity'])
                p = {}
                p["product_id"] = commodity.id
                p["product_name"] = commodity.commodity_name
                p["price"] = commodity.commodity_price
                p["amount"] = 100
                p["description"] = commodity.commodity_info
                p["image_url"] = CommodityImage.objects.filter(commodity_id=commodity.id).first().image_url.url
                p["status"] = commodity.commodity_status
                p["three_category_id"] = commodity.commodity_type.id
                two_category = commodity.commodity_type.parent
                if two_category:
                    p["two_category_id"] = two_category.id
                    one_category = two_category.parent
                    if one_category:
                        p["one_category_id"] = one_category.id
                    else:
                        p["one_category_id"] = None
                else:
                    p["two_category_id"] = None
                    p["one_category_id"] = None
                p["sold_out"] = len(OrderDetail.objects.filter(commodity_id=commodity.id).all())
                commoditylist.append(p)
            data['prduct_list'] = commoditylist
        else:
            data['prduct_list'] = "[...]"

        datalist.append(data)

    response_body = b_response_body
    response_body['data'] = datalist
    return JsonResponse(response_body)


def get_activities(request: HttpRequest, id):
    datalist = []
    commodity_list = RelActivityCommodity.objects.filter(activity_id=id).values('commodity')
    for commodity_dic in commodity_list:
        commodity = CommodityDetail.objects.get(id=commodity_dic['commodity'])
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
