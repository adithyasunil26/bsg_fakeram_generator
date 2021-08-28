# BSG Black-box SRAM Generator for FuseSoC

[FuseSoC](https://github.com/olofk/fusesoc) generator for [bsg_fakeram](https://github.com/bespoke-silicon-group/bsg_fakeram).

### Adding core library to FuseSoC
```bash
fusesoc library add bsg_fakeram https://github.com/adithyasunil26/bsg_fakeram_generator
```

### Testing the generator
The `bsg_fakeram` core can be used to test the functioning of the generator. 

For linting
```bash
fusesoc run --target lint bsg_fakeram
```

### To use a custom config file
Before running the `fusesoc run` command, open the core file present in your `fusesoc_libraries` directory which will be created on executing the previous command and edit the `path_to_cfg` value to match the path to the mentioned file in your file system.


To use a custom config file follow these steps:
1. Navigate to library
```bash
cd fusesoc_libraries/bsg_fakeram/
```
2. Open the `bsg_fakeram.core` file and change `path_to_cfg` to path to custom config file
3. Return to original directory with 
```bash
cd ../..
```
Now you can use the core with the before mentioned targets.


### Using the generator in your own core
In order to use the generator in your cores add the following lines of code to your core

```YAML
generate:
  <name_of_generate_block>:
    generator: bsg_fakeram_gen
    parameters:
      path_to_cfg: '<path_to_config_file>'
```

Also reference the generator in your targets 

```YAML
generate: <name_of_generate_block>
```
