# -*- coding: utf-8 -*-
import os
import time
import unittest
from configparser import ConfigParser

from KBaseSynCom.KBaseSynComImpl import KBaseSynCom
from KBaseSynCom.KBaseSynComServer import MethodContext
from KBaseSynCom.authclient import KBaseAuth as _KBaseAuth

from installed_clients.WorkspaceClient import Workspace
from installed_clients.DataFileUtilClient import DataFileUtil


class KBaseSynComTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = os.environ.get('KB_AUTH_TOKEN', None)
        config_file = os.environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('KBaseSynCom'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'KBaseSynCom',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = Workspace(cls.wsURL)
        cls.serviceImpl = KBaseSynCom(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']
        suffix = int(time.time() * 1000)
        cls.wsName = "test_ContigFilter_" + str(suffix)
        ret = cls.wsClient.create_workspace({'workspace': cls.wsName})  # noqa

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    @classmethod
    def get_protein_handle_from_metagenome(self, ama_ref):
        protein_handle = self.wsClient.get_object_subset([{
               'included': ['/protein_handle_ref'],
               'ref': ama_ref
                }])[0]['data']['protein_handle_ref']
        return (protein_handle)

    @classmethod
    def features_from_genome(self, genome_ref):
        genome_features  = self.wsClient.get_object_subset([{
               'included': ['/features'],
               'ref': genome_ref
                }])[0]['data']['features']
        return (genome_features)

    @classmethod
    def splitSequence(self, seq):
        colsz = 50
        start = 0
        lenseq = len(seq)
        line = ""

        while True:
            end = start + colsz
            if end > lenseq:
                end = lenseq
            # print seq[start:end]
            line += seq[start:end] + "\n"
            start += colsz
            if start > lenseq:
#                False
                break
        return line


    @classmethod
    def create_Fasta_from_features(self, pyStr):
        myFeat = pyStr
        line = ""
        for feat in myFeat:
            if 'function' not in feat:
                feat['function'] = 'unknown'
            if 'type' in feat and feat['type'] not in ['CDS', 'gene']:
                continue

            if ('protein_translation' in feat):
                line += ">" + feat['id'] + " " + feat['function']
                line += " (len=" + str(feat['protein_translation_length']) + ")" + "\n"

                # print line
                line += self.splitSequence(feat['protein_translation']) + "\n"
        return line


    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    @unittest.skip('x')
    def test_your_method(self):
        # Prepare test objects in workspace if needed using
        # self.getWsClient().save_objects({'workspace': self.getWsName(),
        #                                  'objects': []})
        #
        # Run your method by
        # ret = self.getImpl().your_method(self.getContext(), parameters...)
        #
        # Check returned data with
        # self.assertEqual(ret[...], ...) or other unittest methods
 #       ret = self.serviceImpl.run_KBaseSynCom(self.ctx, {'workspace_name': self.wsName,
 #                                                            'parameter_1': 'Hello World!'})

        ama_ref = "63670/4/1"
        protein_handle = self.get_protein_handle_from_metagenome(ama_ref)
        print (protein_handle)
         
        protein_file = "/kb/module/work/tmp/test.fa.gz"
        dfu = DataFileUtil(os.environ['SDK_CALLBACK_URL'], token=self.ctx['token']) 
        shock_to_file = dfu.shock_to_file({'handle_id': protein_handle, 'file_path': protein_file})
        print (shock_to_file)
        #self.assertTrue(os.path.exists(protein_file))

    def test_download_genome_protein(self):
        # Prepare test objects in workspace if needed using
        # self.getWsClient().save_objects({'workspace': self.getWsName(),
        #                                  'objects': []})
        #
        # Run your method by
        # ret = self.getImpl().your_method(self.getContext(), parameters...)
        #
        # Check returned data with
        # self.assertEqual(ret[...], ...) or other unittest methods
 #       ret = self.serviceImpl.run_KBaseSynCom(self.ctx, {'workspace_name': self.wsName,
 #                                                            'parameter_1': 'Hello World!'})

        genome_ref = "63151/519/2"
        

        genome_features  = self.features_from_genome(genome_ref)
        fasta_data = self.create_Fasta_from_features(genome_features)

          
        protein_file = "/kb/module/work/genome_protein.fa"
        with open(protein_file, "w") as file1:
            file1.write(fasta_data) 
