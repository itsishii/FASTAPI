##using get
from data import product
from fastapi import FastAPI
from database import getData,add_data,update_data,delete_data
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:3000"],
                   allow_methods=['*']
    
)
products=[
    product(id=1,name='laptop',description='dell laptop',price=150,quantity=10),
    product(id=2,name='laptop',description='apple laptop',price=250,quantity=15),
    product(id=3,name='laptop',description='apple laptop',price=280,quantity=16),
    product(id=4,name='laptop',description='apple laptop',price=260,quantity=17)
]

'''@app.get('/')
def getData():
    return "welcome to home"

@app.get('/newPage')
def getData():
    return "welcome to new page"
'''

@app.get('/products/')
def get_products():
    return getData()

@app.get('/products/{id}')
def get_products(id:int):
    for i in products:
        if i.id==id:
            return i
        return "404"

@app.post('/products/')
def add_product(product:product):
    return add_data(product)

@app.put('/products/{id}')
def update_products(id:int,product:product):
    return update_data(id,product)
    '''
    for i in range(len(products)):
        if products[i].id==id:
            products[i]=product
            return 'update successfully'
    return 'product not found'
    '''

@app.delete('/products/{id}')
def del_product(id:int):
    return delete_data(id)
    
    '''
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return 'done'
    return 'fail'
    '''