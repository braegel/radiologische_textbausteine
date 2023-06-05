import yaml

def read_yaml(file_path):
    with open(file_path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            data = None
    return data

def write_txt(file_path, data):
    with open(file_path, 'w') as f:
        f.write(str(data))

def main():
    yaml_file = 'textbausteine.yaml'  # your yaml file path
    txt_file = 'textbausteine.txt'  # your txt file path
    data = read_yaml(yaml_file)
    write_txt(txt_file, data)

if __name__ == "__main__":
    main()
