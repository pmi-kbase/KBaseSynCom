import unittest
import logging
import sys
import os  # noqa: F401
import time
import hashlib
import subprocess
import uuid


class MinimalCommunityInstallTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__LOGGER = logging.getLogger('MinimalCommunityInstallTest')
        cls.__LOGGER.setLevel(logging.INFO)
        streamHandler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s")
        formatter.converter = time.gmtime
        streamHandler.setFormatter(formatter)
        cls.__LOGGER.addHandler(streamHandler)
        cls.__LOGGER.info("Logger was set")


    def test_minimial_community_install(self):

        resultdir = os.path.join( '/kb/module/work', str(uuid.uuid4().hex))
        
        if not os.path.exists(resultdir) :
            os.makedirs(resultdir)

        metagenomefileName="/kb/module/test/data/metagenomefileName.txt"
        genomeVectorFileName="/kb/module/test/data/genomeVectorFileName.txt"
        iteration = 10
        mimicOutputName = resultdir + "/" + "mimicOutputName.txt"
        kneepointbasedOutputName = resultdir + "/" + "kneepointbasedOutputName.txt"

        minimal_community_run = subprocess.run(["/kb/module/scripts/run_minimal_community_builder.sh",
                                 resultdir,
                                 metagenomefileName,
                                 genomeVectorFileName,
                                 str(iteration),
                                 mimicOutputName,
                                 kneepointbasedOutputName
                                 ]) 
        print("The exit code was: %d" % minimal_community_run.returncode)
        print ("Result directory is " + resultdir)  
        self.assertTrue(os.path.exists(mimicOutputName))
        self.assertTrue(os.path.exists(kneepointbasedOutputName))



if __name__ == '__main__':
      unittest.main()

