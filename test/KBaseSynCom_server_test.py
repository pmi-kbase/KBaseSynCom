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
import pandas as pd
from collections import Counter

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

    #@unittest.skip('x')
    def test_runSyncom(self):
        # Prepare test objects in workspace if needed using
        # self.getWsClient().save_objects({'workspace': self.getWsName(),
        #                                  'objects': []})
        #
        # Run your method by
        # ret = self.getImpl().your_method(self.getContext(), parameters...)
        #
        # Check returned data with
        # self.assertEqual(ret[...], ...) or other unittest methodsa



        metagenome_pfam_output_files = ["/kb/module/test/metagenome_pfams/BESC-133_Co2_50_25_rhizosphere.pfam", 
                                       "/kb/module/test/metagenome_pfams/BESC-847-Co3_34_soil.pfam",
                                       "/kb/module/test/metagenome_pfams/BESC-Co2_50_25_rhizosphere.pfam",
                                       "/kb/module/test/metagenome_pfams/BESC-133-Co3_19_46_soil.pfam",
                                       "/kb/module/test/metagenome_pfams/BESC-847-Co3_9_34_rhizosphere.pfam",
                                       "/kb/module/test/metagenome_pfams/PMI_metgenome_2_PFAM"]
        #domain_annotation_list = ['63727/187/1', '63727/185/1', '63727/183/1']
        domain_annotation_list = ['63727/3/1',  '63727/5/1', '63727/7/1', '63727/9/1',
                                 '63727/11/1',  '63727/13/1', '63727/15/1', '63727/17/1']
        ret = self.serviceImpl.run_KBaseSynCom(self.ctx, {'workspace_name':"pranjan77:narrative_1643163998153",
                                                        'metagenome_pfam_annotation_files': metagenome_pfam_output_files,
                                                        'genome_domain_annotation_objects': domain_annotation_list,
                                                        'domain_pattern':"domains.*CF365\nHerb",
                                                        'iteration':10, 'workspace_id':63999})
        print (ret)
            


