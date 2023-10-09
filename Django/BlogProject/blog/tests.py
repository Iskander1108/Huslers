context= {
    "posts": [
        ("Django", "apple", "123", "22222"),
        ("Fifa", "apple", "321", "3333"),
        ("ITC", "apple", "12", "4444"),
        ("jjj", "sms", "31", "5555"),
        ("loy", "mms", "41", "6666"),
       
    ]
}

for posts in context["posts"]:
    print(f"{posts[0]}")
