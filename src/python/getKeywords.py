#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get(set_keywords):
    set_keywords_ = ""
    for keyword in set(set_keywords):
        set_keywords_ = set_keywords_ + keyword + " "
    return str(set_keywords_)[:-1]
