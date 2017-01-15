% (c) 2009 Eric R. Jeschke (eric@redskieatnight.com) 
%
% This work is licensed under a Creative Commons Attribution-Share Alike
% 3.0 United States License
% See http://creativecommons.org/licenses/by-sa/3.0/us/
%
% Eric Jeschke makes no representation about the suitability or accuracy
% of this software or data for any purpose, and makes no warranties,
% either express or implied, including merchantability and fitness for a
% particular purpose or that the use of this software or data will not
% infringe any third party patents, copyrights, trademarks, or other
% rights.  The software and data are provided "as is". 

This a latex implementation of a photo book or photo folio.  It has been
used to create a PDF photo book that has low-res images suitable for web
display, and also will generate a hi-res version that is compatible with
the Blurb.com "PDF to Book" publish on demand process
(http://www.blurb.com/make/pdf_to_book).  It will also make a "folio"
PDF--a stack of prints with some front and back material, both hi-res
print and lo-res web versions.

This particular example was for the 10x8 softcover book, although it
should be straightforward to tweak this to other sizes, compared to GUI
desktop publishing systems.  The folios are targeted to 8.5x11 letter
size paper, a common inkjet paper size, although the photos are in the
same size/resolution as the book.

To use this, you will need a decent implementation of xelatex or
pdflatex.  I use the excellent version of xelatex that is bundled with
the "texlive" TeX distribution--just google for "texlive" and your
platform (MacOS, Windows, Linux, etc.)

Files of interest:

- Makefile
  Used to build the different vesions.  Targets: all, book-web,
  book-blurb, folio-web, folio-print.  This tar file comes with sample
  images to build "book-web" and "folio-web".

- common-book.tex
  Content that is common to both web and book (POD) versions

- book-web.tex
  Top level file for the book (web version) PDF

- book-blurb.pdf
  Top level file for the book (Blurb version) PDF (minus cover).  This
  is uploaded as the "text block PDF" to blurb.com

- cover-blurb.pdf
  Top level file for creating the wraparound cover for the book (Blurb
  version) PDF.  This is uploaded as the "cover PDF" to blurb.com

- folio-web.tex
  Top level file for the folio (web version) PDF

- folio-print.pdf
  Top level file for the folio (print version PDF).  Designed to be 
  printed via inkjet.

- sRGB.icm
  Generic sRGB profile for embedding in images.  You can use another
  profile if you like.

- cvt.py
  Script for downsampling master image files for use in the documents

IMAGE PREPARATION

I create two directories, "photos.web" and "photos.book" which I
populate with images downsampled to 144dpi and 300dpi, respectively, at
the same "printed" dimensions (e.g. 8x6in).

Personally, I use ImageMagick's "convert" to downsample the master image
files to the two different resolutions used for the web and book.  The 
included script cvt.py does this.

Suppose you have prepared a directory "photos.master" with all the
postprocessed image files in there saved as TIFFs, but not downsampled.
Then you could create the necessary images like this (images will be 8
inches on the long dimension):

$ mkdir photos.web photos.book
$ ./cvt.py --dst=photos.web --dpi=144 --length=8 photos.master/*.tif
$ ./cvt.py --dst=photos.book --dpi=300 --length=8 photos.master/*.tif

The default sharpening parameter is probably sufficient for average use,
but as sharpening is a very personal preference and very dependent upon
the imput files I recommend you to adjust it as necessary.  In
particular, the book version at 300 dpi should probably have more
sharpening applied (the default is rather mild sharpening for the web
version).  You will have to learn the arcana of ImageMagick's sharpening
algorithm, which is somewhat challenging to grok.

COMMENTS

If someone with more TeX experience wanted to wrap all this up into a
nice blurb.sty file it would be really useful, especially if it captured
the different size books that they offer and did all the calculations
for you!

Questions, comments --> eric@redskiesatnight.com

Download: http://redskiesatnight.com/books/pod/latex

Good Luck!

Eric Jeschke
redskiesatnight.com

