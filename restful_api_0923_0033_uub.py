# 代码生成时间: 2025-09-23 00:33:43
import pandas as pd
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

# 创建 Flask 应用
app = Flask(__name__)
api = Api(app)

# 示例数据集
data = {
    "users": [
        {
            "id": 1,
            "name": "John",
            "age": 30,
            "city": "New York"
        },
        {
            "id": 2,
            "name": "Doe",
            "age": 50,
            "city": "Los Angeles"
        },
        {
            "id": 3,
            "name": "Alice",
            "age": 28,
            "city": "Chicago"
        },
    ]
}

class User(Resource):
    """ 用户资源类 \