from tasks import add

result = add.delay(4, 4)
result.ready()
print(result.get(timeout=100))