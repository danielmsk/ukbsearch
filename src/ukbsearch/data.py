
import re
from .conf import COLNAMES
from .block import BLOCK
from . import util



class DATA:
    html_list = []
    total_col = 0
    blocklist = []

    def __init__(self):
        self.html_list = []
        self.total_col = 0
        self.blocklist = []
        
    def set_html_list(self, path = './'):
        self.html_list = util.walk(path, '.html')

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
                        row[COLNAMES[k]]= util.strip_tag(arr[k].replace('<br>', ' '))
                        # print(">",arr[k])
                        # print("==>",row[COLNAMES[k]])
                    else:
                        row[COLNAMES[k]]= util.strip_tag(arr[k])
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

    def search_description(self, terms=[], logical_operator="or"):
        rst_blocklist = []

        patterns = util.get_patterns_from_terms(terms)
        
        for block in self.blocklist:
            flag_or = False
            flag_and = True
            for k in range(len(patterns)):
                fa = re.findall(patterns[k], block.description, flags=re.IGNORECASE)
                if len(fa) > 0:
                    flag_or = True
                elif len(fa) == 0:
                    flag_and = False 
            if  (logical_operator == "or" and flag_or) or (logical_operator == "and" and flag_and):
                rst_blocklist.append(block)

        return rst_blocklist


'''
        console = Console()
        table = Table(show_header=True)
        table.add_column("HTML", justify="left")
        for k in range(len(COLNAMES)):
            table.add_column(COLNAMES[k], justify=COL_JUSTIFY[k])
        table.add_column("FileID", justify="left")
        # table.add_column("Title")
        # table.add_column("Production Budget", justify="right")
        # table.add_column("Box Office", justify="right")
        pattern = r'\b'+term+r'\b|\bsmoking\b'
        # pattern = r'\bage\b'
        # pattern = r'age'
        print(term)
        for block in self.blocklist:
            fa = re.findall(pattern, block.description, flags=re.IGNORECASE)
            if len(fa) > 0:
            # if term in block.description:
                # print(pattern, re.findall(pattern, block.description, flags=re.IGNORECASE))

                # text = Text()
                # text.append("Hello", style="bold magenta")
                # text.append(" World!")

                for row in block.get_listrows():
                    if row[4] != "":
                        desc = Text()
                        arr_split = re.split(pattern, block.description, flags=re.IGNORECASE)
                        arr_findall = re.findall(pattern, block.description, flags=re.IGNORECASE)
                        for k in range(len(arr_split)):
                            desc.append(arr_split[k])
                            if k < len(arr_findall):
                                desc.append(arr_findall[k], style="bold magenta")
                    else:
                        desc = ""
                    table.add_row(block.fid, row[0], row[1], row[2], row[3], desc, block.htmlfile)
                        # table.add_row(block.fid, row[0], row[1], row[2], row[3], row[4], block.htmlfile)
        console.print(table)
'''