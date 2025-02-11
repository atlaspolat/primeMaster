import json
import os


class FileData(object):
    max_prime: int
    number_primes: int

    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__), "primes_data.json"), 'r') as f:
            data = f.read()
            data_object = json.loads(data)
            self.max_prime = data_object.get("max_prime")
            self.number_primes = data_object.get("number_primes")

    def update_file_data(self):
        with open(os.path.join(os.path.dirname(__file__), "primes_data.json"), 'w') as f:
            try:
                json_data = self.__dict__
                print(json_data)
                json_str = json.dumps(json_data)
            except Exception as e:
                print(str(e))
            else:
                f.write(json_str)


if __name__ == '__main__':
    obj = FileData()
    obj.max_prime = 83
    obj.number_primes = 23
    obj.update_file_data()
