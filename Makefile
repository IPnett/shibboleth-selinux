APP = shibboleth

PWD = $(shell pwd)
TOPDIR = $(PWD)/tmp
OUTPUTDIR = noarch

SELINUX_MAKEFILE = /usr/share/selinux/devel/Makefile


all: build

rpm: build
	rpmbuild -v -bb \
			--define "_sourcedir $(PWD)" \
			--define "_rpmdir $(PWD)" \
			--define "_topdir $(TOPDIR)" \
			$(APP)-selinux.spec
	mv $(OUTPUTDIR)/*.rpm .

build: $(APP).pp 

shibd_selinux.8:
	sepolicy manpage --path . -d shibd_t

shibd_selinux.8.gz: shibd_selinux.8
	gzip -9 < $< >$@

$(APP).pp: $(APP).fc $(APP).if $(APP).te
	make -f $(SELINUX_MAKEFILE)

clean:
	make -f $(SELINUX_MAKEFILE) clean
	rm -rf $(TOPDIR)
	rm -fr $(OUTPUTDIR)
	rm -f *.8 *.gz
	rm -f *.rpm
