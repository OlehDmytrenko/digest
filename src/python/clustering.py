#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import numpy

def cluster(n_clusters, vectors, docsID):
        M = numpy.array(vectors)
        clustersID = dict.fromkeys(docsID)
        kmeans = KMeans(n_clusters=int(n_clusters), random_state=0).fit(M)
        clusters = kmeans.predict(M)
        for index in range(len(docsID)):
            clustersID[docsID[index]] = clusters[index]
        return str(clustersID)
    