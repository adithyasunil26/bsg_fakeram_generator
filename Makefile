export TOP_DIR := ~/.cache/fusesoc/bsg_fakeram_0-r1

export CACTI_BUILD_DIR := tools/cacti

CONFIG := example_cfgs/freepdk45.cfg

run:
	./scripts/run.py $(CONFIG)

view.%:
	klayout ./results/$*/$*.lef &

clean:
	rm -rf ./results

#=======================================
# TOOLS
#=======================================

tools: $(CACTI_BUILD_DIR)

$(CACTI_BUILD_DIR):
	mkdir -p $(@D)
	git clone https://github.com/HewlettPackard/Cacti.git $@
	cd $@; git checkout 1ffd8dfb10303d306ecd8d215320aea07651e878
	cd $@; git apply $(TOP_DIR)/patches/cacti.patch
	cd $@; make -j4

clean_tools:
	rm -rf $(CACTI_BUILD_DIR)