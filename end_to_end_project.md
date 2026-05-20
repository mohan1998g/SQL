# End-to-End Data Engineering Project (BigQuery + Spark)

## Project: Real-Time E-commerce Analytics Pipeline

## Architecture

```
Data Sources (Web/App Events)
        |
        v
     Pub/Sub
        |
        v
   Dataflow / Spark
        |
        v
   Cloud Storage (GCS)
        |
        v
     BigQuery
        |
        v
   Visualization (Looker/Tableau)
```

## Step 1: Data Ingestion
- Use Pub/Sub to capture streaming events

## Step 2: Data Processing (Spark)
```python
from pyspark.sql.functions import col, to_date

df = spark.read.json("gs://bucket/raw_events")
clean_df = df.filter(col("user_id").isNotNull())              .withColumn("event_date", to_date(col("timestamp")))

clean_df.write.parquet("gs://bucket/processed/")
```

## Step 3: Load into BigQuery
```sql
CREATE OR REPLACE TABLE dataset.events AS
SELECT * FROM EXTERNAL_QUERY(...);
```

## Step 4: Analytics Queries
```sql
SELECT event_type, COUNT(*)
FROM dataset.events
GROUP BY event_type;
```

## Resume Points
- Built real-time data pipeline using Pub/Sub, Spark, and BigQuery
- Processed large-scale datasets with Spark transformations
- Designed analytical models in BigQuery
- Optimized queries using partitioning and clustering
