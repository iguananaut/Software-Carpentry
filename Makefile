#
# Photography Book Makefile
# Eric Jeschke  2009-08-08
#
# Pass environment variables to sub-make's
#.EXPORT_ALL_VARIABLES

BOOK_DOCS = common-book.tex
FOLIO_DOCs = common-folio.tex
#CMD  = pdflatex
CMD  = xelatex
ARGS = -output-driver="xdvipdfmx -q -E -V 3"

PHOTOs_master = photos.master/*

all: book-web book-blurb folio-web folio-print

book-web: book-web.pdf
book-blurb: book-blurb.pdf cover-blurb.pdf
folio-web: folio-web.pdf
folio-print: folio-print.pdf

book-web.pdf: book-web.tex $(BOOK_DOCs) 
	$(CMD) $<

book-blurb.pdf: book-blurb.tex $(BOOK_DOCs) 
	$(CMD) $(ARGS) $<

cover-blurb.pdf: cover-blurb.tex
	$(CMD) $(ARGS) $<

folio-web.pdf: folio-web.tex $(FOLIO_DOCs) 
	$(CMD) $<

folio-print.pdf: folio-print.tex $(FOLIO_DOCs) 
	$(CMD) $(ARGS) $<

web_photos: $(PHOTOs_master)
	./cvt.py --dst=photos.web --dpi=144 --quality=75 --length=8 $(PHOTOs_master)

book_photos: $(PHOTOs_master)
	./cvt.py --dst=photos.book --dpi=300 --length=8 $(PHOTOs_master)

sweep:
	-/bin/rm *~ *.out *.aux *.log \#*\# 

clean: sweep
	-/bin/rm *.pdf 

tar: sweep
	cd ..; tar czf blurb_latex.tgz --exclude=photos.master --exclude=photos.book latex

# END
