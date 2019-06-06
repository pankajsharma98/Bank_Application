user1={
        'name':'ajay',
        'balance':3000,
        'password':'qwer',
    }

user2={
        'name':'babu',
        'balance':4000,
        'password':'asdf',
    }

user3={
        'name':'pankaj',
        'balance':5000,
        'password':'sharma',
    }

import shelve

db=shelve.open("database/users_data",writeback=True)

db['1001'] = user1
db['1002'] = user2
db['1003'] = user3

db['last_acc'] = 1003

db.close()

print("Data Exported Sucessfully")
