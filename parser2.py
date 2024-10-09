import pandas_gbq
from datetime import datetime
import pandas as pd
import numpy as np

dr = pd.date_range(start = "2017-01-01", end= "2017-01-31")
dr = dr.strftime("%Y%m%d").tolist()


# TODO: Set project_id to your Google Cloud Platform project ID.
project_id = "your-project-id"

df = pd.DataFrame()
for date in dr:
    print(f"Adding date {date}")
    sql = f"""
    SELECT visitorId, visitId, visitStartTime, date, totals, hits, fullVisitorId, userId
    FROM `bigquery-public-data.google_analytics_sample.ga_sessions_{date}`
    """
    df1 = pandas_gbq.read_gbq(sql, project_id=project_id)
    df = pd.concat([df, df1], ignore_index = True)

df.to_csv("customer_behaviour_jan17_totals.csv")