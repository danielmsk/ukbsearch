import os
import time
import re
from . import util
from .data import DATA
from .conf import COLNAMES, COL_JUSTIFY
from rich.console import Console
from rich.table import Table
from rich.text import Text

class UKBSearch():
    opt = None
    runtime = {}

    def __init__(self, opt):
        self.opt = opt
        self.has_opt_error = False

    def run(self):
        self.opt['log'].info('COMMAND: ' + self.opt['cmd'])
        t0 = time.time()
        self.dispatch()
        t2 = time.time()

        self.opt['log'].info('Total running time: ' + str(round(t2-t0, 1))+' sec')
        self.opt['log'].info('END')


    def search(self):
        data = DATA()
        data.load_html_list('./')
        blocklist = data.search_description(self.opt['searchterm'], self.opt['logic'])
        if self.opt['outtype'] == "console":
            self.print_blocklist(blocklist, self.opt['searchterm'])
        elif self.opt['outtype'] == "udi":
            self.print_udi(blocklist)

    def dispatch(self):
        if len(self.opt['searchterm']) > 0:
            self.search()
                
        # if self.opt['subcommand'] == "sim":
        #     sim = Simulation(self.opt['log'], self.dbman)
        #     sim.run(self.opt)
            # if self.opt['source'] == "bithumb":
            #     dc = Bithumb(self.opt['log'])
            #     dc.run(self.opt)

    def print_udi(self, blocklist):
        rst = []
        for block in blocklist:
            rst.append(block.fid)
            for row in block.get_listrows():
                rst.append(row[1])
        print()
        print (' '.join(rst))
        print()

    def print_blocklist(self, blocklist, terms=[]):
        console = Console()
        table = Table(show_header=True)
        table.add_column("HTML", justify="left")
        for k in range(len(COLNAMES)):
            table.add_column(COLNAMES[k], justify=COL_JUSTIFY[k])
        table.add_column("FileID", justify="left")

        patterns = util.get_patterns_from_terms(terms)
        pattern = r'|'.join(patterns)
        
        for block in blocklist:
            for row in block.get_listrows():
                if row[4] != "":
                    desc = Text()
                    arr_split = re.split(pattern, block.description, flags=re.IGNORECASE)
                    arr_findall = re.findall(pattern, block.description, flags=re.IGNORECASE)
                    for k in range(len(arr_split)):
                        desc.append(arr_split[k])
                        if k < len(arr_findall):
                            desc.append(arr_findall[k], style="bold magenta")
                    # desc.append(row[4])
                else:
                    desc = ""
                table.add_row(block.fid, row[0], row[1], row[2], row[3], desc, block.htmlfile)
        console.print(table)