#!/usr/bin/env python
from fusesoc.capi2.generator import Generator
import subprocess

class BSGFakeramGenerator(Generator):
    def run(self):
        path_to_cfg = self.config.get('path_to_cfg', 'example_cfgs/freepdk45.cfg')
        
        cwd = self.files_root
        
        args = ['cp', '-rf','../bsg_fakeram_gen_0-r1/Makefile','Makefile']
        rc = subprocess.call(args, cwd=cwd)

        args = ['make', 'tools']
        rc = subprocess.call(args, cwd=cwd)
        
        args = ['make', 'run', 'CONFIG=', path_to_cfg]
        rc = subprocess.call(args, cwd=cwd)
        
        args = ['cp', '-rf','results/sram_8x512_1rw/sram_8x512_1rw.v','../generated/bsg_fakeram-gen_0/sram_8x512_1rw.v']
        rc = subprocess.call(args, cwd=cwd)
        
        args = ['cp', '-rf','results/sram_32x32_1rw/sram_32x32_1rw.v','../generated/bsg_fakeram-gen_0/sram_32x32_1rw.v']
        rc = subprocess.call(args, cwd=cwd)

        if rc:
            exit(1)
        
        self.add_files([{ 'sram_8x512_1rw.v' : {'file_type' : 'verilogSource'}}, { 'sram_32x32_1rw.v' : {'file_type' : 'verilogSource'}}])

g = BSGFakeramGenerator()
g.run()
g.write()
