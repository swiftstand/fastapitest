from fastapi import FastAPI
from graphene import ObjectType, List, String, Schema, Int, Field
from graphql.execution.executors.asyncio import AsyncioExecutor
from pydantic import Field
from starlette.graphql import GraphQLApp
from schemas import ProductType
import json



class Query(ObjectType):
    product_list = None
    get_products = List(ProductType,{"id":Int(), "category":String()})
    async def resolve_get_products(self,info,id=None, category= None):
        with open('./items.json') as products:
            product_list = json.load(products)
        if (id):
            for item in product_list:
                if item["id"] == id:
                    return [item]

        if (category):
            return [item for item in product_list if item["category"] == category]

        return product_list

app = FastAPI()

app.add_route('/', GraphQLApp(
    schema=Schema(query=Query),
    executor_class=AsyncioExecutor
))



