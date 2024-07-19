from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

# Initialize Spark session
spark = SparkSession.builder.appName('ClimateChangePrediction').getOrCreate()

# Load data from HDFS
nasa_data = spark.read.parquet('hdfs://namenode:8020/data/nasa')
noaa_data = spark.read.parquet('hdfs://namenode:8020/data/noaa')

# Feature extraction
assembler = VectorAssembler(inputCols=['temp_anomaly', 'precipitation', 'sea_level'], outputCol='features')
nasa_data = assembler.transform(nasa_data)
noaa_data = assembler.transform(noaa_data)

# Combine datasets if necessary
# combined_data = nasa_data.union(noaa_data)

# Train-test split
train_data, test_data = nasa_data.randomSplit([0.8, 0.2], seed=1234)

# Train a Random Forest model
rf = RandomForestRegressor(featuresCol='features', labelCol='temperature')
rf_model = rf.fit(train_data)

# Evaluate the model
predictions = rf_model.transform(test_data)
evaluator = RegressionEvaluator(labelCol='temperature', predictionCol='prediction', metricName='rmse')
rmse = evaluator.evaluate(predictions)
print(f'Root Mean Squared Error (RMSE): {rmse}')

# Save the model
rf_model.save('models/climate_change_prediction_model')
