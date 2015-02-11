from libtbx import easy_pickle as ep
from scitbx_array_family_flex_ext import int as scint
import sys

def update_img_pickle(img_pkl, beamstop_pkl, out_name=None):
  if not out_name:
    out_name = img_pkl

  beamstop = ep.load(beamstop_pkl)
  beamstop = scint(beamstop)

  img_d = ep.load(img_pkl)
  img_d["ACTIVE_AREAS"] = beamstop
  ep.dump(out_name, img_d)



if __name__ == '__main__':
  if len(sys.argv) != 3:
    print "takes only 2 arguments"
    sys.exit()

  img_pkl = sys.argv[1]
  beamstop_pkl = sys.argv[2]
  update_img_pickle(img_pkl, beamstop_pkl, out_name="updated-" + img_pkl)
