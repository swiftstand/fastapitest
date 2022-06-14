from fastapi import FastAPI
from graphene import ObjectType, List, String, Schema, Int, Field
from graphql.execution.executors.asyncio import AsyncioExecutor
from pydantic import Field
from starlette.graphql import GraphQLApp
from schemas import ProductType
import json



class Query(ObjectType):
    product_list = None
    products_details = List(ProductType,{"id":Int()})
    products_by_category = List(ProductType,{"category":String()})
    products_overview = List(ProductType)
    # async def resolve_products(self,info):
    #     with open('./items.json') as products:
    #         product_list = json.load(products)
    #     return product_list

    async def resolve_products_by_category(self,info,category= None):
        with open('./items.json') as products:
            product_list = json.load(products)
        if (category):
            return [item for item in product_list if item["category"] == category]

        return "Item with provided category doesn't exist"

    
    async def resolve_products_details(self,info,id=None):
        with open('./items.json') as products:
            product_list = json.load(products)
        if (id):
            for item in product_list:
                if item["id"] == id:
                    return [item]
            return "Item with provided id doesn't exist"

    async def resolve_products_overview(self,info):
        with open('./items.json') as products:
            product_list = json.load(products)
        return product_list

app = FastAPI()

app.add_route('/', GraphQLApp(
    schema=Schema(query=Query),
    executor_class=AsyncioExecutor
))



