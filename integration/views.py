from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from integration.serializers import (
    FormSerializer
)


class HomeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        return Response({'hello': "hello"})


@api_view(('POST',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def form_view(request):
    dict = {
        'name': request.POST["name"],
        'email': request.POST["email"],
        'education': request.POST["education"],
        'gender': request.POST["gender"],
        'phone': request.POST["phone"],
        'type': request.POST["type"],
    }
    return Response({"status": True, "message": "success", "result": dict}, template_name='form.html')
