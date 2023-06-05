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
        
        for finding_category in self.findings:
            if list(finding_category)[0] != 'general':
                print()
                print("  "+list(finding_category)[0]+":")
                for findings in finding_category.values():
                    for finding in findings:
                        if isinstance(finding,str):
                            print(finding+": Unauffällig")
                        else:
                            for finding, answer in finding.items():
                                print(finding+": "+str(answer))
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

if __name__ == "__main__":
    main()
