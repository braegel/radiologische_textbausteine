import yaml

class Report:
    def __init__(self, modality,region,shortcut,history,technique,findings): #,region,shortcut,history,technique,findings):
        self.modality=modality
        self.region=region
        self.shortcut=shortcut
        self.history=history
        self.technique=technique
        self.findings=findings

    def de_md(self):
        if self.modality == 'cr':
            md = "# Röntgen "
        md = md + self.region+": "+self.shortcut+"\n"
        md = md + "## Klinische Informationen\n"+self.history+"\n"
        md = md + "\n## Technik\n"+self.technique+"\n"
        if self.modality=='cr':
            md= md + "Die rechtfertigende Indikation gemäß StrSchV §119 wurde durch die im Strahlenschutz fachkundige unterzeichende Person gestellt.\n"
        md = md + "\n## Befund\n"
        
        for finding_category in self.findings:
            for finding_category_name,findings in finding_category.items():
                md=md + "\n### "+finding_category_name+"\n"
                for finding in findings:
                    if isinstance(finding,str):
                        md=md + str(finding) +": Unauffällig\n"
                    else:
                        for finding,answers in finding.items():
                            md=md + finding + ":\n"
                            for answer in answers['answers']:
                                md = md + "- [ ] "+answer + "\n"
        md=md+"\n## Beurteilung\n"
        return(md)

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
                    print(report.de_md())

def main():
    yaml_file = 'textbausteine.yaml'  # your yaml file path 
    txt_file = 'textbausteine.txt'  # your txt file path
    data = read_yaml(yaml_file)
    list_of_reports=parse_yaml(data)

if __name__ == "__main__":
    main()
