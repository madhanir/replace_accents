Often, we encounter data that includes special characters with accents or diacritical marks collectively referred to as diacritics. When working with this data, there's often a need to substitute these accented characters with their equivalent non-accented ASCII counterparts.

The exciting news is that this Python package simplifies the process of replacing accented characters with their non-accented ASCII equivalents. 

This Python package is compatible with both standard Python and can seamlessly integrate with Pyspark and Spark SQL for your data processing needs.

The package can be installed from the PyPi repository using the below command
```
pip install replace_accents
```

Let's delve into detailed examples
**1. Python example**
```
# Import the replace accents function
from replace_accents import replace_accents_characters

# Use the function to replace accent characters
replace_accents_characters("crème de la crème")
```

**2. Pyspark example**
```
# Import the replace accents function
from replace_accents import replace_accents_characters

# Import Pyspark col function
from pyspark.sql.functions import col

# Register python function as Pyspark UDF and Spark SQL UDF
replace_accents_characters_pyspark_udf = spark.udf.register("replace_accents_characters_sparksql_udf", replace_accents_characters)

# Create Pyspark Dataframe
df = spark.table("table_name")

# Use Pyspark UDF on the Pyspark dataframe
display(df.select("col1", replace_accents_characters_pyspark_udf(col("col1")).alias("replaced_col1")))
```

**3. Spark SQL example**
```
# Import the replace accents function
from replace_accents import replace_accents_characters

# Register python function as Pyspark UDF and Spark SQL UDF
replace_accents_characters_pyspark_udf = spark.udf.register("replace_accents_characters_sparksql_udf", replace_accents_characters)

# Use Spark SQL UDF in the SQL query
spark.sql("select col1, replace_accents_characters_sparksql_udf(col1) as replaced_col1 from table")
```

You can get more information about this package [here](https://medium.com/@rahul.madhani/replace-accented-characters-in-python-pyspark-and-spark-sql-28844b6c783e)