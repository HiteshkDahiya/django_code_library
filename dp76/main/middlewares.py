def my_middleware(get_response):
    print("One Time Initialization!!")
    def my_function(request):
        print('code before view')
        response = get_response(request)
        print('code after view')
        return response
    return my_function

def my_middleware2(get_response):
    print("One Time Initialization2!!")
    def my_function(request):
        print('code before view2')
        response = get_response(request)
        print('code after view2')
        return response
    return my_function