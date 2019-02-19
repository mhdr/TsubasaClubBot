from db.users import Users
from pprint import pprint

users=Users()

print(users.count_join())

users_join=users.find_start_join()
for u in users_join:
    pprint(u)