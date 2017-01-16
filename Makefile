#
# Photography Book Makefile
# Eric Jeschke  2009-08-08
#
# Pass environment variables to sub-make's
#.EXPORT_ALL_VARIABLES
.PHONY: all book-blurb book-photos sweep clean tar

BOOK_DOCs = common-book.tex
#CMD  = pdflatex
CMD  = xelatex
ARGS = -output-driver="xdvipdfmx -q -E -V 3"

PHOTO_format = jpg
PHOTOs_master = $(wildcard photos.master/*)
PHOTOs_book = $(addsuffix .$(PHOTO_format),$(addprefix photos.book/,$(basename $(notdir $(PHOTOs_master)))))

all: book-blurb

book-blurb: book-blurb.pdf cover-blurb.pdf

book-blurb.pdf: book-blurb.tex $(BOOK_DOCs) $(PHOTOs_book)
	$(CMD) $(ARGS) $<

cover-blurb.pdf: cover-blurb.tex $(PHOTOs_book)
	$(CMD) $(ARGS) $<

book-photos: $(PHOTOs_book)

$(PHOTOs_book): | photos.book
	./cvt.py --format=$(PHOTO_format) --dst=photos.book --dpi=300 --length=8 $<

# Devilish rule generator to associate each photo with its original
$(foreach rule,$(join $(addsuffix :,$(PHOTOs_book)),$(PHOTOs_master)),$(eval $(rule)))

photos.book:
	mkdir $@

sweep:
	-/bin/rm -f *~ *.out *.aux *.log \#*\# 

clean: sweep
	-/bin/rm -f *.pdf 
	-/bin/rm -rf photos.book

tar: sweep
	cd ..; tar czf blurb_latex.tgz --exclude=photos.master latex

# END
