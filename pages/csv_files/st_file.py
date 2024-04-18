import pandas as pd

df = pd.read_csv("clean_data.csv")
df["artist_track"] = df["first_artist"] + " - " + df["name"]

df_1950s = df.query('decade == "1950s"')
df_1950s.to_csv("data_1950s.csv", index=False)

df_1960s = df.query('decade == "1960s"')
df_1960s.to_csv("data_1960s.csv", index=False)

df_1970s = df.query('decade == "1970s"')
df_1970s.to_csv("data_1970s.csv", index=False)

df_1980s = df.query('decade == "1980s"')
df_1980s.to_csv("data_1980s.csv", index=False)

df_1990s = df.query('decade == "1990s"')
df_1990s.to_csv("data_1990s.csv", index=False)

df_2000s = df.query('decade == "2000s"')
df_2000s.to_csv("data_2000s.csv", index=False)

df_2010s = df.query('decade == "2010s"')
df_2010s.to_csv("data_2010s.csv", index=False)
