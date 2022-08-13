#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def build(keywords, set_keywords):
        vector = ""
        for keyword in set_keywords:
            if keyword in keywords.split(" "):
                vector += "1 "
            else:
                vector += "0 "
        return str(vector[:-1])
