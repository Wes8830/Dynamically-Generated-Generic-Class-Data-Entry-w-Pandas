from generics import GenericORM

class Something:
    pass


item1 = Something()

setattr(item1, 'item', 'value')



print(item1.item)

item1.this = "this attribute"
item1.andthat = "attribute"
print(item1.this)
print(item1.andthat)

print(dir(item1))


item = GenericORM(
    datas = "some generic basic ORM object",
    description = "this is a description",
    field = 'a new field'
)

print(item)
print(item.datas, item.description, item.field)

