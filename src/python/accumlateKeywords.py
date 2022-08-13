#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def accumulate(newkeywords, set_keywords):
    set_keywords = set_keywords+newkeywords.split(" ")
    return set_keywords
