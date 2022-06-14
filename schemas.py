from graphene import ObjectType, List, String, Schema, Int


class ProductType(ObjectType):
    id = String()
    name = String()
    price = Int()
    category = String()

