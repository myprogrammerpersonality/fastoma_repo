import xml.etree.ElementTree as ET
from xml.dom import minidom
from os import listdir
import os
import dill as pickle

address_working_folder="/work/FAC/FBM/DBC/cdessim2/default/ayazdiza/fastoma_repo/temp_results/" 
address_group_xml = "/work/FAC/FBM/DBC/cdessim2/default/ayazdiza/fastoma-dask/group_xml_ortho.pickle"
address_pickle_folder = address_working_folder + "/pickles/mid_no_merge_1/"

pickle_files = listdir(address_pickle_folder)
print("num pickle files", len(pickle_files))

with open(address_group_xml, 'rb') as handle:
    (groups_xml, gene_id_name, orthoxml_file) = pickle.load(handle)

for pickle_file in pickle_files:
    pickl_file_path = address_pickle_folder + pickle_file
    if os.path.exists(pickl_file_path): 
        with open(pickl_file_path, 'rb') as handle:
            (HOG_thisLevel_xml_all) = pickle.load(handle)
            for HOG_thisLevel_xml in HOG_thisLevel_xml_all:
                groups_xml.append(HOG_thisLevel_xml)
print("done1")


xml_str = minidom.parseString(ET.tostring(orthoxml_file)).toprettyxml(indent="   ")

output_xml_name= address_working_folder + "/orthoxmls/mid_no_merge_all_qfo.xml"
with open(output_xml_name, "w") as file_out:
    file_out.write(xml_str)

print("done2")
