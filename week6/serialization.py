import pickle

data = {
    'name': 'Alice',
    'age': 30,
    'city': 'Kimpala'
}

#serialize the data to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)


# Deserialize the data from the file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)