# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_app.py'.

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame using the list given above. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

# Write your code to filter streamlit warnings 
st.set_option('deprecation.showPyplotGlabalUse', False)

# Write the code to design the web app

# Add title on the main page and in the sidebar.
st.title('Census Data Visualization Web App')
st.sidebar.title('Census Data Visualization')

# Using the 'if' statement, display raw data on the click of the checkbox.
if st.sidebar.checkbox('Show raw data') :
  st.subheader('Census Data set')
  st.dataframe(census_df)
  st.write('Number of rows', census_df.shape[0])
  st.write('Number of columns', census_df.shape[1])

# Add a multiselect widget to allow the user to select multiple visualisations.
# Add a subheader in the sidebar with the label "Visualisation Selector"

# Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
# Store the current value of this widget in a variable 'plot_list'.
st.sidebar.subheader('Visualisation selector')
plot_list = st.sidebar.multiselect('Select the plots/charts', ('Pie Chart', 'Box Plot', 'Count Plot'))


# Display pie plot using matplotlib module and 'st.pyplot()'
if 'Pie Chart' in plot_list :
  st.subheader('Pie Chart')
  pie_data = census_df['income-group'].value_counts()
  plt.figure(figsize=(5,5))
  plt.pie(pie_data, labels=pie_data.index, autopct='%1.2f%%', startangle=30)
  plt.title('Distribution of records for the income-group feature.')
  st.pyplot()

  pie_data = census_df['gender'].value_counts()
  plt.figure(figsize=(5,5))
  plt.pie(pie_data, labels=pie_data.index, autopct='%1.2f%%', startangle=30)
  plt.title('Distribution of records for the gender feature.')
  st.pyplot()

# Display box plot using matplotlib module and 'st.pyplot()'
if 'Box Plot' in plot_list :
  st.subheader('Box Plot')
  plt.figure(figsize=(12,2))
  plt.title('Box plot for difference in the range of values for the hours-per-week feature for different income groups.')
  sns.boxplot('hours-per-week', 'income', data=census_df)
  st.pyplot()
  
  plt.figure(figsize=(12,2))
  plt.title('Box plot for difference in the range of values for the hours-per-week feature for different gender groups.')
  sns.boxplot('hours-per-week', 'gender', data=census_df)
  st.pyplot() 

# Display count plot using seaborn module and 'st.pyplot()' 
if 'Count Plot' in plot_list :
  st.subheader('Count Plot')
  plt.figure(figsize=(9,5))
  plt.title('Count plot for distribution of records for unique workclass groups')
  sns.countplot('workclass', data=census_df)
  st.pyplot()
