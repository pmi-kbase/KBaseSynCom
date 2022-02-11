import uuid
import os
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.KBaseReportClient import KBaseReport
from installed_clients.WorkspaceClient import Workspace
import shutil 
import pandas as pd
from collections import defaultdict
import sys



class htmlreportutils:

    def __init__(self, config):
        callback_url = os.environ['SDK_CALLBACK_URL']
        self.dfu = DataFileUtil(callback_url)
        self.report = KBaseReport(callback_url)
        ws_url = config['ws_url']
        self.ws = Workspace(ws_url)
        self.kbase_endpoint = config['kbase_endpoint'].replace("/services", "")
        self.first_drop_down_page = ""
        pass

    def create_html_report(self, output_dir, workspace_name, objects_created):
        '''
         function for creating html report
        '''

        report_name = 'KBaseSyncomrun_Syncom' + str(uuid.uuid4())

        report_shock_id = self.dfu.file_to_shock({'file_path': output_dir,
                                            'pack': 'zip'})['shock_id']

        html_file = {
            'shock_id': report_shock_id,
            'name': 'index.html',
            'label': 'index.html',
            'description': 'Variation HTML report'
            }
        
        report_info = self.report.create_extended_report({
                        'objects_created': objects_created,
                        'direct_html_link_index': 0,
                        'html_links': [html_file],
                        'report_object_name': report_name,
                        'workspace_name': workspace_name
                    })
        return {
            'report_name': report_info['name'],
            'report_ref': report_info['ref']
        }



    def tab_to_td(self, text):
       htmlstr = "<tr>"
       text = text.strip()
       textsplit = text.split("\t")
       for j in textsplit:

           htmlstr += "<td>" + str(j) + "</td>"
       htmlstr += "</tr>"
       return htmlstr

    def get_full_table_html (self, thead, tbody, template_file, outfile, resultdir):
        with open (template_file, "r") as f:
            template_text  = f.read()

        template_text = template_text.replace("{{THEADTXT}}", thead)
        template_text = template_text.replace("{{TBODYTEXT}}", tbody)

        ofile = resultdir + "/" + outfile
        with open (ofile, "w") as wf:
            wf.write(template_text)
        return (outfile)


    def create_mimic_knee_point_table(self, kneepointfile):
       with open (kneepointfile) as k:
         lines = k.readlines()
       htmlstr = "<table border=1>"
       for line in lines:
           l = line.split("\t")
           if (len(l)==2):
               htmlstr += self.tab_to_td(line)
           else:
               rowstr = str(l[1]) + "\t" + str(l[2])
               htmlstr += self.tab_to_td(rowstr)
       htmlstr += "</table>"
       return (htmlstr)

    def domainannotation_to_genome(self, domainannotation):
        genome = self.ws.get_object_subset([{
           'included': ['/genome_ref'],
            'ref': domainannotation
            }])[0]['data']['genome_ref']

        return genome

    def get_genome_to_name(self, genome_ref):
       genome_name = self.ws.get_object_info3({"objects": [{'ref':genome_ref}], "includeMetadata": 1})['infos'][0][1]
       return (genome_name)

    def get_object_to_name(self, obj):
       obj_name = self.ws.get_object_info3({"objects": [{'ref':obj}], "includeMetadata": 1})['infos'][0][1]
       return (obj_name)


    def update_upa_with_genome_name(self, line):
        d = line.split("\t")
        domainannotation = d[1]
#        genome_ref = self.domainannotation_to_genome(domainannotation)
#        genome_url = self.kbase_endpoint + "/#dataview/" + genome_ref
        durl = self.kbase_endpoint + "/#dataview/" + domainannotation
#        genome_name = self.get_genome_to_name(genome_ref)
        obj_name = self.get_object_to_name(domainannotation)
        d[1] = "<a href ='" + durl  + "' target='_blank' >" + obj_name + "</a>" 
        newline = "\t".join(d)
        return (newline)
        
    def create_drop_down_table(self, metagenome_dict):
       htmlstr = ""
       firstpage = ""
       i =  0
       for j in metagenome_dict:
         metagenome_file_html  = str(j) + ".html"
         if i == 0:
            firstpage = metagenome_file_html
            i = i +1
         htmlstr += '<option value="' + metagenome_file_html + '">' + str(j) + '</option>'

       return (htmlstr, firstpage)

    def create_data_table_html(self, file, template_file, resultdir):

        metagenome_dict = defaultdict(None)
        with open (file, "r") as f:
            lines = f.readlines()

        firstline = ""
        for line in lines:
           if firstline:
               metagenome_id = line.split("\t")[0]
               nline = self.update_upa_with_genome_name(line)
               if metagenome_id in metagenome_dict:
                   metagenome_dict[metagenome_id] = metagenome_dict[metagenome_id] + self.tab_to_td(nline)
               else:
                   metagenome_dict[metagenome_id] = self.tab_to_td(nline)
           else:
               firstline = self.tab_to_td(line)

        for mid in metagenome_dict:
            midofile = str(mid) + ".html"
            ofile =  self.get_full_table_html(firstline, metagenome_dict[mid], template_file, midofile, resultdir)

        return (metagenome_dict)


    def create_index_html(self, index_template, kneepointfile, imgfile1, imgfile2, metagenome_dict, outfile):
        with open (index_template, "r") as f:
            template_text  = f.read()

        mimickneepointtable = self.create_mimic_knee_point_table(kneepointfile)
        dropdowntablehtml, firstpage = self.create_drop_down_table(metagenome_dict)

        template_text = template_text.replace("{{MIMICKNEEPOINTTABLE}}", mimickneepointtable)
        template_text = template_text.replace("{{PFAMCOVERAGE}}", imgfile1)
        template_text = template_text.replace("{{PFAMCOVERAGEKNEEPOINT}}", imgfile2)
        template_text = template_text.replace("{{DROPDOWNTABLE}}", dropdowntablehtml )
        template_text = template_text.replace("{{MYFIRSTPAGE}}", firstpage )

        with open (outfile, "w") as wf:
            wf.write(template_text)
        return (outfile)


    def delete_file (self, file_to_delete):
       if os.path.exists(file_to_delete):
           os.remove(file_to_delete)

    def clean_up (self):
        files_to_delete = ['knee_point_summary.txt',
                          'merged_metagenome_pfam_file.tsv',
                          'merged_genome_pfam_file.tsv',
                          'minimal_community.R',
                          'html.py']
        for f in files_to_delete:
            self.delete_file(f)

    def run_workflow(self, resultdir):
        scriptdir = "/kb/module/scripts"
        mimicfile = resultdir + "/" + "mimicOutputName.txt"
        template_file = scriptdir + "/" + "datatable_template.html"
        index_template = scriptdir + "/" + "index_template.html"
        metagenome_dict = self.create_data_table_html(mimicfile, template_file, resultdir)
        imgfile1 = "Pfam_coverage_plot.jpg"
        imgfile2 = "Pfam_coverage_kneepoint.jpg"
        kneepointfile = resultdir + "/" + "knee_point_summary.txt"
        outfile = resultdir + "/index.html"
        index_page = self.create_index_html(index_template, kneepointfile, imgfile1, imgfile2, metagenome_dict, outfile)
        return (resultdir)


    
    def generate_HTML_report(self, resultdir):
   
        index = resultdir + "/index.html" 
        index = self.run_workflow(resultdir) 
        return (index)

    def formathtmlreport(self, resultsdir, workspace_name, objects_created):

        index = self.generate_HTML_report(resultsdir)
        report_info = self.create_html_report(resultsdir,  workspace_name, objects_created)
        return report_info


