#!/usr/bin/env python
# -*- coding: utf-8 -*-
#### ukbsearch.py
#### made by Daniel Minseok Kwon
#### 2022-03-18 03:08:40
#########################
import sys
import os
# import pandas as pd
from ims import file_util
from ims import str_util
from prettytable import PrettyTable


COLNAMES = ["Column", "UDI", "Count", "Type", "Description"]

class BLOCK:
    rows = []
    size = 0
    htmlfile = ""
    description = ""

    def __init__(self, htmlfile):
        self.htmlfile = htmlfile
        self.feid = htmlfile.split('/')[-1].replace('.html', '').strip()
        self.rows = []
        self.size = 0
        self.desciption = ""

    def add(self, row):
        if len(self.rows) == 0:
            self.description = row['Description']
        self.rows.append(row)
        self.size = len(self.rows)

    def print(self):
        x = PrettyTable()
        x.field_names = COLNAMES
        for row in self.rows:
            listrow = []
            for cn in COLNAMES:
                try:
                    listrow.append(row[cn])
                except KeyError:
                    listrow.append('')
            x.add_row(listrow)
        # print(self.rows)
        print(x)

    def get_listrows(self):
        listrows = []
        for row in self.rows:
            listrow = []
            for cn in COLNAMES:
                try:
                    listrow.append(row[cn])
                except KeyError:
                    listrow.append('')
            listrows.append(listrow)
        return listrows


class DATA:
    html_list = []
    total_col = 0
    blocklist = []

    def __init__(self):
        self.html_list = []
        self.total_col = 0
        self.blocklist = []
        
    def set_html_list(self, path = './'):
        self.html_list = file_util.walk(path, '.html')

    def load_html_list(self, path = './'):
        self.set_html_list(path)

        for htmlfile in self.html_list:
            self.load_html(htmlfile)

        print("\tTotal_columns:", self.total_col)
            

    def load_html(self, htmlfile):
        flag = False
        no_row = 0
        no_col = 0
        block = BLOCK(htmlfile)
        for line in open(htmlfile):
            if "</table" in line:
                flag = False

            if flag:
                no_row += 1
                arr = line.strip().split('</td>')
                row = {}
                for k in range(len(arr)-1):
                    if COLNAMES[k] == "Description":
                        # row[COLNAMES[k]]= arr[k]
                        row[COLNAMES[k]]= str_util.strip_tag(arr[k])
                    else:
                        row[COLNAMES[k]]= str_util.strip_tag(arr[k])
                if len(row) > 3:
                    if block.size > 0:
                        self.blocklist.append(block)
                        no_col += block.size
                    block = BLOCK(htmlfile)
                    block.add(row)
                else:
                    block.add(row)
            if not flag:
                flag2 = True
                for col in COLNAMES:
                    if not col in line:
                        flag2 = False
                if flag2:
                    flag = True
        if block.size > 0:
            self.blocklist.append(block)
            no_col += block.size

        self.total_col += no_col
        print("\tloaded", htmlfile, "no_columns:", no_col)


    def search_description(self, term):
        x = PrettyTable()
        x.field_names = COLNAMES
        for block in self.blocklist:
            if term in block.description:
                # block.print()
                x.add_rows(block.get_listrows())
        x.align["Column"] = "r"
        x.align["Count"] = "r"
        x.align["Description"] = "l"
        print(x)



def ukbsearch():
    data = DATA()
    data.load_html_list('./')
    data.search_description('age')



if __name__ == "__main__":
    print ("USAGE: python ukbsearch.py age")
    print(sys.argv[1])
    ukbsearch()
