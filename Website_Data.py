import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("website.csv")
df.head()
df.info()

#Data Cleaning
df.columns = df.iloc[0]
df = df.drop(index=0).reset_index(drop=True)
df.columns = [ "channel group", "DateHour", "Users", "Sessions", "Engaged Sessions", "Average engagement time per session", "Engaged sessions per user", "Events per session", "Engagement rate", " Event count"]
df["DateHour"] = pd.to_datetime(df["DateHour"], format="%Y%m%d%H", errors="coerce")
numeric_cols = df.columns.drop(["channel group", "DateHour"])
df[numeric_cols]= df[numeric_cols].apply(pd.to_numeric, errors= 'coerce')
df["Hour"]= df["DateHour"].dt.hour
df.info()

# Sessions and Users over time
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10,5))
df.groupby("DateHour")[["Sessions", "Users"]].sum().plot(ax=plt.gca())
plt.title(" Sessions And Users OverTime")
plt.xlabel("DateHour")
plt.ylabel("count")
plt.show()

#Total Users by Channel 
plt.figure(figsize=(8,5))
sns.barplot(data=df, x="channel group", y="Users", estimator=np.sum, palette="viridis")
plt.title("Total Users By Channel")
plt.xticks(rotation=45)
plt.show()

# Average Engagement Time by Channel 
plt.figure(figsize=(8,5))
sns.barplot(data=df, x="channel group",y="Average engagement time per session", estimator=np.mean, palette="magma")
plt.title("Avg Engagement Time By Channel")
plt.xticks(rotation=45)
plt.show

# Engagement Rate Distribution By Channel

plt.figure(figsize=(8,5))
sns.boxplot( data= df, x="channel group", y="Engagement rate", palette="coolwarm")
plt.title("Engagement Rate Distribution By Chanel")
plt.xticks(rotation=45)
plt.show()

#Engaged VS Non-Engaged Sessions

session_df = df.groupby("channel group")[["Sessions", "Engaged Sessions"]].sum().reset_index()
session_df["Non-Engaged"]= session_df["Sessions"] - session_df["Engaged Sessions"]
session_df_melted= session_df.melt(id_vars="channel group", value_vars=["Engaged Sessions", "Non-Engaged"])

plt.figure(figsize=(8,5))
sns.barplot(data = session_df_melted, x="channel group", y="value", hue="variable")
plt.title("Engaged vs Non-Engaged Sessions")
plt.xticks(rotation=45)
plt.show()

#Traffic by hour and channel
heatmap_data = df.groupby(["Hour","channel group"]) ["Sessions"].sum().unstack().fillna(0)

plt.figure(figsize=(12,6))
sns.heatmap(heatmap_data, cmap="YlGnBu", linewidths=.5, annot=True, fmt='.0f')
plt.title("Traffic by Hour and Channel")
plt.xlabel("channel group")
plt.ylabel("Hour of Day")
plt.show()

# Engagement Rate vs Session OverTime

df_plot= df.groupby("DateHour")[["Engagement rate", "Sessions"]].mean().reset_index()

plt.figure(figsize=(10,5))
plt.plot(df_plot["DateHour"], df_plot["Engagement rate"], label="Engagement rate", color="red")
plt.plot(df_plot["DateHour"],df_plot["Sessions"], label="Sessions", color="blue")
plt.title("Engagement Rate vs Session Over Time")
plt.xlabel("DateHour")
plt.legend()
plt.grid(True)
plt.show()
print(session_df_melted.columns)

print(df.columns.to_list())
















