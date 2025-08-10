import json

def process_json(data: dict, filename: str):
        with open(filename, 'w')as json_file:
                json.dump(data, json_file, indent=4)

        # deserialize 
        with open(filename, 'r') as json_file:
                deserialized_data = json.load(json_file)

        return deserialized_data
                
            
if __name__ == "__main__":
        data = {
            'name': 'Alice',
            'age': 30,
            'skills': ['Python', 'JavaScript', 'C++']

        }
        result = process_json(data, 'data.json')
        print(result)