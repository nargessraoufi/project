from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def converter(request):
    vlaue = request.data.get ("value")
    from_unit = request.data.get ("from_unit")
    to_unit = request.data.get ("to_unit")
    units = {'kg': 1,
            'gr': 1000,
            'mg': 1000000,
            'ton': 0.001,
            'lb': 2.20462,
            'oz': 35.274}
    baseValue = vlaue / units[from_unit]
    result = baseValue * units[to_unit]

    if vlaue is None:
        return Response({"error": "لطفاً مقدار را وارد کنید."}, status=400)
    
    if from_unit is None:
        return Response({"error": "لطفاً واحد مبدا را وارد کنید."}, status=400)
    
    if to_unit is None:
        return Response({"error": "لطفاً واحد مقصد را وارد کنید."}, status=400)
    
    try:
        vlaue = float(vlaue)
    except ValueError:
        return Response({"error": "یک مفدار عددی وارد کنید."}, status=400)


    return Response({'result': result})

