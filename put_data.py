import tecton

workspace = tecton.get_workspace("bruce_test")

bucket = "pgr-quoting-quotingresearch-dev-aws35d-nonversioned"
filename = "bruce_sample.parquet"
table_name = "bruce_sample"

data = tecton.FileDSConfig(
    uri=f"s3://{bucket}/{filename}",
    file_format='parquet'
)

data_vds = tecton.VirtualDataSource(
    name=table_name,
    batch_ds_config=data
)

