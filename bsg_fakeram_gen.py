#!/usr/bin/env python
from fusesoc.capi2.generator import Generator
import subprocess
import json

class BSGFakeramGenerator(Generator):
    def run(self):
        path_to_cfg = self.config.get('path_to_cfg', 'example_cfgs/freepdk45.cfg')
        
        cwd = self.files_root
        
        args = ['cp', '-rf','../bsg_fakeram_gen_0-r1/Makefile','Makefile']
        rc = subprocess.call(args, cwd=cwd)

        args = ['make', 'tools']
        rc = subprocess.call(args, cwd=cwd)

        args = ['cp', str(path_to_cfg),'./conf.cfg']
        rc = subprocess.call(args, cwd=cwd)
        
        args = ['make', 'run']
        rc = subprocess.call(args, cwd=cwd)
        
        f = open('conf.cfg',"r")
        data=json.load(f)
        for i in data["srams"]:
            a=i["name"]
            args = ['cp', '-rf','results/{}/{}.v'.format(a,a),'../generated/bsg_fakeram-gen_0/{}.v'.format(a)]
            rc = subprocess.call(args, cwd=cwd)
            self.add_files([{ '{}.v'.format(a) : {'file_type' : 'verilogSource'}}])
        
        if rc:
            exit(1)

g = BSGFakeramGenerator()
g.run()
g.write()
