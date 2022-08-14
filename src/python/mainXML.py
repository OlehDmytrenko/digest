#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import io
import sys
import warnings
import traceback
import accumlateKeywords, buildVertor, accumulateVector, clustering
import re

#xmlFile = sys.argv[1]
#n_clusters = sys.argv[2]
xmlFile = "/Users/dmytrenko.o/Desktop/python/ex-xml-ok.xml"
n_clusters = 4

warnings.filterwarnings("ignore", message=r"\[W033\]", category=UserWarning)

if __name__=='__main__':
    
    f = open(xmlFile, encoding='utf-8')
    doc = ""
    set_keywords = []
    for line in f:
        try:
            doc = doc + line
            if line == "</sphinx:document>\n":
                set_keywords = accumlateKeywords.accumulate(re.findall("<keyword>(.+?)</keyword>+?", doc)[0], set_keywords)
                doc = "" 
        except BaseException as ex:
            ex_type, ex_value, ex_traceback = sys.exc_info()            
            
            output = {"error": ''}           
            output['error'] += "Exception type : %s; \n" % ex_type.__name__
            output['error'] += "Exception message : %s\n" %ex_value
            output['error'] += "Exception traceback : %s\n" %"".join(traceback.TracebackException.from_exception(ex).format())
    
    f = open(xmlFile, encoding='utf-8')
    doc = ""
    docsID = []
    vectors = []
    for line in f:
        try:
            doc = doc + line
            if line == "</sphinx:document>\n":
                vector = buildVertor.build(re.findall("<keyword>(.+?)</keyword>+?", doc)[0], set_keywords)
                vectors, docsID = accumulateVector.accumulate(re.findall("<sphinx:document id=(.+?)>+?", doc)[0][1:-1], vector, vectors, docsID)
                
                doc = "" 
                
        except BaseException as ex:
            ex_type, ex_value, ex_traceback = sys.exc_info()            
            
            output = {"error": ''}           
            output['error'] += "Exception type : %s; \n" % ex_type.__name__
            output['error'] += "Exception message : %s\n" %ex_value
            output['error'] += "Exception traceback : %s\n" %"".join(traceback.TracebackException.from_exception(ex).format())
    

    print (clustering.cluster(n_clusters, vectors, docsID))
        
    print()
