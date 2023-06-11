import yaml

class Report:
    def __init__(self, modality, region, shortcut, history, technique, findings):
        self.modality = modality
        self.region = region
        self.shortcut = shortcut
        self.history = history
        self.technique = technique
        self.findings = findings

    def de_md(self):
        md = []
        md.append(f"# Röntgen {self.region if self.modality == 'cr' else ''}: {self.shortcut}")
        md.append(f"## Klinische Informationen\n{self.history}")
        md.append(f"\n## Technik\n{self.technique}")

        if self.modality=='cr':
            md.append("Die rechtfertigende Indikation gemäß StrSchV §119 wurde durch die im Strahlenschutz fachkundige unterzeichende Person gestellt.")
        
        md.append("\n## Befund")
        
        for finding_category in self.findings:
            for finding_category_name,findings in finding_category.items():
                md.append(f"\n### {finding_category_name}")
                for finding in findings:
                    if isinstance(finding, str):
                        md.append(f"{finding}: Unauffällig")
                    else:
                        for finding, answers in finding.items():
                            md.append(f"{finding}:")
                            for answer in answers['answers']:
                                md.append(f"- [ ] {answer}")
                                
        md.append("\n## Beurteilung")
        return "\n".join(md)

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
                    report = Report(list(modality.keys())[0], region['region'], region['shortcut'], region['history'], region['technique'], region['findings'])
                    print(report.de_md())

def main():
    yaml_file = 'textbausteine.yaml'
    data = read_yaml(yaml_file)
    parse_yaml(data)

if __name__ == "__main__":
    main()
