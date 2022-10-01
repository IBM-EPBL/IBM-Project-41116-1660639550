import datetime
import pandas as pd
test_date = datetime.datetime.strptime("01-01-2023","%d-%m-%y")
k=40
date_generated = pd.date_range(test_date, periods=k)
print(date_generated.strftime("%d-%m-%y"))
