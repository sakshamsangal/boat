import glob
import json
import uuid

import pandas as pd
from sqlalchemy import create_engine, types

engine = create_engine('mysql://root:root@localhost/stud')  # enter your password and database names here

# myQuery = "SELECT * FROM tb_student"
# df = pd.read_sql_query(myQuery, engine)

# from datetime import datetime, timezone

# utc_dt = datetime.now(timezone.utc)
# s1 = utc_dt.strftime("%m/%d/%Y, %H:%M:%SZ")
# mm/dd/YY H:M:S format
# print("s1:", s1)

# print(x)
# for index, row in df.iterrows():
#     print(row['roll_num'])
#
# df = pd.read_csv("temp.csv", sep=',', quotechar='\'', encoding='utf8')
#
#
# for i in range(50000):
#     df['roll_num'] = x
#     df.to_sql('tb_student', con=engine, index=False, if_exists='append')
#     if i % 1000 == 0:
#         print(i, "records inserted")

def add_record(rec_count, tb_name, cols):
    rows_list = []
    log_count = rec_count / 20
    for i in range(rec_count):
        x = uuid.uuid4()
        rows_list.append(cols)
        if i % log_count == 0:
            print(i, "dict inserted")

    df = pd.DataFrame(rows_list)
    df.to_sql(tb_name, con=engine, index=False, if_exists='append')
    print("records inserted successfully")

for json_file in glob.glob("../static/tb/*.json"):
    with open(json_file) as f:
        x = json.load(f)
        add_record(10, x['tb_name'], x['tb_cols'])
