import sys
if ("-h" in sys.argv) or ("--help" in sys.argv):
  print "The minimal bag-file dumper. http://wiki.ros.org/Bags/Format/2.0"
  print "cat file.bag | python bag_to_xml.py >file.xml"
  sys.exit(0)

import struct

def read_initial_line(h):
  s = h.readline()
  s = s.strip()
  assert "#ROSBAG V2.0" == s

def loop_over_records(h):
  while True:
    s_header_len = h.read(4)
    if not s_header_len:
      break
    header_len = struct.unpack_from("<I", s_header_len)[0]
    s_header = h.read(header_len)
    s_data_len = h.read(4)
    data_len = struct.unpack_from("<I", s_data_len)[0]
    s_data = h.read(data_len)
    print header_len, data_len

read_initial_line(sys.stdin)
loop_over_records(sys.stdin)
