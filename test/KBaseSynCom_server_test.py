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
        metagenome_pfam_output_files = ["/kb/module/test/metagenome_pfams/PMI_metgenome_1_PFAM", 
                                       "/kb/module/test/metagenome_pfams/PMI_metgenome_2_PFAM"]
        #domain_annotation_list = ['63727/187/1', '63727/185/1', '63727/183/1']
        domain_annotation_list = ['63727/3/1',  '63727/5/1', '63727/7/1', '63727/9/1',
                                 '63727/11/1',  '63727/13/1', '63727/15/1',
         '63727/17/1',
         '63727/19/1',
         '63727/21/1',
         '63727/23/1',
         '63727/25/1',
         '63727/27/1',
         '63727/29/1',
         '63727/31/1',
         '63727/33/1',
         '63727/35/1',
         '63727/37/1',
         '63727/39/1',
         '63727/41/1',
         '63727/43/1',
         '63727/45/1',
         '63727/47/1',
         '63727/49/1',
         '63727/51/1',
         '63727/53/1',
         '63727/55/1',
         '63727/57/1',
         '63727/59/1',
         '63727/61/1',
         '63727/63/1',
         '63727/65/1',
         '63727/67/1',
         '63727/69/1',
         '63727/71/1',
         '63727/73/1',
         '63727/75/1',
         '63727/77/1',
         '63727/86/1',
         '63727/88/1',
         '63727/90/1',
         '63727/92/1',
         '63727/94/1',
         '63727/96/1',
         '63727/98/1',
         '63727/100/1',
         '63727/102/1',
         '63727/104/1',
         '63727/106/1',
         '63727/108/1',
         '63727/110/1',
         '63727/112/1',
         '63727/114/1',
         '63727/116/1',
         '63727/118/1',
         '63727/120/1',
         '63727/122/1',
         '63727/124/1',
         '63727/126/1',
         '63727/128/1',
         '63727/130/1',
         '63727/132/1',
         '63727/134/1',
         '63727/136/1',
         '63727/138/1',
         '63727/140/1',
         '63727/142/1',
         '63727/144/1',
         '63727/146/1',
         '63727/148/1',
         '63727/150/1',
         '63727/152/1',
         '63727/154/1',
         '63727/156/1',
         '63727/158/1',
         '63727/160/1',
         '63727/162/1',
         '63727/164/1',
         '63727/166/1',
         '63727/168/1',
         '63727/170/1',
         '63727/172/1',
         '63727/175/1',
         '63727/177/1',
         '63727/179/1',
         '63727/181/1',
         '63727/183/1',
         '63727/185/1',
         '63727/187/1',
         '63727/189/1',
         '63727/191/1',
         '63727/193/1',
         '63727/195/1',
         '63727/198/1',
         '63727/200/1',
         '63727/202/1',
         '63727/204/1',
         '63727/206/1',
         '63727/208/1',
         '63727/210/1',
         '63727/212/1',
         '63727/214/1',
         '63727/217/1',
         '63727/219/1',
         '63727/221/1',
         '63727/223/1']
        ret = self.serviceImpl.run_KBaseSynCom(self.ctx, {'workspace_name':"pranjan77:narrative_1642294515776",
                                                        'metagenome_pfam_annotation_files': metagenome_pfam_output_files,
                                                        'genome_domain_annotation_objects': domain_annotation_list,
                                                        'iteration':10})
        print (ret)
            
 
