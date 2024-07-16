import joblib
import pickle

# Load the pickle file using Python 2
with open('test_data/SMPLX_MALE.pkl', 'rb') as f:
    data = pickle.load(f, encoding='latin1')

    # Now you can use the data as needed
print(data)

# Save the data in a new pickle file using Python 2
with open('test_data/SMPLX_MALE_2.pkl', 'wb') as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
