from celery import Celery


app = Celery('prueba', backend= 'amqp://quest:quest@localhost',broker= 'amqp://localhost')

@app.task
def add(x, y):
    return x + y

# para probar se ejecuta python por consola, luego:
# >>> from prueba import add
# >>> result = add.delay(5,7)
# >>> result.result
# 12
# >>>
