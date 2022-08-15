#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def accumulate(ID, vector, vectors, docsID):
        docsID.append(ID)
        vectors.append([int(v) for v in vector.split(" ")])
        return vectors, docsID
