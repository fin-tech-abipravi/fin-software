from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers
import json
from datetime import datetime, timedelta
from accounts.models import AuthTFfield
from accounts.serializers import Authserializers
# Importing Models.

from . models import (Costumerdetails, Collectionlist, Dlammounts, Ammountinhand, Expence, Expencetotal, Closeup,
                      Closedown, Otherammountin, Otherammountout, Inversment, Others)

# importing serializers.
from . serializers import (Costumerdetailsserializer, Collectionlistserializer, Dlammountsserializer, Ammountinhandserializer,
                           Expencetotalserializer,
                           Expenceserializer, Closeupserializer, Closedownserializer, Otherammountinserializer, Otherammountoutserializer, Inversmentserializer,
                           Othersserializer)


def check_auth(Authkey):
    # getting current date and time for validating the token expire time
    present_time = datetime.now()
    '{:%H:%M:%S}'.format(present_time)
    updated_time = datetime.now()
    if AuthTFfield.objects.filter(Auth=Authkey):
        Auth = AuthTFfield.objects.get(Auth=Authkey)
        serializer = Authserializers(Auth, many=False)
        expire_time = serializer.data.get('expires')
        # remove the z from the output time
        expire_time = expire_time.replace('Z', "")
        # Converting datetime form string format to Date Time format for verifing the expiring time
        expire_time = datetime.strptime(expire_time, '%Y-%m-%dT%H:%M:%S.%f')
        # checking wheather the current time is greater the expire time is true it will not login else it will login return the data to the user
        if updated_time > expire_time:
            return False
        else:
            return True


def apiloginview(request):
    return render(request, "index.html")


@api_view(['GET'])
def getCostumer(request, pk):
    if check_auth(pk) == True:
        data = Costumerdetails.objects.all()
        serializer = Costumerdetailsserializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse("Invalid Data", safe=False)


@api_view(['POST'])
def createcostumer(request, pk):
    if check_auth(pk) == True:
        serializer = Costumerdetailsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(request.data)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse(request.data, safe=False)


@api_view(['DELETE'])
def deletecostumer(request, pk, tk):
    if check_auth(tk) == True:
        data = Costumerdetails.objects.get(id=pk)
        data.delete()
        return JsonResponse("Costumer deleted successfully.", safe=False)
    else:
        return JsonResponse("{'request' : 'failed', 'User' : 'User token invalid'}", safe=False)


@api_view(['POST'])
def updatecostumer(request, pk):
    data = Costumerdetails.objects.get(id=pk)
    serializer = Costumerdetailsserializer(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


'''
============================================================================================================================
Collection List Viewes
============================================================================================================================
'''


@api_view(['GET'])
def getcollection(request, tk):
    if check_auth(tk) == True:
        data = Collectionlist.objects.all()
        serializer = Collectionlistserializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse(request.data, safe=False)


@api_view(['GET'])
def getcollectiondetail(request, pk):
   user_lists = (Collectionlist.objects
    .filter(costumer_id = pk)
    .values('ammount', 'costumer_id', 'costumer_name', 'date', 'id')  # all fields you need
    )
   person = serializers.serialize("json", Collectionlist.objects.filter(costumer_id = 25))
   list_data_json = json.dumps(list(user_lists))
   print(user_lists)
   return JsonResponse(list_data_json, safe=False)


@api_view(['POST'])
def createcollection(request, tk):
    if check_auth(tk) == True:
        serializer = Collectionlistserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print("not")
            print(f'\n{serializer.data}\n')
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse("Create Collection Error", safe=False)


@api_view(['DELETE'])
def deletecollection(request, pk):
    data = Collectionlist.objects.get(id=pk)
    data.delete()
    return JsonResponse("Collection deleted successfully.", safe=False)


@api_view(['POST'])
def updatecollection(request, pk):
    data = Collectionlist.objects.get(id=pk)
    serializer = Collectionlistserializer(instance=data, data=request.data)
    print(data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


'''
============================================================================================================================
Expence Table Viewes
============================================================================================================================
'''


@api_view(['GET'])
def getExpence(request):
    data = Expence.objects.all()
    serializer = Expenceserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getExpencedetail(request, pk):
    data = Expence.objects.get(id=pk)
    serializer = Expenceserializer(data, many=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def createExpence(request):
    serializer = Expenceserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print('not')
        print(serializer.data)
    return JsonResponse(serializer.data, safe=False)


@api_view(['DELETE'])
def deleteExpence(request, pk):
    data = Expence.objects.get(id=pk)
    data.delete()
    return JsonResponse("Collection deleted successfully.", safe=False)


@api_view(['POST'])
def updateExpence(request, pk):
    data = Expence.objects.get(id=pk)
    serializer = Expenceserializer(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


'''
============================================================================================================================
Expence Total Table Viewes
===========================================================================================================================w
'''


@api_view(['GET'])
def getExpencetotal(request):
    data = Expencetotal.objects.all()
    serializer = Expencetotalserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getExpencedetailtotal(request, pk):
    data = Expencetotal.objects.get(id=pk)
    serializer = Expencetotalserializer(data, many=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def createExpencetotal(request):
    serializer = Expencetotalserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.data)
    return JsonResponse(serializer.data, safe=False)


@api_view(['DELETE'])
def deleteExpencetotal(request, pk):
    data = Expencetotal.objects.get(id=pk)
    data.delete()
    return JsonResponse("Collection deleted successfully.", safe=False)


@api_view(['POST'])
def updateExpencetotal(request, pk):
    data = Expencetotal.objects.get(id=pk)
    serializer = Expenceserializer(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.data)
    return JsonResponse(serializer.data, safe=False)


'''
============================================================================================================================
DL ammount Data Table Viewes
===========================================================================================================================w
'''


@api_view(['GET'])
def getDl(request):
    data = Dlammounts.objects.all()
    serializer = Dlammountsserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getDldetail(request, pk):
    data = Dlammounts.objects.get(id=pk)
    serializer = Dlammountsserializer(data, many=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def createDl(request):
    serializer = Dlammountsserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer)
    else:
        print(serializer)
    return JsonResponse(serializer.data, safe=False)


@api_view(['DELETE'])
def deleteDl(request, pk):
    data = Dlammounts.objects.get(id=pk)
    data.delete()
    return JsonResponse("dl deleted successfully.", safe=False)


@api_view(['POST'])
def updateDl(request, pk):
    data = Dlammounts.objects.get(id=pk)
    serializer = Dlammountsserializer(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


'''
============================================================================================================================
ammount in hand Data Table Viewes
===========================================================================================================================w
'''


@api_view(['GET'])
def getaih(request):
    data = Ammountinhand.objects.all()
    serializer = Ammountinhandserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getaihdetail(request, pk):
    data = Ammountinhand.objects.get(id=pk)
    serializer = Ammountinhandserializer(data, many=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def createaih(request):
    serializer = Ammountinhandserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def updateaih(request, pk):
    data = Ammountinhand.objects.get(id=pk)
    serializer = Ammountinhandserializer(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


'''
============================================================================================================================
Close up Data Table Viewes
===========================================================================================================================w
'''


@api_view(['GET'])
def getcloseup(request):
    data = Closeup.objects.all()
    serializer = Closeupserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getcloseupdetail(request, pk):
    data = Closeup.objects.get(id=pk)
    serializer = Closeupserializer(data, many=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def createcloseup(request):
    serializer = Closeupserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("not")
        print(serializer.data, safe=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def updatecloseup(request, pk):
    data = Closeup.objects.get(id=pk)
    serializer = Closeupserializer(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


'''
============================================================================================================================
Close down Data Table Viewes
===========================================================================================================================w
'''


@api_view(['GET'])
def getclosedown(request):
    data = Closedown.objects.all()
    serializer = Closedownserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getclosedowndetail(request, pk):
    data = Closedown.objects.get(id=pk)
    serializer = Closedownserializer(data, many=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def createclosedown(request):
    serializer = Closedownserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def updateclosedown(request, pk):
    data = Closedown.objects.get(id=pk)
    serializer = Closedownserializer(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


'''
============================================================================================================================
Other Ammount in Data Table Viewes
===========================================================================================================================w
'''


@api_view(['GET'])
def getoai(request):
    data = Otherammountin.objects.all()
    serializer = Otherammountinserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getoaidetails(request, pk):
    data = Otherammountin.objects.get(id=pk)
    serializer = Otherammountinserializer(data, many=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def createoai(request):
    serializer = Otherammountinserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def updateoai(request, pk):
    data = Otherammountin.objects.get(id=pk)
    serializer = Otherammountinserializer(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


'''
============================================================================================================================
Other Ammount Out Data Table Viewes
===========================================================================================================================w
'''


@api_view(['GET'])
def getoao(request):
    data = Otherammountout.objects.all()
    serializer = Otherammountoutserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getoaodetails(request, pk):
    data = Otherammountout.objects.get(id=pk)
    serializer = Otherammountoutserializer(data, many=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def createoao(request):
    serializer = Otherammountoutserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def updateoao(request, pk):
    data = Otherammountout.objects.get(id=pk)
    serializer = Otherammountoutserializer(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


'''
============================================================================================================================
Inversment Data Table Viewes
===========================================================================================================================w
'''


@api_view(['GET'])
def getinversment(request):
    data = Inversment.objects.all()
    serializer = Inversmentserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getinversmentdetails(request, pk):
    data = Inversment.objects.get(id=pk)
    serializer = Inversmentserializer(data, many=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def createinversment(request):
    serializer = Inversmentserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def updateinversment(request, pk):
    data = Inversment.objects.get(id=pk)
    serializer = Inversmentserializer(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


'''
============================================================================================================================
Others Data Table Viewes
===========================================================================================================================w
'''


@api_view(['GET'])
def getothers(request):
    data = Others.objects.all()
    serializer = Othersserializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getothersdetails(request, pk):
    data = Others.objects.get(id=pk)
    serializer = Othersserializer(data, many=False)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def createothers(request):
    serializer = Othersserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def updateothers(request, pk):
    data = Others.objects.get(id=pk)
    serializer = Othersserializer(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def api_docs(request):
    docs = {
        'costumer/auth/ => CRUD; getcostumerdetail/<id> {for get detail of the costumer with id} and use get, create, update, delete',
        'collection => CRUD; getcollectiondetail/<id> {for get detail of the collection with id} and use get, create, update, delete',
        'expence => CRUD; getexpencedetail/<id> {for get detail of the expence with id} and use get, create, update, delete',
        'expencetotal => CRUD; getexpencetotaldetail/<id> {for get detail of the expencetotal with id} and use get, create, update, delete',
        'dl => CRUD; getdldetail/<id> {for get detail of the dl with id} and use get, create, update, delete',
        'aih => CRU not delete; getaihdetail/<id> {for get detail of the ammount in hand with id} and use get, create, update',
        'closeup => CRU not delete; getcloseupdetail/<id> {for get detail of the closeup with id} and use get, create, update',
        'closedown => CRU not delete; getclosedowndetail/<id> {for get detail of the closedown with id} and use get, create, update',
        'oao => CRU not delete; getoaodetail/<id> {for get detail of the oao with id} and use get, create, update',
        'oai => CRU not delete; getoaidetail/<id> {for get detail of the oai with id} and use get, create, update',
        'inversment => CRU not delete; getinversmentdetail/<id> {for get detail of the inversment with id} and use get, create, update',
        'others => CRU not delete; getothersdetail/<id> {for get detail of the others with id} and use get, create, update',
    }
    return Response(docs)