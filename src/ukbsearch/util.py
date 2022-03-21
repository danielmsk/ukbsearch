import os
import re


def walk(dirPath, ext=""):
    flist = []
    for root, dirs, files in os.walk(dirPath):
        for fname in files:
            if (len(ext) > 0 and fname.endswith(ext)) or len(ext) == 0:
                fullpath = os.path.join(root, fname)
                flist.append(fullpath)
    flist.sort()
    return flist

def strip_tag(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)

def get_patterns_from_terms(terms):
    patterns = []
    for term in terms:
        patterns.append(convert_term2pattern(term))
    return patterns

def convert_term2pattern(term):
    aterm = ""
    if term[0] == "*":
        if term[-1] == "*":
            aterm += term[1:-1]
        else:
            aterm += term[1:] + r'\b'
    else:
        if term[-1] == "*":
            aterm += r'\b' + term[:-1]
        else:
            aterm += r'\b' + term + r'\b'
    return aterm