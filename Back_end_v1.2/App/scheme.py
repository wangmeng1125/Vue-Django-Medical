from ninja import Schema


# 用户信息约束模式

# 正常找到用户信息的模式
class UserSchema(Schema):
    name: str
    password: str
    age: int


class AdminSchema(Schema):
    username: str
    password: str


# 如果没有找到用户信息的模式
class NotFoundSchema(Schema):
    message: str


# 算法信息约束模式

# 算法视图
class AlgoritmSchema(Schema):
    algoritm_name: str
    type: str


# 模型视图
class ModelSchema(Schema):
    model_name: str
    type: str
