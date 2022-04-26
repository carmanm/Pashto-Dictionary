import tkinter as tk
from tkinter import *
import requests
from bs4 import BeautifulSoup as bs4
import xlrd
import sys
import codecs



#Mazaar dictionary and thePashto.com search
class Search:

    def excelWebSearch(self, dictRequest):

        global word_list_format

        word_list_format = []
        word_list_format = list(set(word_list_format))

        page = requests.get('http://thepashto.com/word.php?english=' + str(dictRequest))
        pageName = 'http://thepashto.com/word.php?english=' + str(dictRequest)
        soup = bs4(page.text, 'html.parser')
        
        word_list = soup.find('span', {'itemprop' : 'articleBody'})


        if  word_list is None:
            word_list_items = []
            
        else:
            word_list_items = word_list.findAllNext('span', {'itemprop' : 'articleBody'})
            
        if len(word_list_items) >= 1 and word_list is not None:
            word_list_items = word_list.findAllNext('span', {'itemprop' : 'articleBody'})
            for item in word_list_items:
                word_list_format.append(
                    str(item).replace('<span itemprop="articleBody">', '').replace('</span>', '')
                    )

        elif len(word_list_items) == 0 and word_list is not None:
            word_list_format.append(
                    str(word_list).replace('<span itemprop="articleBody">', '').replace('</span>', '')
                    )
        else:
            pass
#        print(word_list_format)

    def __init__(self):

        global e1
        global Lb
        global currRow_d 
        global cVal
        fullList = []
        text_file = open("corncob_lowercase.txt", "r")
        lines = text_file.readlines()
        txt = open('D:\pashtoDictionary\DICTIONARY.txt', 'w')
        for index, item in zip(range(19), lines):
            item_1 = item.replace('\n', '')
            if index <=99:
                self.excelWebSearch(item)
              #  print(word_list_format)
                for word in word_list_format:
                    print(item_1 + ', ' + word)    
                    fullList.append(str(item_1.encode('utf-8') + ', '.encode('utf-8') + word.encode('utf-8')))
                item_1 = item.replace('\n', '')
                print(str(index) + item_1)
            else:
                break

        for obj in fullList:
            txt.write(obj + '\n')
        open('DICTIONARY.txt', 'w').close()
        print(open("DICTIONARY.txt", "r").readlines())
        print("DECODING")
        dictTxt = codecs.open('DICTIONARY.txt', encoding='utf-8')
        print(dictTxt)
        for line in dictTxt:
            print(line)
        for line in open("DICTIONARY.txt", "r"):
            l = line.decode('utf-8')
            print(l)
        
        



def main():
       
        Search()
    

if __name__ == "__main__": main()
