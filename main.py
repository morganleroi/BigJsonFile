import json
import random
import string
import uuid


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def generate_json2():
    data = []
    for i in range(150000):
        data.append({
            'name': randomString(),
            'website': randomString(),
            'from': randomString(),
            'objectID': str(uuid.uuid4())
        })

    with open('data/150k.json', 'w') as outfile:
        json.dump(data, outfile)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_json2()
