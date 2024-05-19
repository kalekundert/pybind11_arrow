import pyarrow as pa
import demo
import polars as pl

df = pl.DataFrame({'a': [1,2,3], 'b': [4,5,6]})
print(demo.num_rows(df.to_arrow()))

