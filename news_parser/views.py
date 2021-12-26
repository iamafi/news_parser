from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from news_parser.serializers import ParserSerializer
from news_parser.utils import gazeta_scraper, daryo_scraper, kun_scraper


class ParseNews(APIView):
    def post(self, request, *args, **kwargs):
        parser = ParserSerializer(data=request.data)
        if parser.is_valid():
            source = parser.validated_data["source"]
            if source == 'gazeta':
                return Response(data={'description': 'hehe'})
            elif source == 'daryo':
                return Response(data={'description': daryo_scraper(parser.validated_data["url"])})
            elif source == 'kun':
                return Response(data={'description': kun_scraper(parser.validated_data["url"])})

        return Response(data={'message': 'not valid', 'status': False})
