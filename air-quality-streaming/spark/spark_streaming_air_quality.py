from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window, count, current_timestamp
from pyspark.sql.types import StructType, StringType

# 1. Schema for your Kafka value
schema = StructType().add("location_name", StringType())

# 2. Create Spark session with MinIO S3 support
spark = SparkSession.builder \
    .appName("AirQualityBasic") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# 3. Read from Kafka
raw_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9093") \
    .option("subscribe", "air_quality") \
    .load()

# 4. Parse JSON and select location_name + fake timestamp
json_df = raw_df.selectExpr("CAST(value AS STRING) as json") \
    .select(from_json(col("json"), schema).alias("data")) \
    .select("data.location_name") \
    .withColumn("timestamp", current_timestamp())

# 5. Group by location and 10-minute window, count messages
agg_df = json_df \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        window(col("timestamp"), "10 minutes"),
        col("location_name")
    ).agg(count("*").alias("reading_count"))

# 6. Write to MinIO in Delta format
agg_df.writeStream \
    .format("parquet") \
    .outputMode("append") \
    .option("checkpointLocation", "s3a://delta-aq/checkpoints/") \
    .start("s3a://delta-aq/aggregated/") \
    .awaitTermination()