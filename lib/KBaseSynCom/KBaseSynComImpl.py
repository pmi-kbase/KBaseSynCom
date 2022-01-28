# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
from .Utils.PFAMUtils import PFAMUtils
from .Utils.MinimalCommunityUtils import MinimalCommunityUtils
from .Utils.htmlreportutils import htmlreportutils
from .Utils.GenomeSetsfromMimic import GenomeSetsfromMimic
import uuid
#END_HEADER


class KBaseSynCom:
    '''
    Module Name:
    KBaseSynCom

    Module Description:
    A KBase module: KBaseSynCom
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
  
        self.ws_url = config['workspace-url']
        self.hr = htmlreportutils()

        #END_CONSTRUCTOR
        pass


    def run_KBaseSynCom(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_KBaseSynCom
      
        print (params) 
        metagenome_pfam_annotation_file_list = params['metagenome_pfam_annotation_files']
        genome_domain_annotation_object_list = params['genome_domain_annotation_objects']
        iteration = str(params['iteration'])
        #TODO: change randomname to uui
        results_dir = os.path.join(self.shared_folder, str(uuid.uuid4()))

        #TODO: change to if dir exists

        workspace = params['workspace_name']

        config ={'ws_url': self.ws_url}
        config ['workspace'] = params['workspace_name']
        PFU = PFAMUtils(config)
        os.makedirs (results_dir) 
        merged_metagenome_pfam_file_path = os.path.join(results_dir, "merged_metagenome_pfam_file.tsv")
        merged_genome_pfam_annotation_file_path = os.path.join(results_dir, "merged_genome_pfam_file.tsv")

        updated_merged_metagenome_pfam_file_path = os.path.join(results_dir, "updated_merged_metagenome_pfam_file.tsv")
        updated_merged_genome_pfam_annotation_file_path = os.path.join(results_dir, "updated_merged_genome_pfam_file.tsv")
        

        mpath =PFU.merged_pfam_workflow(metagenome_pfam_annotation_file_list,merged_metagenome_pfam_file_path)
        gpath = PFU.merged_domain_annotation_workflow(genome_domain_annotation_object_list, merged_genome_pfam_annotation_file_path)

        updated_mpath, updated_gpath = PFU.get_updated_files_with_common_pfams(merged_metagenome_pfam_file_path,
                                                                               merged_genome_pfam_annotation_file_path,
                                                                               updated_merged_metagenome_pfam_file_path,
                                                                               updated_merged_genome_pfam_annotation_file_path)
        updated_mpath_file = updated_mpath.split("/")[-1] 
        updated_gpath_file = updated_gpath.split("/")[-1] 
      
        MCU = MinimalCommunityUtils()
       
        mcuinfo = MCU.run_minimal_community_workflow(results_dir, updated_mpath_file, updated_gpath_file, iteration) 

        GSM = GenomeSetsfromMimic(config)
        #TODO: Get prefix from params
        prefix = "Syncom"
        
        #TODO: ASk users if they want all genomes or just kneepoint genomes
        mimicoutput = mcuinfo['mimicOutputName']
        #genomesetlist, treelist = GSM.mimicoutput_to_allgenomesets(mimicoutput, prefix)
        genomesetlist = GSM.mimicoutput_to_allgenomesets(mimicoutput, prefix)

        created_objects = []

        for count, genomeset in enumerate(genomesetlist):
           created_objects.append({
                   "ref": genomeset,
                    "description": str(count)
            }) 
        #for count,species_tree in enumerate(treelist):
        #   created_objects.append({
        #           "ref": species_tree,
        #            "description": str(count)
        #    })

 
        created_objects=[]
        output = self.hr.formathtmlreport(results_dir,
                                            workspace,
                                            created_objects)
        print (output)
        print (mcuinfo)
        
        

       # report = KBaseReport(self.callback_url)
       # report_info = report.create({'report': {'objects_created':[],
      #                                          'text_message': "successful run"},
      #                                          'workspace_name': params['workspace_name']})
       # output = {
       #     'report_name': report_info['name'],
       #     'report_ref': report_info['ref'],
       # }
        #END run_KBaseSynCom

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_KBaseSynCom return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
