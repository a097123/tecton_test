import tecton

workspace = tecton.get_workspace("bruce_test")

print(tecton.list_data_sources())

data = workspace.get_virtual_data_source('bruce_sample')

print(data.dataframe())
