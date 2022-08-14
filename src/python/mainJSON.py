
import json
import io
import sys
import warnings
import traceback
import accumlateKeywords, getKeywords, buildVertor, accumulateVector, clustering

warnings.filterwarnings("ignore", message=r"\[W033\]", category=UserWarning)

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

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
                set_keywords = accumlateKeywords.accumulate(input_json["keywords"], set_keywords)
                output = {}
            elif command == "get_keywords":
                output = {
                            "set_keywords": getKeywords.get(set_keywords)
                        }
            elif command == "vector":
                output = {
                            "vector": buildVertor.build(input_json["keywords"], set_keywords)
                        }
            elif command == "accumulate_vectors":
                vectors, docsID = accumulateVector.accumulate(input_json["id"], input_json["vector"], vectors, docsID)
                output = {}
            elif command == "cluster":
                output = {
                            "clusters": clustering.cluster(input_json["n_clusters"], vectors, docsID)
                        }
                
        except BaseException as ex:
            ex_type, ex_value, ex_traceback = sys.exc_info()            
            
            output = {"error": ''}           
            output['error'] += "Exception type : %s; \n" % ex_type.__name__
            output['error'] += "Exception message : %s\n" %ex_value
            output['error'] += "Exception traceback : %s\n" %"".join(traceback.TracebackException.from_exception(ex).format())
            
            
        
        output_json = json.dumps(output, ensure_ascii=False).encode('utf-8')
        sys.stdout.buffer.write(output_json)
        print()
