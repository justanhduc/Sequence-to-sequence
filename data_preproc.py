import glob
import xml.etree.ElementTree as ET
import codecs


jp_list = []
en_list = []
for folder in ('bds', 'ltt', 'hst', 'clt', 'pnm', 'bld', 'fml', 'gnm', 'rlw', 'rod', 'sat', 'scl', 'snt', 'ttl'):
    print('Processing folder %s' % folder)
    file_list = glob.glob('%s/*.xml' % folder)
    for file in file_list:
        print('\tProcessing file %s' % file)
        tree = ET.parse(file, ET.XMLParser(encoding='utf-8'))
        root = tree.getroot()
        for nodes in root.findall('par/sen'):
            jp = None
            en = None
            for childs in nodes.findall('j'):
                jp = childs.text
            for childs in nodes.findall('e'):
                if childs.get('type') == 'check':
                    en = childs.text
            if jp is not None and en is not None:
                jp_list.append(jp)
                en_list.append(en)

if len(jp_list) != len(en_list):
    raise ValueError('Two lists must be the same')
jp_file = codecs.open('training.jp', 'w', 'utf-8')
for line in jp_list:
    jp_file.write('%s\n' % line)
jp_file.close()

en_file = codecs.open('training.en', 'w', 'utf-8')
for line in en_list:
    en_file.write('%s\n' % line)
en_file.close()