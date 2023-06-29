import xml.etree.ElementTree as ET
import argparse
def get_preferred_name(xml_file, rid):
    ns = {'owl': 'http://www.w3.org/2002/07/owl#',
          'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
          'rdfs': 'http://www.w3.org/2000/01/rdf-schema#'}
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for elem in root.iter('{http://www.w3.org/2002/07/owl#}Class'):
        if '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about' in elem.attrib:
            about = elem.attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about']
#            print(f'Verarbeite: {about}')
            if about.endswith(rid):
                for child in elem:
                    if 'Preferred_name_German' in child.tag:
#                        print("German Preferred Name gefunden")
                        return child.text
    return None

def main():
    parser = argparse.ArgumentParser(description="Finde den deutschen Namen einer Radlex RID in einer gegebenen XML-Datei.")
    parser.add_argument("xml_file", help="Der Pfad zur XML-Datei.")
    parser.add_argument("rid", help="Die Radlex RID, für die der deutsche Name gesucht wird.")

    args = parser.parse_args()

    result = get_preferred_name(args.xml_file, args.rid)

    if result:
#        print(f"Der deutsche Name für RID {args.rid} ist {result}.")
        print({result})
    else:
        print(f"Kein Eintrag mit RID {args.rid} gefunden.")

if __name__ == "__main__":
    main()
    
