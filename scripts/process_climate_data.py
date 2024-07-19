from pyspark.sql import SparkSession
import pandas as pd

# Initialize Spark session
spark = SparkSession.builder.appName('ClimateChangeAnalysis').getOrCreate()

def process_nasa_data(file_path):
    df = pd.read_csv(file_path)
    spark_df = spark.createDataFrame(df)
    return spark_df

def process_noaa_data(directory_path):
    # Process multiple NOAA data files
    # ...
    return combined_spark_df

# Process and store data
nasa_data = process_nasa_data('data/nasa_climate_data.csv')
noaa_data = process_noaa_data('data/noaa')
nasa_data.write.mode('overwrite').parquet('hdfs://namenode:8020/data/nasa')
noaa_data.write.mode('overwrite').parquet('hdfs://namenode:8020/data/noaa')
