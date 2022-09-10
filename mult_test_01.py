import numpy as np
import pandas as pd
import plotly.express as px

vals = []
for i in np.array(range(2,19)):
  val = 0
  j = i
  while val < 100:
    val = i*j
    tmp = [i,j]
    tmp.sort()
    vals.append((j*i,*tmp))
    j+=1

# vals = set(vals)
df = pd.DataFrame(vals,columns=["Multiplied","i","j"])
df = df[df["Multiplied"]<=100]
df.sort_values(by=["Multiplied","i","j"],inplace=True)
df["Count"] = 1
df["i"] = df["i"].astype(str)
fig = px.bar(df,x="Multiplied",y="Count",color="i",text="i",
             hover_data={
               "i":True,
               "j":True,
               "Multiplied":True,
             "Count":False}
             )
fig.write_html("del.html",auto_open=True)

df["k"] = df["i"].astype(str) + 'x' + df["j"].astype(str)
df[["Multiplied","k"]]

df_group = df.groupby(by="Multiplied")["k"].apply(lambda x: ','.join(x))
df_group.to_clipboard(index=False)
