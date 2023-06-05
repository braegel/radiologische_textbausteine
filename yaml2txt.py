import yaml

class Report:
    def __init__(self, modality,region,shortcut,history,technique,findings): #,region,shortcut,history,technique,findings):
        self.modality=modality
        self.region=region
        self.shortcut=shortcut
        self.history=history
        self.technique=technique
        self.findings=findings

    def de_txt(self):
        print ("* ", end ='')
        if self.modality == 'cr':
            print("Röntgen ", end = '')
        print(self.region+": "+self.shortcut)
        print("Klinische Informationen: "+self.history)
        print();
        print("Technik: "+self.technique)
        if self.modality=='cr':
            print("Die rechtfertigende Indikation gemäß StrSchV §119 wurde durch die im Strahlenschutz fachkundige unterzeichende Person gestellt.")
        print()
        print("Befund")
        print()
        print("Beurteilung")
        print()

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
                    if('cr' in modality.keys()): #TODO MRI CT
                        print("* " + "Röntgen "+region['region']+": "+region['shortcut'])
                    print("Rechtfertigende Indikation: " + region['history']) # TODO for MRI
                    print()
                    print("Technik: " + region['technique'])
                    print()
                    print("Befund:")
                    for finding_cat in region['findings']:
                        print (f"{finding_cat}")
                    print();
                    print("Beurteilung: \n")

def parse_yaml(data):
    for modality in data['modality']:
        if isinstance(modality, dict):
            for regions in modality.values():
                for region in regions:
                    report=Report(list(modality)[0], region['region'], region['shortcut'], region['history'], region['technique'],region['findings'])
                    report.de_txt()

def main():
    yaml_file = 'textbausteine.yaml'  # your yaml file path 
    txt_file = 'textbausteine.txt'  # your txt file path
    data = read_yaml(yaml_file)
    list_of_reports=parse_yaml(data)
#    data_txt(data)

if __name__ == "__main__":
    main()
