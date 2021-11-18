from rest_framework.decorators import api_view
from rest_framework.response import Response

from .data import ExampleData, memory

def validate_data(data):
    try:
        id = data['id']
        title = data['title']
        problem = data['problem']
        point = int(data['point'])
        level = data['level']
        language = data['language']
        input_ = data['input']
        expected_output = data['expected_output'] 
        return (id, title, problem, point, level, language, input_, expected_output)
    except:
        err_msg = """
            Hatalı Veri [id,title,problem,point,level,language,input,excepted_output alanları zorunludur]
        """.strip('\n').lstrip('\n').strip()
        return {
            "Hata": err_msg
            }

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'list': '/data-list/',
        'create': '/data-create/',
        'update': '/data-update/<str:id>/',
        'delete': '/data-delete/<str:id>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def dataList(request):
    data = memory.get_data()
    return Response(data)

@api_view(['POST'])
def dataCreate(request):
    new_data = validate_data(request.data)
    if type(new_data) == dict:
        return Response(new_data)
    ex = ExampleData(
        id=new_data[0],
        title=new_data[1],
        problem=new_data[2],
        point=new_data[3],
        level=new_data[4],
        language=new_data[5],
        input=new_data[6],
        expected_output=new_data[7]
        )
    message = ex.save()
    return Response(message)

@api_view(['PUT'])
def dataUpdate(request, id):
    new_data = validate_data(request.data)
    if type(new_data) == dict:
        return Response(new_data)
    message = memory.update(id, request.data)
    return Response(message)

@api_view(['DELETE'])
def dataDelete(request,id):
    data = memory.delete(id)
    return Response(data)   