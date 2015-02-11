from libtbx import easy_pickle as ep
import sys

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print "takes only 1 argumenr"
    sys.exit()
  pck_file = sys.argv[1]
  new_name = "numpy-" + pck_file
  img_d = ep.load(pck_file)
  img_data = img_d['DATA'].as_numpy_array()
  ep.dump(new_name, img_data)
