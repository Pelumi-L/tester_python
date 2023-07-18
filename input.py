#person = []
# for i in range(1, 5):
#     username = input("username: ")
#     password = input("password: ")
#     person.append({username, password})
#     print(person)
# num = [1, 2, 3, 4]
# for i in num:
#     username = input("username: ")
#     password = input("password: ")
#     person.append({username, password})
#     print(person)
profiles = [
    {
        "username":"pelzz",
        "fname":"pelumi",
        "lastname":"sam",
        "age":23,
        "gender":"male",
        "email":"pelumi@email.com",
        "class":[
            {"beginner"},
            {"intermediate"},
            {"advance"}
        ],
        "password":1234,
        "status":True
    },
    {
        "username":"john01",
        "fname":"john",
        "lastname":"doe",
        "age":33,
        "gender":"male",
        "email":"john@email.com",
        "class":[
            {"beginner"},
            {"intermediate"},
            {"advance"}
        ],
        "password":"12jones",
        "status":False
    },
    {
        "username":"pilo0",
        "fname":"philip",
        "lastname":"pesa",
        "age":43,
        "gender":"female",
        "email":"philip@email.com",
        "class":[
            {"beginner"},
            {"intermediate"},
            {"advance"}
        ],
        "password":"12stones",
        "status":True
    }
]
#print(profiles[1]["fname"] + " is in the " + profiles[1]["class"][1] + " class")
username = input("enter your username: ")
profile_length = len(profiles)
for profile in profiles:
    if profile["username"] == username or profile["fname"] == username:
        print("welcome " + username)
        break;
    # elif profile["fname"] == username:
    #     print("welcome " + username)
    #     break;
    else:
        print(username + " please register")
        break;