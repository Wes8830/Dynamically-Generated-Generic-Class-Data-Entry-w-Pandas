from generics import GenericORM

item = GenericORM(
    datas = "some generic basic ORM object",
    description = "this is a description",
    field = 'a new field'
)

print(item)
print(item.datas, item.description, item.field)

