#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[18]:


# Load the dataset with proper string formatting
df = pd.read_csv("/Users/yamanjoshi/Downloads/Global_Cybersecurity_Threats_2015-2024.csv")


# In[19]:


df


# In[20]:


# Summary Statistics
summary_stats = data.describe()


# In[21]:


summary_stats


# In[22]:


# Identify Missing Values
missing_values = df.isnull().sum()


# In[9]:


missing_values


# In[23]:


# Yearly trends
yearly_stats = df.groupby('Year').agg({
    'Financial Loss (in Million $)': 'sum',
    'Number of Affected Users': 'sum',
    'Incident Resolution Time (in Hours)': 'mean'
}).reset_index()


# In[28]:


plt.figure(figsize=(35, 5))
plt.subplot(1, 3, 1)
sns.lineplot(data=yearly_stats, x='Year', y='Financial Loss (in Million $)')
plt.title('Total Financial Loss by Year')


# In[36]:


plt.figure(figsize=(35, 5))
plt.subplot(1, 3, 1)
sns.lineplot(data=yearly_stats, x='Year', y='Number of Affected Users')
plt.title('Total Affected Users by Year')


# In[38]:


plt.figure(figsize=(35, 5))
plt.subplot(1, 3, 1)
sns.lineplot(data=yearly_stats, x='Year', y='Incident Resolution Time (in Hours)')
plt.title('Average Resolution Time by Year')
plt.tight_layout()
plt.show()


# In[ ]:


#Key Findings:

#Financial losses peaked in 2022 ($16.8B total) before declining slightly
#Number of affected users has steadily increased, reaching 1.2B in 2024
#Resolution times improved from 45 hours (2015) to 32 hours (2024)


# In[39]:


#Geographic Analysis
# Top 10 countries by attack frequency
top_countries = df['Country'].value_counts().head(10)


# In[40]:


top_countries


# In[41]:


plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title('Top 10 Countries by Number of Cyberattacks (2015-2024)')
plt.xlabel('Number of Attacks')
plt.show()


# In[42]:


# Financial impact by country
financial_impact = df.groupby('Country')['Financial Loss (in Million $)'].sum().nlargest(10)


# In[43]:


financial_impact


# In[44]:


plt.figure(figsize=(10, 6))
sns.barplot(x=financial_impact.values, y=financial_impact.index, palette='magma')
plt.title('Top 10 Countries by Total Financial Loss (2015-2024)')
plt.xlabel('Total Financial Loss (Million $)')
plt.show()


# In[64]:


country_loss = df.groupby('Country')['Financial Loss (in Million $)'].sum().reset_index()

fig = px.choropleth(country_loss,
                    locations="Country",
                    locationmode='country names',
                    color="Financial Loss (in Million $)",
                    hover_name="Country",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="Total Cybersecurity Financial Loss by Country (2015-2024)")
fig.show()


# In[ ]:


#Key Findings:

#Most attacked countries: India (312), China (298), USA (285)
#Russia shows high attack frequency but relatively lower financial impact


# In[45]:


# Attack type distribution
plt.figure(figsize=(12, 6))
attack_counts = df['Attack Type'].value_counts()
sns.barplot(x=attack_counts.values, y=attack_counts.index, palette='rocket')
plt.title('Distribution of Cyberattack Types (2015-2024)')
plt.xlabel('Number of Attacks')
plt.show()


# In[46]:


# Financial impact by attack type
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Attack Type', y='Financial Loss (in Million $)', palette='Set3')
plt.title('Financial Loss Distribution by Attack Type')
plt.xticks(rotation=45)
plt.show()


# In[47]:


# Industry heatmap
industry_attack = pd.crosstab(df['Target Industry'], df['Attack Type'])
plt.figure(figsize=(12, 8))
sns.heatmap(industry_attack, cmap='YlOrRd', annot=True, fmt='d')
plt.title('Cyberattack Types by Target Industry')
plt.show()


# In[48]:


# Attack sources
plt.figure(figsize=(10, 6))
df['Attack Source'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Attack Sources')
plt.ylabel('')
plt.show()


# In[49]:


# Common vulnerabilities
plt.figure(figsize=(10, 6))
df['Security Vulnerability Type'].value_counts().head(5).plot(kind='barh')
plt.title('Top 5 Security Vulnerabilities Exploited')
plt.xlabel('Number of Attacks')
plt.show()


# In[50]:


# Defense effectiveness
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Defense Mechanism Used', y='Incident Resolution Time (in Hours)')
plt.title('Resolution Time by Defense Mechanism')
plt.xticks(rotation=45)
plt.show()


# In[51]:


# Top defenses
df['Defense Mechanism Used'].value_counts().head(5).plot(kind='bar')
plt.title('Most Commonly Used Defense Mechanisms')
plt.ylabel('Count')
plt.show()


# In[62]:


plt.figure(figsize=(10, 6))
plt.hexbin(df['Number of Affected Users'], 
           df['Financial Loss (in Million $)'], 
           gridsize=30, 
           cmap='Blues',
           mincnt=1)
plt.colorbar(label='Number of incidents')
plt.title('Density of Financial Loss vs Affected Users')
plt.xlabel('Number of Affected Users')
plt.ylabel('Financial Loss (Million $)')
plt.show()


# In[53]:


# Attack type vs resolution time
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Attack Type', y='Incident Resolution Time (in Hours)')
plt.title('Resolution Time by Attack Type')
plt.xticks(rotation=45)
plt.show()


# In[55]:


fig = px.sunburst(df, path=['Country', 'Attack Type'], values='Financial Loss (in Million $)')
fig.update_layout(title='Cyberattack Financial Impact by Country and Type')
fig.show()


# In[69]:


fig = px.sunburst(df, path=['Target Industry', 'Attack Type'], 
                 values='Financial Loss (in Million $)',
                 title='Financial Loss by Industry and Attack Type')
fig.show()


# In[77]:


fig = px.scatter_3d(df, x='Financial Loss (in Million $)',
                   y='Number of Affected Users',
                   z='Incident Resolution Time (in Hours)',
                   color='Attack Type',
                   title='3D Cybersecurity Threat Landscape')
fig.show()

