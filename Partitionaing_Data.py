### partitioning data
# training 60%, validation 40%
trainData, validData = train_test_split(housing_df, test_size = 0.40, random_state = 1)
# produces 
# training: 3481, validation: 2321

# training 50%, validation 30%, test 20%
trainData, temp = train_test_split(housing_df, test_size = 0.5, random_state =1)
# now split temp into validation and test (temp -> validation / test)
validData, testData = train_test_split(temp, test_size = 0.4, random_state = 1)

# produces
# training: 2901, validation: 1741, test: 1160

### Fit model and make predictions (training data)
mode = LinearRegression()
model.fit(train_X, train_y)

train_pred = model.predict(train_X)
train_results = pd.DataFrame({
  'TOTAL_VALUE': train_y,
  'predicted': train_pred,
  'residual': train_y - train_pred
})

### show sample of predictions
train_results.head()


### scoring the validation data
valid_pred = model.predict(valid_X)
valid_results = pd.DataFrame({
  'TOTAL_VALUE': valid_y,
  'predicted': valid_pred,
  'residual': valid_y - valid_pred
})

valid_results.head()

'''   TOTAL_VALUE  Predicted  residual
1822  462.0        406.946377 55.053623 
1998  370.3        362.888928 7.511072
...'''

### reviewing variables
housing_df.columns # pritn a list of varaibles
# REMODEL needs to be converted to a categorical variable
housing_df.REMODEL = housing_df.REMODEL.astype('category')
housing_df.REMODEL.cat.categories # show number of categories
hosuing_df.REMODEL.dtype # check type of converted variable

### creating binary dummies
# use drop_first = True to drop the first dummy variable (binary variable)
housing_df = pd.get_dummies(hosuing_df, prefix_sep = '_', drop_first = True)
housing_df.columns
housing_df.loc[:,'REMODEL_Old': 'REMODEL_Recent'].head()
