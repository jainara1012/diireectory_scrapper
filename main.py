import pandas as pd
import argparse
import os
from datetime import datetime
from web_scraper import Extract_Data

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--searchspec", required=True, help="search parameter")
ap.add_argument(
    "-a", "--async", required=False, help="headless mode == True, else False"
)
ap.add_argument(
    "-startpage",
    required=False,
    help="give the starting page of the seach. If left blank, extraction will start from page 1",
)
args = vars(ap.parse_args())
batch_id = str(int(datetime.now().timestamp() * 1000))
# driver = login(batch_id=batch_id, headless=args["async"])
# df = pd.read_csv(args["filepath"], header=None)
# user_list = df.values.tolist()
# updated_list = []
# updated_list.append(["phone number", "url", "file_path", "comments"])
# for item in user_list:
#     print(f"{item[0]=}")
search_spec = args["searchspec"]
out_data = Extract_Data(
    search_param=search_spec,
    batch_id=batch_id,
    start_page=args["startpage"],
    headless=args["async"],
)
# updated_list.append([f"+{item[0]}", item[1], file_path, comments])
print(f"{out_data=}")
df = pd.DataFrame(
    out_data,
    columns=[
        "Name",
        "City",
        "State",
        "Contact Number Primary",
        "Contact Number Secondary",
        "Search parameter",
        "Page Number",
    ],
)
# print(f"{updated_df}")
df.to_csv(
    os.path.join("output", f"{search_spec}_{batch_id[-4:]}.csv"),
    index=False,
    header=True,
)
# driver.close()
