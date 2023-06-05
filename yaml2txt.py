import yaml

def read_yaml(file_path):
    with open(file_path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            data = None
    return data

def data_txt(data):
    for modality in data['modality']:
        if isinstance(modality, dict):
            for regions in modality.values():
                for region in regions:
#                    print(modality.keys())
#                    print('cr' in modality.keys())
                    if('cr' in modality.keys()):
                        print("* " + "Röntgen "+region['region']+": "+region['shortcut'])
                    print("Rechtfertigende Indikation: " + region['history']) # TODO for MRI
def main():
    yaml_file = 'textbausteine.yaml'  # your yaml file path
    txt_file = 'textbausteine.txt'  # your txt file path
    data = read_yaml(yaml_file)
    data_txt(data)

if __name__ == "__main__":
    main()
