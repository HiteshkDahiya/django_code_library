from django.http import HttpResponse


class My_Middleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print('This is one Time initialization.')

    def __call__(self,request):
        print('This is before view call')
        response = self.get_response(request)
        print('This is after view call')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('This is process view before view')
        return HttpResponse("This is process view")
        # return None

    def process_exception(self, request, exception):
        print("an exception occured")
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        return HttpResponse(msg)

    def process_template_response(self, request, response):
        print('This is process template response')
        response.context_data['name'] = 'Sanjay'
        return response