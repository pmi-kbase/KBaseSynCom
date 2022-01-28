import logging
import sys
import os  # noqa: F401
import time
import hashlib
import subprocess
import uuid
from collections import defaultdict
from installed_clients.WorkspaceClient import Workspace
from installed_clients.kb_SetUtilitiesClient import kb_SetUtilities
from installed_clients.SpeciesTreeBuilderClient import SpeciesTreeBuilder

class GenomeSetsfromMimic():

    def __init__(self, config):
        self.ws_url = config['ws_url']
        self.wsc = Workspace(self.ws_url)
        self.workspace_name = config['workspace']
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.listofgenomes_in_genomeset = dict() 
        pass

    def genomelist_to_genomeset(self, genomelist, object_name, workspace_name):
         params = {
            'workspace_name': workspace_name,
            'input_refs': genomelist,
            'output_name': object_name,
            'desc': 'Minimal consortia'
         }
         kbs = kb_SetUtilities(self.callback_url)
         result = kbs.KButil_Build_GenomeSet(params)
         print (result)
         return object_name

    def domainannotation_to_genome(self, domainannotation):
        genome = self.wsc.get_object_subset([{
           'included': ['/genome_ref'],
            'ref': domainannotation 
            }])[0]['data']['genome_ref']
        
        return genome
    def domainannotationlist_to_genomeset(self, domainannotationlist, metagenome_name, prefix):
        genomeset_name = str(prefix) + "-" + str(metagenome_name) + "_genomeset"
        genomelist = list()
        for d in domainannotationlist:
            genome = self.domainannotation_to_genome(d)
            genomelist.append(genome)

        genomeset = self.genomelist_to_genomeset (genomelist, genomeset_name, self.workspace_name)
        self.listofgenomes_in_genomeset[genomeset] = genomelist
        return (genomeset)

    #TODO: Currently not being used anywhere because of errors
     # Fix this in futuree
    def genomeset_to_tree(self, genomeset, species_tree, workspace):
        obj = {"workspace": workspace, 'name': genomeset}
        oi = self.wsc.get_object_info3({'objects': [obj]})['infos']
        obj_id = (str(oi[0][6]) + "/" + str(oi[0][0]) + "/" + str(oi[0][4]))

        STB = SpeciesTreeBuilder(self.callback_url)
        newgenomesetname = "species_tree_all_genomes-" + str(genomeset)
        params = {
         "new_genomes": obj_id,
         "nearest_genome_count": 20,
         "copy_genomes": 0,
         "out_tree_id":species_tree,
         "out_genomeset_ref": newgenomesetname,
          "out_workspace": workspace
        }
        print ("################")

        print (obj_id)
        print (params)

        print ("################")
        s = STB.construct_species_tree(params)
        return (s['output_result_id'])



    def mimicoutput_to_allgenomesets(self, mimicoutput, prefix):
        genomesetlist = list()
        treelist = list()
        with open (mimicoutput, 'r') as m:
            lines = m.readlines()

        metagenome_domainobjs_dict = defaultdict(list)
        for line in lines:
            if line.startswith("MetaGenome"):
                    continue
            columns = line.split("\t")
            metagenome = columns[0].split("/")[-1]
            domainobject = columns[1]
            metagenome_domainobjs_dict[metagenome].append(domainobject)

        for metagenome in metagenome_domainobjs_dict:
            domainobjlist = metagenome_domainobjs_dict[metagenome]
            genomeset = self.domainannotationlist_to_genomeset(domainobjlist, metagenome, prefix)
            genomesetlist.append(genomeset)

        for genomeset in genomesetlist:
            species_tree = "species_tree-" + str(genomeset)
            genomelist = self.listofgenomes_in_genomeset[genomeset]
         #   tree = self.genomeset_to_tree(genomeset, species_tree, self.workspace_name)
         #   print (tree)
         #   treelist.append(tree)
         #   print(treelist)
            print (genomelist)
        #return (genomesetlist, treelist)
        return (genomesetlist)


        #return (all_genomesets_created)






if __name__ == '__main__':
    config = {
     'workspace-url':"https://appdev.kbase.us/services/ws",
     'workspace_name': 'pranjan77:narrative_1643163998153'
    }
    GSM = GenomeSetsfromMimic(config)
    mimicoutput = "/kb/module/work/tmp/a8b3c2a8-df72-4fca-9cf2-3b6d471204f4/mimicOutputName.txt"
    prefix = "run10"
    g = GSM.mimicoutput_to_allgenomesets(mimicoutput, prefix)
    print (g)
