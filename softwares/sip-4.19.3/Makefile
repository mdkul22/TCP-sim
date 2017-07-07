
all:
	@(cd sipgen; $(MAKE))
	@(cd siplib; $(MAKE))

install:
	@(cd sipgen; $(MAKE) install)
	@(cd siplib; $(MAKE) install)
	@test -d $(DESTDIR)/home/mdk/Desktop/TCP-sim/tcp_sim/lib/python2.7/site-packages || mkdir -p $(DESTDIR)/home/mdk/Desktop/TCP-sim/tcp_sim/lib/python2.7/site-packages
	cp -f sipconfig.py $(DESTDIR)/home/mdk/Desktop/TCP-sim/tcp_sim/lib/python2.7/site-packages/sipconfig.py
	cp -f /home/mdk/Desktop/TCP-sim/softwares/sip-4.19.3/sipdistutils.py $(DESTDIR)/home/mdk/Desktop/TCP-sim/tcp_sim/lib/python2.7/site-packages/sipdistutils.py

clean:
	@(cd sipgen; $(MAKE) clean)
	@(cd siplib; $(MAKE) clean)
