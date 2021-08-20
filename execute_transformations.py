import pandas as pd
import tecton

workspace = tecton.get_workspace("bruce_test")
print(workspace)

print(workspace.list_feature_services())

# feature_service = workspace.get_feature_service("bruce_sample_feature_service")

# df = pd.DataFrame({
    # "cred_tier": ["B1", "B1"],
    # "veh_model": ["FORD", "FORD"]
# })

# print(feature_service.get_feature_dataframe(df).to_pandas())

