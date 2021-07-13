#!/usr/bin/env python
from fusesoc.capi2.generator import Generator
import subprocess

class BSGRoundRobinArbGenerator(Generator):
    def run(self):
        # channels = self.config.get('channels', 16)
        cwd = self.files_root
        args = ['make', 'tools']
        
        rc = subprocess.call(args, cwd=cwd)
        
        args = ['make', 'run', 'CONFIG=',str(path_to_cfg)]
        
        rc = subprocess.call(args, cwd=cwd)
        
        if rc:
            exit(1)
        
        # self.add_files([{ 'bsg_round_robin_arb.v' : {'file_type' : 'verilogSource'}}])

g = BSGRoundRobinArbGenerator()
g.run()
g.write()