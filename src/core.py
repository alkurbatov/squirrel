# This file is a part of Squirrel project
#
# Copyright (C) 2014, Alexander Kurbatov <sir.alkurbatov@yandex.ru>
#
# Squirrel is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Squirrel is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys, os, os.path

from datetime import datetime

from zipfile import ZipFile
from zipfile import ZIP_DEFLATED

def busy(path):
    try:
         with open(path, "a+") as f:
            return False

    except IOError:
        return True

def remove(path):
    try:
        print >> sys.stdout, "Removing %s..." % path
        os.unlink(path)

    except OSError, e:
        print >> sys.stderr, "Failed to remove %s" % path
        print >> sys.stderr, repr(e)

def explore(path):
    l = []

    for f in os.listdir(path):
        if os.path.islink(f) or os.path.isdir(f):
            continue

        if os.path.splitext(f)[1] in [".zip", ".tar", ".bz2", ".gz", ".exe"]:
            print >> sys.stdout, "Ignoring %s , unsupported file extension" % f
            continue

        if busy(f):
            print >> sys.stdout, "Cant access %s , file is busy or inaccessible" % f
            continue

        l.append(f)

    return l

def compress(path, dry_run):
    os.chdir(path)

    l = explore(path)
    if not l:
        print >> sys.stdout, "Nothing to do"
        return

    t = datetime.now()
    n = t.strftime("%Y%m%d-%H%M%S") + ".zip"

    with ZipFile(n, 'w') as z:
        for f in l:
            print >> sys.stdout, "Compressing %s..." % f
            z.write(filename = f, compress_type = ZIP_DEFLATED)

            if not dry_run:
                remove(f)

    print >> sys.stdout, "Archive %s was created successfully" % n

