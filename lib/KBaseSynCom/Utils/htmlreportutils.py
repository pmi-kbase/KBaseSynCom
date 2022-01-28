import uuid
import os
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.KBaseReportClient import KBaseReport
from installed_clients.WorkspaceClient import Workspace
import shutil 
import pandas as pd

class htmlreportutils:

    def __init__(self):
        callback_url = os.environ['SDK_CALLBACK_URL']
        self.dfu = DataFileUtil(callback_url)
        self.report = KBaseReport(callback_url)
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

    
    def generate_HTML_report(self, resultdir):
   
        index = resultdir + "/index.html" 
        df = pd.read_csv(resultdir+'/kneepointbasedOutputName.txt',sep='\t', header=0)
        df2 = pd.read_csv(resultdir+'/mimicOutputName.txt',sep='\t', header=0)
        df3 = pd.read_csv(resultdir+'/knee_point_summary.txt',sep='\t', header=0)
        with open(index, 'w') as html_file:
            html_file.write('<body>'+  "Mimic Output" + '</body>')
            html_file.write(df2.to_html(index=False))
            html_file.write('<body>' +  "Knee Point Output" + '</body>')
            html_file.write(df.to_html(index=False))
            html_file.write('<body>' + 'Knee Point Summary' + '</body>')
            html_file.write(df3.to_html(index=False))
        
        f = open(index,'a')
        message = """<html>
            <p><img src="Pfam_coverage_plot.jpg" alt="pfam plot" width="100%" height="600px" /></p>
            <p><iframe src="mbarc_mimic_coverage_ncbiRef_2016_kneePoint.pdf" width="100%" height="1000px" /></p>
            <a href="updated_merged_genome_pfam_file.tsv">Updated Merged Genome Pfam</a> 
            <a href="updated_merged_metagenome_pfam_file.tsv">Updated Merged Metagenome Pfam</a> 
    
            <a href="merged_genome_pfam_file.tsv ">Merged Genome Pfam</a> 
            <a href="merged_metagenome_pfam_file.tsv">Merged Metagenome Pfam</a> 
    
            </html>"""
        f.write(message)
        f.close()    
        return (index)

    def formathtmlreport(self, resultsdir, workspace_name, objects_created):
        #utput_html = resultsdir  + "/" + "index.html"
        #shutil.copyfile("/kb/module/lib/KBaseSynCom/Utils/index.html", output_html )

        index = self.generate_HTML_report(resultsdir)
        report_info = self.create_html_report(resultsdir,  workspace_name, objects_created)
        return report_info


