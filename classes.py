import random
from httpError import http_error

httpErrors = [400, 404, 414]
status = random.choice(httpErrors)

print(status)

# match status:
#         case 400:
#             print("Bad request")
#         case 404:
#             print("Not found")
#         case 414:
#             print("I am a teapot")
#         case _:
#             print("Something's wrong with the internet")

http_error(status)


