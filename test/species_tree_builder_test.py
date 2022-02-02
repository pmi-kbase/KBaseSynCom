import unittest
import logging
import sys
import os  # noqa: F401
import time
import hashlib
import subprocess
import uuid
from installed_clients.SpeciesTreeBuilderClient import SpeciesTreeBuilder
from installed_clients.WorkspaceClient import Workspace

from configparser import ConfigParser
from KBaseSynCom.KBaseSynComImpl import KBaseSynCom

class MinimalCommunityInstallTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        config = ConfigParser()
        config_file = os.environ.get('KB_DEPLOYMENT_CONFIG', None)
        config.read(config_file)
        cls.cfg = {}
       
        for nameval in config.items('KBaseSynCom'):
            cls.cfg[nameval[0]] = nameval[1]
        wsURL = cls.cfg['workspace-url']
        cls.wsc = Workspace(wsURL)

        cls.callback_url = os.environ['SDK_CALLBACK_URL']
        cls.serviceImpl = KBaseSynCom(cls.cfg)
 

    def test_genomeset_to_tree(self):

      #  workspace = "pranjan77:narrative_1643163998153"
      #  genomeset = "Syncom-PMI_metgenome_2_PFAM_genomeset"
      #  species_tree = "new_tree"
      #  newgenomesetname = "new_tree_genome"

      #  obj = {"workspace": workspace, 'name': genomeset}
      #  oi = self.wsc.get_object_info3({'objects': [obj]})['infos']
      #  obj_id = (str(oi[0][6]) + "/" + str(oi[0][0]) + "/" + str(oi[0][4]))

      #  newgenomesetname = "species_tree_all_genomes-" + str(genomeset)
  
        STB = SpeciesTreeBuilder(self.callback_url)
        params = {
         "genomeset_ref":'63999/95/6' ,
         "nearest_genome_count": 20,
         "copy_genomes": 0,
         "out_tree_id":"species_tree123",
         "out_genomeset_ref": "newgenomesetname123",
          "out_workspace": "pranjan77:narrative_1643163998153",
          "use_ribosomal_s9_only": 0
        }

        s = STB.construct_species_tree(params)
        print (s)




if __name__ == '__main__':
      unittest.main()

