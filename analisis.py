import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, col, expr, concat, lit

spark = SparkSession.builder.appName("Amazon Book Reviews Analysis").getOrCreate()

archivo_csv = sys.argv[1]
data = spark.read.option("header", "true").csv(archivo_csv, inferSchema=True)

data = data.withColumn("helpful_votes", expr("split(`review/helpfulness`, '/')[0]").cast("int")) \
           .withColumn("total_votes", expr("split(`review/helpfulness`, '/')[1]").cast("int"))

data = data.withColumn("helpfulness_ratio", 
                       expr("CASE WHEN total_votes > 0 THEN helpful_votes / total_votes ELSE 0 END"))

result = data.groupBy("Id", "Title").agg(
    avg("review/score").alias("average_score"),
    count("Id").alias("total_reviews"),
    (avg("helpfulness_ratio") * 100).alias("average_helpfulness_ratio_percentage")
)

result = result.withColumn("average_helpfulness_ratio_percentage", 
                           concat(col("average_helpfulness_ratio_percentage"), lit("%")))

result = result.select("Id", "Title", "average_score", "total_reviews", "average_helpfulness_ratio_percentage")

result.write.csv(sys.argv[2], header=True)

spark.stop()