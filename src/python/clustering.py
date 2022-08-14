#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import numpy
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

def distortion(M, n_clusters):
    distortions = []
    inertias = []
    K = range(1, 10)
    for k in K:
        kmeanModel = KMeans(n_clusters=k, random_state=0).fit(M)
      
        distortions.append(sum(numpy.min(cdist(M, kmeanModel.cluster_centers_,
                                            'euclidean'), axis=1)) / M.shape[0])
        inertias.append(kmeanModel.inertia_)
    print (distortions)
    plt.plot(K, distortions, 'bx-')
    plt.xlabel('Values of K')
    plt.ylabel('Distortion')
    plt.title('The Elbow Method using Distortion')
    plt.show()
    return 

def cluster(n_clusters, vectors, docsID):
    n_clusters = int(n_clusters)
    digest = []
    for i in range(n_clusters):
        digest.append({})
        
    M = numpy.array(vectors)
    
    #distortion(M, n_clusters)
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(M)
    clusters = kmeans.predict(M)
    centers = kmeans.cluster_centers_
    for index in range(len(docsID)):
        digest[clusters[index]][docsID[index]] = cdist([M[index]], [centers[clusters[index]]])[0][0]
    sortdigest = {}
    for index in range(n_clusters):
        sortdigest[index] = {k: v for k, v in sorted(digest[index].items(), key=lambda item: item[1], reverse=True)}
    return str(sortdigest)
    