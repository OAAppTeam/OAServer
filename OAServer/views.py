__author__ = 'Justin'

from django.http import HttpResponse
from OAServer.models import TestModel
import json

def post_only(func):
    """ Ensures a method is post only """
    def wrapped_f(request):
        if request.method != "POST":
            response = HttpResponse(json.dumps(
                {"error": "this method only accepts posts!"}))
            response.status_code = 500
            return response
        return func(request)
    return wrapped_f

# Create your views here.
@post_only
def test_view(request):
    posts = TestModel.objects.all()
    j = {"aa":"test"}
    return HttpResponse(json.dumps(j))