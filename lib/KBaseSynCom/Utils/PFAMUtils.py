import os
from collections import Counter
import pandas as pd
from installed_clients.WorkspaceClient import Workspace



class PFAMUtils:

    def __init__(self, Config):
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

        return (merged_pfam_output_file)
 
    def merged_domain_annotation_workflow(self, domain_annotation_list, merged_pfam_output_file):
        all_pfam_counters = dict()

        for obj in domain_annotation_list:
            all_pfam_counters[obj] = self.get_pfam_counts(obj)

        merged_all_obj_count = self.merge_counters(all_pfam_counters)
        df=pd.DataFrame(merged_all_obj_count)

        df[df > 0] = 1
        df.to_csv(merged_pfam_output_file, sep="\t", index_label="PfamID")

        return (merged_pfam_output_file)

    def fix_name(self, id):
       ids = id.split("/")
       if (ids[0].isnumeric() and 
          ids[1].isnumeric() and
          ids[2].isnumeric()):
          return id # most probably a workspace upa eg 61234/2/1
       else:
          return id.split ("/")[-1]  # for /kb/module/metagenome1 change to metagenome1

       
        
    def get_updated_files_with_common_pfams(self, file1, file2, out1, out2):
        dfile1 = pd.read_csv(file1, sep='\t', index_col=0)
        dfile2 = pd.read_csv(file2, sep='\t', index_col=0)
        dfile1_columns = dfile1.columns
        dfile2_columns = dfile2.columns

        newdict1 = dict()
        newdict2 = dict()
        for j in dfile1_columns:
            newdict1[j] = self.fix_name(j)
        for j in dfile2_columns:
            newdict2[j] = self.fix_name(j)



        merged_df = pd.concat([dfile1,dfile2], axis=1).fillna(0)

        df1 = merged_df[dfile1_columns]
        df1 = df1.rename(columns=newdict1)
        df1.to_csv(out1, sep="\t", index_label="PfamID")
        
        df2 = merged_df [dfile2_columns]
        df2 = df2.rename(columns=newdict2)
        df2.to_csv(out2, sep="\t", index_label="PfamID")
        return (out1, out2)





if __name__ == '__main__':
    pass
    #merged_pfam_output_file = "metagenome_pfam_merged.txt"
    #metagenome_pfam_output_files = ["metagenome1.faa.pfam", "metagenome1_copy.faa.pfam"]

    #mutils = PFAMUtils()
    #output = mutils.merged_pfam_workflow(metagenome_pfam_output_files, merged_pfam_output_file)
    #print (output) 
  
#    domain_annotation_list = ['63727/187/1', '63727/185/1', '63727/183/1'] 
#    merged_genome_domain_annotation_file = "genome_pfam_annotation_merged.txt" 
#    output = mutils.merged_domain_annotation_workflow(domain_annotation_list, merged_genome_domain_annotation_file)
    
