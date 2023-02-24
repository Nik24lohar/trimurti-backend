from product.models import Product , Card , selectedProduct
from product.serializers import ProductSerializer , CardSerializer , selectProductSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from rest_framework import status

class ProductListCreate(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def get(self, request,format = None): 
        product = Product.objects.all()
        print("product", product)
        if product.count()>0:
            product_data =ProductSerializer(data=product,many=True)
            product_data.is_valid()
            print("User Data:",product_data.data)
            return Response({"message":"product listed",'data':product_data.data,"status ": status.HTTP_201_CREATED})
        return Response({"message":"products not found",'data':product_data.data,"status ": status.HTTP_400_BAD_REQUEST})
    
    def post(self, request,format = None):
        print(request.data)
        product = ProductSerializer(data = request.data)
        if product.is_valid():
            product.save()
            return Response({"message":"product created",'data':product.data,"status":status.HTTP_200_OK})
        return Response({"message":"product fail to create",'data':product.errors,"status":status.HTTP_400_BAD_REQUEST})


class ProductUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def get(self,request,*args, **kwargs):
        productObj=Product.objects.get(filter=kwargs['id'])
        product_data=ProductSerializer(productObj)
        if product_data.data:
            return Response({"message":"product created",'data':product_data.data,"status":status.HTTP_200_OK})
        else:
            return Response({"message":"product not found",'data':product_data.data,"status":status.HTTP_400_BAD_REQUEST})
    def patch(self, request, *args, **kwargs):
            report = Product.objects.get(project=kwargs['id'])
            print(request.data)
            reportdata = ProductSerializer(report, data=request.data, partial=True)
            if reportdata.is_valid():
                reportdata.save()
                return Response({"message":"prodct data updated","data":reportdata.data,"status":status.HTTP_201_CREATED})
            return Response({"message":"prodct data is not updated","data":reportdata.errors,"status":status.HTTP_400_BAD_REQUEST})

    def put(self, request, *args, **kwargs):
            report = Product.objects.get(project=kwargs['id'])
            print(request.data)
            reportdata = ProductSerializer(report, data=request.data)
            if reportdata.is_valid():
                reportdata.save()
                return Response({"message":"product updated",'data':reportdata.data,"status":status.HTTP_200_OK})
            return Response({"message":"product is not updated","data":reportdata.errors,"status":status.HTTP_400_BAD_REQUEST})
    def delete(self,request,*args,**kwargs):
        try:
            report = Card.objects.get(project=kwargs['id'])
            report_data = CardSerializer(report)
            report.delete()
            return Response({"message":"deleted","deleted": report_data.data}, status=status.HTTP_202_ACCEPTED)
        except :
            return Response({"message":"fail to delete","deleted": report_data.data}, status=status.HTTP_400_BAD_REQUEST)
             
class CardListCreate(generics.ListCreateAPIView):
    queryset=Card.objects.all()
    serializer_class=CardSerializer
    def get(self, request,format = None): 
        card = Card.objects.all()
        print("card", card)
        if card.count()>0:
            card_data =CardSerializer(data=card,many=True)
            card_data.is_valid()
            print("User Data:",card_data.data)
            return Response({"message":"product listed",'productData':card_data.data,"status ": status.HTTP_201_CREATED})
        return Response({"message":"products not found",'productData':[],"status ": status.HTTP_400_BAD_REQUEST})
    
    def post(self, request,format = None):
        print(request.data['Id'])
        
        product=Product.objects.get(Id=request.data['Id'])
        product_data=ProductSerializer(product)
        if product_data.data:
            selectproduct = selectProductSerializer(data=product_data.data)
            if selectproduct.is_valid():
                selectproduct.save()
                return Response({"message":"Card created",'cardData':selectedProduct.data,"status":status.HTTP_200_OK})
        return Response({"message":"Card fail to create",'cardData':selectedProduct.errors,"status":status.HTTP_400_BAD_REQUEST})


class CardUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Card.objects.all()
    serializer_class=CardSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=Card_id']
    def get(self,request,*args, **kwargs):
        productObj=Card.objects.get(filter=kwargs['id'])
        product_data=CardSerializer(productObj)
        if product_data.data:
            return Response({"message":"card created",'data':product_data.data,"status":status.HTTP_200_OK})
        else:
            return Response({"message":"card not found",'data':product_data.data,"status":status.HTTP_400_BAD_REQUEST})
    def patch(self, request, *args, **kwargs):
            report = Card.objects.get(project=kwargs['id'])
            print(request.data)
            reportdata = CardSerializer(report, data=request.data, partial=True)
            if reportdata.is_valid():
                reportdata.save()
                return Response({"message":"card data updated","data":reportdata.data,"status":status.HTTP_201_CREATED})
            return Response({"message":"card data is not updated","data":reportdata.errors,"status":status.HTTP_400_BAD_REQUEST})

    def put(self, request, *args, **kwargs):
            report = Card.objects.get(project=kwargs['id'])
            print(request.data)
            reportdata = CardSerializer(report, data=request.data)
            if reportdata.is_valid():
                reportdata.save()
                return Response({"message":"card updated",'data':reportdata.data,"status":status.HTTP_200_OK})
            return Response({"message":"card is not updated","data":reportdata.errors,"status":status.HTTP_400_BAD_REQUEST})
    def delete(self,request,*args,**kwargs):
        try:
            report = Card.objects.get(project=kwargs['id'])
            report_data = CardSerializer(report)
            report.delete()
            return Response({"message":"deleted","deleted": report_data.data}, status=status.HTTP_202_ACCEPTED)
        except :
            return Response({"message":"fail to delete","deleted": report_data.data}, status=status.HTTP_400_BAD_REQUEST)
  



