from django.http import JsonResponse
import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import FileResponse

# Create your views here.


def Home(request):
    x = os.getcwd()
    print(x)
    os.environ["PYTHONPATH"] = "/code"
    x = os.environ
    # return JsonResponse(
    #     {
    #         "PYTHONPATH": os.environ.get("PYTHONPATH"),
    #         "PATH": os.environ.get("PATH"),
    #         "DATA":
    #     }
    # )
    response = FileResponse(open("data/otodom_05_06_2022.json", "rb"))
    return response


@api_view(["GET"])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        return Response({})
