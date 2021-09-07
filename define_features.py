import pandas
from pyspark.sql.types import *
import tecton

workspace = tecton.get_workspace("bruce_test")

request_schema = StructType([
    StructField("cred_tier", StringType()),
    StructField("veh_make", StringType()),
])
req_schema = tecton.RequestDataSource(request_schema=request_schema)


@tecton.on_demand_feature_view(
    inputs={"req": tecton.Input(req_schema)},
    mode="pandas",
    output_schema=StructType([
        StructField("ranked_credit", LongType())
    ]),
)
def rank_credit(req: pandas.DataFrame):
    import pandas as pd
    df = pd.DataFrame()
    df["ranked_credit"] = req.cred_tier.str.slice(0, 1).apply(ord) - ord("A")
    return df


@tecton.on_demand_feature_view(
    inputs={"req": tecton.Input(req_schema)},
    mode="pandas",
    output_schema=StructType([
        StructField("encode_veh_make", LongType())
    ]),
)
def encode_veh_make(req: pandas.DataFrame):
    lookups = {
        "FORD": 1,
        "CHEVY": 2,
        "TOYOTA": 300
    }
    import pandas as pd
    df = pd.DataFrame()
    df["veh_make"] = req.veh_make.map(lookups)
    return df

fs = tecton.FeatureService(
    name = 'bruce_sample_feature_service',
    features=[
        rank_credit,
    ]
)
