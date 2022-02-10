import unittest
import os
from collections import Counter
import pandas as pd
from installed_clients.WorkspaceClient import Workspace
from installed_clients.DataFileUtilClient import DataFileUtil


class DownloadMetagenomeProteins(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.token = "QILO3G4OL32GZHHLULNMQ3U2KSLCXLIA"
        ws_url = "https://kbase.us/services/ws"
        self.wsClient = Workspace (ws_url, token=self.token)
        pass

    @classmethod
    def get_protein_handle_from_metagenome(self, ama_ref):
        protein_handle = self.wsClient.get_object_subset([{
               'included': ['/protein_handle_ref'],
               'ref': ama_ref
                }])[0]['data']['protein_handle_ref']
        return (protein_handle)

    @classmethod
    def get_protein_file(self, ama_ref):
        protein_handle = self.get_protein_handle_from_metagenome(ama_ref)
        print ("################")
        print (protein_handle)
        print ("################")
         
        protein_file = "/kb/module/work/tmp/test.fa.gz"
        dfu = DataFileUtil(os.environ['SDK_CALLBACK_URL'], token=self.token) 
        shock_to_file = dfu.shock_to_file({'handle_id': protein_handle, 'file_path': protein_file})
        return (shock_to_file)

 
    def test_download(self):      
       m =DownloadMetagenomeProteins()
       ama_ref = "100072/31/1"
       x = m.get_protein_file(ama_ref) 
       print (x)
