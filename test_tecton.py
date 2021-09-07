import datetime
import pandas as pd
import tecton

ws = tecton.get_workspace('prod')

request_data = {
    "cred_tier": "A1",
    "veh_make": "FORD"
}

fs = tecton.get_feature_service('test_fs')
results = fs.get_feature_vector(request_context_map=request_data)
print(results.to_dict())