
# Create a function that accepts 'model', island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g' and 'sex' as inputs and returns the species name.
def prediction(model, island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex) :
  species_type = model.predict([[island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex]])
  species_type = species_type[0]
  if species_type == 0 :
    return 'Adelie'
  elif species_type == 1 :
    return 'Chinstrap'  
  else :
    return 'Gentoo'
  
  # Design the App
st.title('Penguin species prediction app')


bill_length_input = st.sidebar.slider('bill length(in mm)', float(df['bill_length_mm'].min()), float(df['bill_length_mm'].max()))
bill_depth_input = st.sidebar.slider('bill depth(in mm)', float(df['bill_depth_mm'].min()), float(df['bill_depth_mm'].max()))
flipper_length_input = st.sidebar.slider('flipper length(in mm)', float(df['flipper_length_mm'].min()), float(df['flipper_length_mm'].max()))
body_mass_input = st.sidebar.slider('body mass(in g)', float(df['body_mass_g'].min()), float(df['body_mass_g'].max()))


sex = st.sidebar.selectbox('Gender', ('Male', 'Female'))
if 'sex' == 'Male' :
	sex = 0
else :
	sex = 1	

island = st.sidebar.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))  
if 'island' == 'Biscoe' :
	island = 0
elif 'island' == 'Dream' :
    island = 1
else :
    island = 2  

classifier = st.sidebar.selectbox('Classifier', ('Support Vector Classification', 'Random Forest Classifier', 'Logistic Regression'))


if st.sidebar.button('Predict') :
  if classifier == 'Support Vector Classification' :
    species_type= prediction(svc_model, isl, bill_length_input , bill_depth_input, flipper_length_input, body_mass_input, sex)
    accuracy = svc_model.score(X_train, y_train)

  elif classifier == 'Random Forest Classifier' :
    species_type=prediction(rf_clf, isl, bill_length_input, bill_depth_input, flipper_length_input, body_mass_input, sex)
    accuracy = rf_clf.score(X_train, y_train) 

  else :
    species_type=prediction(log_reg, isl, bill_length_input, bill_depth_input, flipper_length_input, body_mass_input, sex)
    accuracy = log_reg.score(X_train, y_train)



  st.write('The type of the species is ', species_type)
  st.write('Acurracy', accuracy)
