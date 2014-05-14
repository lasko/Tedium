#    Tedium - A cisco configuration generator that utilizes templates
#             to generate configuration files.
#    Copyright (C) 2014 Brandon M. Height <bmheight at gmail dot com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
import argparse
import sys
from switch.model import Switch

if __name__ == '__main__':
    type_list = ['switch','ap','router']
    parser = argparse.ArgumentParser()
    parser.add_argument('--template', dest='template_path', action='store', help='The path to the template file for this device', required=True)
    parser.add_argument('--type', dest='type_value', action='store', help='Device type: switch, ap, router', required=True)
    args = parser.parse_args()

    if args.type_value == 'switch':
      switch = Switch()
    elif args.type_value == 'ap':
      sys.exit()
    elif args.type_value == 'router':
      sys.exit()
