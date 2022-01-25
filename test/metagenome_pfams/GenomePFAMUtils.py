import os
from collections import Counter
import pandas as pd
from installed_clients.WorkspaceClient import Workspace



class GenomePFAMUtils:

    def __init_(self, Config, logger=None):
        ws_url = Config['ws_url']
        self.wsClient = Workspace(ws_url)
        pass


    def Merge(self, dict1, dict2):
        res = {**dict1, **dict2}
        return res

    def merge_counters(self, all_pfam_counters):
        pfam_counts = Counter([])
        updated_counter_dict = dict()
        for genome in all_pfam_counters:
            pfam_counts = pfam_counts + all_pfam_counters[genome]

        all_pfam_zero_values = Counter({x:0 for x in pfam_counts})
        for genome in all_pfam_counters:
            updated_counter_dict[genome] = self.Merge(all_pfam_zero_values, all_pfam_counters[genome])

        return (updated_counter_dict)

    def get_pfam_counts(self, obj_id):
        obj1 = self.wsClient.get_objects2({'objects': [{'ref': obj_id}]})
        annotation=obj1['data'][0]['data']['data']
        pfam_list = list()
        for contig_id in annotation:
            for gene in annotation[contig_id]:
                for domain in gene[4].keys():
                    if domain.startswith('PF'):
                        pfam_list.append(domain)
        pfam_counts=Counter(pfam_list)
        return (pfam_counts)

    def get_counter_from_metagenome_pfam_output_file(self, metagenome_pfam_output):
        with open (metagenome_pfam_output) as f:
            lines = f.readlines()
        pfam_list = list()
        for j in lines:
            pfam = j.split()[2]
            pfam_list.append(pfam)
        pfam_counter = Counter(pfam_list)
        return (pfam_counter)

    def merged_pfam_workflow(self, metagenome_pfam_output_files, merged_pfam_output_file):
        all_pfam_counters = dict()
        for file in metagenome_pfam_output_files:
            all_pfam_counters[file] = self.get_counter_from_metagenome_pfam_output_file(file)

        merged_all_obj_count = self.merge_counters(all_pfam_counters)
        df=pd.DataFrame(merged_all_obj_count)
 
        df[df > 0] = 1
        df.to_csv(merged_pfam_output_file, sep="\t", index_label="PfamID")

        return ("path of merged pfam file is: "  + merged_pfam_output_file)
 
     def merged_domain_annotation_workflow(self, domain_annotation_list, merged_pfam_output_file):
        all_pfam_counters = dict()

        for obj in domain_annotation_list:
            all_pfam_counters[obj] = self.get_pfam_counts(obj)

        merged_all_obj_count = self.merge_counters(all_pfam_counters)
        df=pd.DataFrame(merged_all_obj_count)

        df[df > 0] = 1
        df.to_csv(merged_pfam_output_file, sep="\t", index_label="PfamID")

        return ("path of merged pfam file is: "  + merged_pfam_output_file)
         
if __name__ == '__main__':

    merged_pfam_output_file = "metagenome_pfam_merged.txt"
    metagenome_pfam_output_files = ["metagenome1.faa.pfam", "metagenome1_copy.faa.pfam"]

    mutils = MetagenomePFAMUtils()
    output = mutils.merged_pfam_workflow(metagenome_pfam_output_files, merged_pfam_output_file)
    print (output) 
  
    domain_annotation_list = ['63727/187/1', '63727/185/1', '63727/183/1'] 
    merged_genome_domain_annotation_file = "genome_pfam_annotation_merged.txt" 
    output = mutils.merged_domain_annotation_workflow(domain_annotation_list, merged_genome_domain_annotation_file)
    
