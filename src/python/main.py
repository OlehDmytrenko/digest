
import json
import io
import sys
import warnings
import traceback
import numpy
from sklearn.cluster import KMeans

warnings.filterwarnings("ignore", message=r"\[W033\]", category=UserWarning)

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')   

def accumulate_keywords(input_json, set_keywords):
    keywords = input_json["keywords"].split(" ")
    set_keywords = set_keywords+keywords
    return set_keywords, {}
        
def return_keywords(input_json, set_keywords):
    set_keywords_ = ""
    for keyword in set(set_keywords):
        set_keywords_ = set_keywords_ + keyword + " "
    return {
                "set_keywords": str(set_keywords_)[:-1]
            }
    
def vector(input_json, set_keywords):
        set_keywords = input_json["set_keywords"].split(" ")
        keywords = input_json["keywords"].split(" ")
        vector = ""
        for keyword in set_keywords:
            if keyword in keywords:
                vector += "1 "
            else:
                vector += "0 "
        return {
                    "vector": str(vector[:-1])
                }
    
def accumulate_vectors(input_json, vectors, docsID):
        ID = input_json["id"]
        docsID.append(ID)
        vector = (input_json["vector"].split(" "))
        vectors.append([int(v) for v in vector])
        return vectors, docsID, {}
        
def cluster(input_json, vectors, docsID):
        n_clusters = int(input_json["n_clusters"])
        M = numpy.array(vectors)
        clustersID = dict.fromkeys(docsID)
        kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(M)
        clusters = kmeans.predict(M)
        for index in range(len(docsID)):
            clustersID[docsID[index]] = clusters[index]
        return {
                    "clusters": str(clustersID)
                }

if __name__=='__main__':
    
    input_json = None
    
    docsID = []
    vectors = []
    set_keywords = []
    for line in input_stream:
        
        # read json from stdin
        input_json = json.loads(line)
        
        try:
            command = input_json["command"]
            
            if command == "accumulate_keywords":
                set_keywords, output = accumulate_keywords(input_json, set_keywords)
            elif command == "return_keywords":
                output = return_keywords(input_json, set_keywords)
            elif command == "vector":
                output = vector(input_json, set_keywords)
            elif command == "accumulate_vectors":
                vectors, docsID, output = accumulate_vectors(input_json, vectors, docsID)
            elif command == "cluster":
                output = cluster(input_json, vectors, docsID)
                
        except BaseException as ex:
            ex_type, ex_value, ex_traceback = sys.exc_info()            
            
            output = {"error": ''}           
            output['error'] += "Exception type : %s; \n" % ex_type.__name__
            output['error'] += "Exception message : %s\n" %ex_value
            output['error'] += "Exception traceback : %s\n" %"".join(traceback.TracebackException.from_exception(ex).format())
            
            
        
        output_json = json.dumps(output, ensure_ascii=False).encode('utf-8')
        sys.stdout.buffer.write(output_json)
        print()
