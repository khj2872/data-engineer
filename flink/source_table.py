from pyflink.table import EnvironmentSettings, TableEnvironment, DataTypes

settings = EnvironmentSettings.new_instance()\
    .in_batch_mode().build()
table_env = TableEnvironment.create(settings)

sample_data = [
    ("Spark", 1),
    ("Airflow", 2),
    ("Kafka", 3),
    ("Flink", 4),
]

# schema infer
src1 = table_env.from_elements(sample_data)
print(src1)
src1.print_schema()

df = src1.to_pandas()
print(df)

# set column name
col_names = ["framework", "chapter"]
src2 = table_env.from_elements(sample_data, col_names)
print(src2.to_pandas())

# set schema
schema = DataTypes.ROW([
    DataTypes.FIELD("framework", DataTypes.STRING()),
    DataTypes.FIELD("chapter", DataTypes.BIGINT())
])
src3 = table_env.from_elements(sample_data, schema)
print(src3.to_pandas())