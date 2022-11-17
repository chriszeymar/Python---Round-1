from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

@api_view(['GET'])
def get_params():
    """
    """
    #request and capture Json response
    data = requests.get(http://127.0.0.1:8000/get_params?name=John&surname=Doe)
    json_data = data.json()
    
    #isolate
    item_list = json_data.get('data')
    
    content = {
        for item in itemlist:
            name = item['name']
            surname = item['surname']
    }
    return Response(content, status=status.HTTP_200_OK)
