from bs4 import BeautifulSoup
from urllib.request import urlopen

from datetime import date

from openpyxl import load_workbook


# Global vars
urlToParse = u"https://www.amazon.com.br/Resist%C3%AAncia-dos-materiais-R-Hibbeler-ebook/dp/B07WH4677K/ref=sr_1_1?qid=1573499147&refinements=p_27%3AR.+C.+Hibbeler&s=digital-text&sr=1-1"
urlToParse = u"https://www.amazon.com.br"

originalSpeadsheet = "aquisicaodelivros.xlsx"

DEBUG_FLAG = False

class Request:
    def __init__(self):
        self.library = None
        self.branchLine = None
        self.email = None
        self.email = None
        self.date = None

    def getMetaData(self):
        self.library        = input("Insira o nome da Biblioteca: ")
        self.branchLine     = input("Insira o ramal: ")
        self.email          = input("Insira o seu e-mail: ")
        self.responsible    = input("Insira o nome do responsável pela solicitação: ")
        self.date           = date.today()

    def getLinks(self):
        #TODO implement
        pass

    def __str__(self):
        out = ""
        out += "This is a resquest. Attrs:"
        out += str(vars(self))
        return out

def openUrlAndSoup(url):
    #TODO catch para urllib.error.URLError
    with urlopen(url) as response:
        soup = BeautifulSoup(response, 'html.parser')
    return soup

def anchorAndGet(soup):
    # TODO entender isso aqui:
    for anchor in soup.find_all('a'):
        a = anchor.get('href', '/')
    print(type(a))

def debug(str):
    if DEBUG_FLAG:
        print(str)

def main():
    request = Request()
    #request.getMetaData()
    #print(request)

    wb = load_workbook(originalSpeadsheet)
    #print(wb.sheetnames)

    #soup = openUrlAndSoup(urlToParse)
    #anchorAndGet(soup)

if __name__ == "__main__":
    main()