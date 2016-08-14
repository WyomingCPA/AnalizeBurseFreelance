from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from FreelanceAds.models import FreelanceAds
from lxml import etree, html
import requests
import json


class Command(BaseCommand):
    help = 'Get Ads'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0'}

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.GetFreelanceParser()
            
      
    def GetFreelanceParser(self):
        """
        https://freelance.ru
        """
        try:     
            i = 1
            while (i < 4):
                self.frelance(i)
                i += 1
        except:
            print 'Error freelance.ru'

        """
        https://www.weblancer.net/
        """
        try:     
            i = 1
            while (i < 4):
                self.weblancer(i)
                i += 1
        except:
            print 'Error https://www.weblancer.net/'




    def frelance(self, page):
        """
        https://freelance.ru
        """
        session = requests.Session()
        session.headers = self.headers

        getPageFreelance = session.get("https://freelance.ru/projects/filter/?page=%s" % page )
        pageHtml = html.fromstring(getPageFreelance.text)
        getAllTitleBlock = pageHtml.xpath(".//*[@id='col_center']/div/div[1]/div")

        listObjFreelance = []
        for TitleBlock in getAllTitleBlock:
            title = TitleBlock.xpath(".//*[@class='ptitle']/span")[0].text
            href = TitleBlock.xpath(".//*[@class='ptitle']")[0].attrib['href']
            link = 'https://freelance.ru' + href

            try:
                FreelanceAds.objects.get(link=link)

            except FreelanceAds.MultipleObjectsReturned:
                pass
            except FreelanceAds.DoesNotExist:                    
                itemAds = FreelanceAds(title = title, text = '', site = 'https://freelance.ru', link = link)
                itemAds.save()

    def weblancer(self, page):
        """
        https://www.weblancer.net/
        """
        session = requests.Session()
        session.headers = self.headers
        
        getPageWeblancer = session.get("https://www.weblancer.net/projects/?page=%s" % page)
        pageHtml = html.fromstring(getPageWeblancer.text)
        getAllTitleBlock = pageHtml.xpath(".//*[@class='title']")

        for TitleBlock in getAllTitleBlock:
            href = TitleBlock.attrib['href']
            title = TitleBlock.text
            link = 'https://www.weblancer.net' + href
            try:
                FreelanceAds.objects.get(link=link)

            except FreelanceAds.MultipleObjectsReturned:
                pass
            except FreelanceAds.DoesNotExist:                    
                itemAds = FreelanceAds(title = title, text = '', site = 'https://www.weblancer.net', link = link)
                itemAds.save()
