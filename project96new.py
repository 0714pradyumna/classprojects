# Configure the main page by setting its title and icon that will be displayed in a browser tab.
# Import the streamlit Python module.
import streamlit as st
census_df = load_data()
# Configure your home page.
st.set_page_config(page_title = 'Census Visualisation Web App',
                   page_icon = '*',
                   layout = 'centered',
                   initial_sidebar_state = 'auto')
# Set the title to the home page contents.
st.subheader('Census Visualisation Web App')
# Provide a brief description for the web app.
st.title('This web app allows a user to explore ans visualise the census data')

# View Dataset Configuration
st.header('View Data')
# Add an expander and display the dataset as a static table within the expander.
with st.beta_expander('View Dataset'):
  st.table(census_df)

# Create three beta_columns.
beta_col1, beta_col2, beta_col3 = st.beta_columns(3)

# Add a checkbox in the first column. Display the column names of 'census_df' on the click of checkbox.
with beta_col1:
  if st.checkbox('Show all column names'):
    st.table(list(census_df.columns))

# Add a checkbox in the second column. Display the column data-types of 'census_df' on the click of checkbox.
with beta_col2:
  if st.checkbox('View column data type'):
    st.table(census_df.dtypes)

# Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
with beta_col3:
  if st.checkbox('View column data'):
    column_data = st.selectbox('Select column', tuple(census_df.columns))
    st.table(census_df[column_data])

# Display summary of the dataset on the click of checkbox.
if st.checkbox('Show summary') :
  st.table(census_df.describe())
