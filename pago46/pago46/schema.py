import graphene
from graphene_django import DjangoObjectType
from users.models import User
from finance.models import IOU
from datetime import datetime
class UserType(DjangoObjectType):
    class Meta:
        model= User
        fields=["last_name"]

class IOUType(DjangoObjectType):
    class Meta:
        model=IOU
        fields= ["lender", "borrower", "value", "expiration"]

class Query(graphene.ObjectType):
    all_iou = graphene.List(IOUType)
    all_users = graphene.List(UserType)
    all_expired_iou = graphene.List(IOUType)
    expired_iou_by_lender = graphene.List(IOUType, lender_id=graphene.Int())
    expired_iou_by_borrower = graphene.List(IOUType, borrower_id=graphene.Int())
    expired_iou_by_datetime = graphene.List(IOUType, date_time=graphene.String())

    def resolve_all_expired_iou(root,info):
        return IOU.objects.filter(expiration__gt=datetime.now())
    def resolve_all_expired_iou_by_lender(root,info,lender_id):
        return IOU.objects.filter(lender_id=lender_id)
    def resolve_all_expired_iou_by_borrower(root,info,borrower_id):
        return IOU.objects.filter(borrower_id=borrower_id)
    def resolve_all_expired_iou_by_datetime(root,info,date_time):
        return IOU.objects.filter(expiration__gt=date_time)

    def resolve_all_iou(root,info):
        return IOU.objects.all()
    def resolve_all_users(root,info):
        return User.objects.all()
    def resolve_iou_by_lender(root,info, id):
        try:
            IOU.objects.get(lender_id=id)
        except IOU.DoesNotExist:
            return None
    def resolve_iou_by_borrower(root,info, id):
        try:
            IOU.objects.get(borrower_id=id)
        except IOU.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)