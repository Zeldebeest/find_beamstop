# coding: utf-8
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def image_pickle_to_numpy(pck_file):
  from libtbx import easy_pickle as ep
  img_d = ep.load(pck_file)
  return img_d['DATA'].as_numpy_array()

def clip_at_percentile(im, percentile=99.9):
  t_val = np.percentile(im, percentile)
  return im.clip(0, t_val)

def get_fig_axes(n_imgs, n_per_row=4):
    fig, axes = plt.subplots(n_imgs // n_per_row + 1, n_per_row,
                             figsize=(20, 40)) # Add one so we ceiling divide.
    return fig, axes

def region_based_seg(im, low_thresh=15, high_thresh=35):
  from skimage.filter import sobel
  from skimage import morphology
  import scipy.ndimage as ndimage

  elevation_map = sobel(im)
  markers = np.zeros_like(im)
  markers[im < low_thresh] = 1
  markers[im > high_thresh] = 2
  segmentation = morphology.watershed(elevation_map, markers)
  segmentation = ndimage.binary_fill_holes(segmentation - 1)
  return segmentation



def plot_segmentation(im, seg, ax=None):

  # Make a figure and some axes if not provided
  if not ax:
    _, ax = plt.subplots()

  ax.imshow(im, cmap=plt.cm.gray, interpolation='nearest')
  ax.contour(seg, [0.5], linewidths=1.2, colors='y')
  ax.axis('off')


