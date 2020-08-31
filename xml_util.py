import xml.etree.ElementTree as ET
from jinja2 import Template

### Annotation file read methods.
def get_title(xml_root):
    pub_details = xml_root.find('{http://ns.adobe.com/digitaleditions/annotations}publication')
    return pub_details.find('{http://purl.org/dc/elements/1.1/}title').text

def get_author(xml_root):
    pub_details = xml_root.find('{http://ns.adobe.com/digitaleditions/annotations}publication')
    return pub_details.find('{http://purl.org/dc/elements/1.1/}creator').text

def get_annotation(annotation):
    target = annotation.find('{http://ns.adobe.com/digitaleditions/annotations}target')
    fragment = target.find('{http://ns.adobe.com/digitaleditions/annotations}fragment')
    text = fragment.find('{http://ns.adobe.com/digitaleditions/annotations}text')
    if text == None:
        return ''
    else:
        return text.text

def get_annotations(xml_root):
    annotations = xml_root.findall('{http://ns.adobe.com/digitaleditions/annotations}annotation')
    data = []
    for i in annotations:
        data.append(get_annotation(i))
    return data
    
def get_xml_root(filepath):
    tree = ET.parse(filepath)
    return tree.getroot()
    
def check_annotations(filepath):
    xml_root = get_xml_root(filepath)
    if xml_root.find('{http://ns.adobe.com/digitaleditions/annotations}annotation') != None:
        return True
    return False

def read_annotation_file(filepath):
    xml_root = get_xml_root(filepath)
    data = {
        'title' : get_title(xml_root),
        'author' : get_author(xml_root)
    }
    data['annotations'] = get_annotations(xml_root)
    return data
    
def read_annotation_file(filepath):
    xml_root = get_xml_root(filepath)
    data = {
        'title' : get_title(xml_root),
        'author' : get_author(xml_root)
    }
    data['annotations'] = get_annotations(xml_root)
    return data

### HTML Render methods
def clean_title(title):
    new_title = title.replace(':', '')
    new_title = new_title.replace('>', '')
    new_title = new_title.replace('<', '')
    new_title = new_title.replace('"', '')
    new_title = new_title.replace('\/', '')
    new_title = new_title.replace('\\', '')
    new_title = new_title.replace('|', '')
    new_title = new_title.replace('?', '')
    return new_title.replace('*', '')

def render_annotation_page(data, output_dir):
    with open('out_template.html', 'r', encoding='utf-8') as file:
        template = Template(file.read())
        
    with open(f"{output_dir}\\{clean_title(data['title'])}.html", 'w') as file:
        file.write(template.render(data=data))