from pyflink.table import EnvironmentSettings, TableEnvironment, CsvTableSource, DataTypes

settings = EnvironmentSettings.new_instance()\
    .in_batch_mode().build()
table_env = TableEnvironment.create(settings)

field_name = ["framework", "chapter"]
field_types = [DataTypes.STRING(), DataTypes.BIGINT()]

source = CsvTableSource(
    "./sample.csv",
    field_name,
    field_types,
    ignore_first_line=False
)

table_env.register_table_source("chapters", source)
table = table_env.from_path("chapters")

print(table.to_pandas())