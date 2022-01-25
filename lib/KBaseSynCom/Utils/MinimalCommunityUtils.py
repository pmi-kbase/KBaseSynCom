import logging
import sys
import os  # noqa: F401
import time
import hashlib
import subprocess
import uuid


class MinimalCommunityUtils():

    def __init__(self):
        pass

    def run_minimal_community_workflow(self, resultdir, metagenomefileName, genomeVectorFileName, iteration):

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
        resultdict = dict()

        resultdict['metagenomefileName'] = metagenomefileName
        resultdict['genomeVectorFileName']= genomeVectorFileName
        resultdict['iteration'] = str(iteration)
        resultdict['output_dir'] = resultdir
        resultdict['mimicOutputName'] = mimicOutputName
        resultdict['kneepointbasedOutputName'] = kneepointbasedOutputName
        return (resultdict)




if __name__ == '__main__':
       x=1
