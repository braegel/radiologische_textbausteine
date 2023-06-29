
import argparse
import yaml
from lxml import etree
from rdflib import Graph, Namespace, URIRef

def extract_info(input_file, output_file):
    g = Graph()
    g.parse(input_file)

    RAD = Namespace('http://www.radlex.org/RID/')

    data_dict = {}
    for s, o in g.subject_objects(RAD.Preferred_name_German):
        data_dict[str(o)] = str(s.split('/')[-1])

    sorted_dict = dict(sorted(data_dict.items()))

    with open(output_file, "w", encoding='utf-8') as f:
        yaml.dump(sorted_dict, f, allow_unicode=True)

def main():
    parser = argparse.ArgumentParser(description='Erstellt einen Index aus deutschen radiologischen Begriffen und deren Radlink-ID. '
                                                 'Das Script benötigt zwei Argumente: Den Pfad zur Radlex OWL-Datei und den Pfad zur Ausgabe-YAML-Datei.')
    parser.add_argument('input_file', help='Der Pfad zur Eingabe-OWL-Datei.')
    parser.add_argument('output_file', help='Der Pfad zur Ausgabe-YAML-Datei.')
    args = parser.parse_args()

    extract_info(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
