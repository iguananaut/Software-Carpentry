#! /usr/bin/env python
#
"""
cvt.py -- script to downsample images for book creation

Comments, patches welcome:
Eric Jeschke (eric@redskiesatnight.com)

(c) 2009 Eric R. Jeschke (eric@redskieatnight.com).
This work is licensed under a Creative Commons Attribution-Share Alike
3.0 United States License
See http://creativecommons.org/licenses/by-sa/3.0/us/

  Eric Jeschke makes no representation about the suitability or accuracy
  of this software or data for any purpose, and makes no warranties,
  either express or implied, including merchantability and fitness for a
  particular purpose or that the use of this software or data will not
  infringe any third party patents, copyrights, trademarks, or other
  rights.  The software and data are provided "as is".

Usage (you will need to have ImageMagick installed)

  $ ./cvt.py --help

  $ ./cvt.py --dst=. --dpi=144 --quality=75 --length=8 <file> ...
  $ ./cvt.py --dst=. --dpi=300 --quality=90 --length=8 <file> ...
"""

import sys, os
from optparse import OptionParser

cmd_str = "convert -geometry %(size)d "\
          "-density %(density)s "\
          "-profile %(icc)s "\
          "-sharpen %(sharpen)s "\
          "-quality %(quality)d "\
          "%(in_file)s %(out_file)s"

def main(options, args):

    # Gather parameters for conversion arguments
    d = {}
    for name in ('length', 'dpi', 'icc', 'sharpen',
                 'quality'):
        d[name] = getattr(options, name)

    # calculate size in pixels of the longest dimension
    d['size'] = d['length'] * d['dpi']
    d['density'] = '%dx%d' % (d['dpi'], d['dpi'])

    dst_dir = options.dstdir.strip('/')

    # Convert each file on the command line
    for in_file in args:
        d['in_file'] = in_file

        path, filename = os.path.split(in_file)
        name, ext = os.path.splitext(filename)

        d['out_file'] = '%s/%s.%s' % (dst_dir, name, options.format)

        cmd = cmd_str % d
        print cmd

        if not options.dry_run:
            os.system(cmd)

if __name__ == '__main__':

    # Parse command line into options and arguments.
    usage = "usage: %prog [options] file [...]"
    optprs = OptionParser(usage=usage, version=('%%prog'))

    optprs.add_option("--debug", dest="debug", default=False,
                      action="store_true",
                      help="Enter the pdb debugger on main()")
    optprs.add_option("--dpi", dest="dpi", type="int", default=144,
                      help="Sepcify the DPI of the result (default 144)")
    optprs.add_option("--dry-run", dest="dry_run", default=False,
                      action="store_true",
                      help="Just show the commands we WOULD do")
    optprs.add_option("--dst", dest="dstdir", default='.',
                      help="Specify a destination directory for the results (default current directory)")
    optprs.add_option("--icc", dest="icc", default='sRGB.icm',
                      help="Supply an ICC/ICM profile for the dst files (default sRGB)")
    optprs.add_option("--format", dest="format", default="jpg",
                      help="Specify format of the result (jpg|tif|png); default jpg")
    optprs.add_option("--profile", dest="profile", action="store_true",
                      default=False,
                      help="Run the profiler on main()")
    optprs.add_option("--quality", dest="quality", type="int", default=90,
                      help="Specify the quality level of the (compressed) result (default 90)")
    optprs.add_option("--length", dest="length", type="int", default=8,
                      metavar="INCHES",
                      help="Dimension in INCHES of the longest side of downsampled image")
    optprs.add_option("--sharpen", dest="sharpen", default='0.6x1.0+0.65+0.0',
                      help="Specify sharpening parameters for the result image")

    (options, args) = optprs.parse_args(sys.argv[1:])

    # Are we debugging this?
    if options.debug:
        import pdb

        pdb.run('main(options, args)')

    # Are we profiling this?
    elif options.profile:
        import profile

        print "%s profile:" % sys.argv[0]
        profile.run('main(options, args)')

    else:
        main(options, args)

# END
