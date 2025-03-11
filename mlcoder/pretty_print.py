import json

def pretty_print(content):
    print(json.dumps(content, indent=4, sort_keys=True))

if __name__ == "__main__":
    sample_content = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    pretty_print(sample_content)