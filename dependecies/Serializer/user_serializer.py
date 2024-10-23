def user_response_serializer(data):
    return{
        "user_id":data.user,
        "first_name":data.first_name,
        "last_name":data.last_name,
        "age":data.age,
        "occupation":data.occupation
    }

def user_login_serializer(data):
    return{
        "user_id":data.user_id
    }