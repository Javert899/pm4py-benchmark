import os
import requests
import gzip
import shutil
import tempfile
import pm4py
import time
import gc
import math
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.importer.csv import importer as csv_importer
from pm4py.objects.petri.importer import importer as petri_importer

LOG_MODEL_REPOSITORY_URL = "http://www.alessandroberti.it/"
A32F0N00_LOG = "a32f0n00.xes"
A32F0N00_NET = "a32f0n00.pnml"
BPIC2017_OFFER_LOG = "bpic2017.xes.gz"
ROADTRAFFIC_CSV_GZ = "roadtraffic.csv.gz"
DEBUG = True


def decompress(gzipped_file):
    """
    Decompress a gzipped file and returns location of the temp file created

    Parameters
    ----------
    gzipped_file
        Gzipped file

    Returns
    ----------
    decompressedPath
        Decompressed file path
    """
    extension = gzipped_file.split(".")[-1]
    fp = tempfile.NamedTemporaryFile(suffix=extension)
    fp.close()
    with gzip.open(gzipped_file, 'rb') as f_in:
        with open(fp.name, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return fp.name


if not os.path.exists(A32F0N00_LOG):
    print("downloading: " + A32F0N00_LOG)
    r = requests.get(LOG_MODEL_REPOSITORY_URL + A32F0N00_LOG)
    with open(A32F0N00_LOG, 'wb') as f:
        f.write(r.content)

if not os.path.exists(A32F0N00_NET):
    print("downloading: " + A32F0N00_NET)
    r = requests.get(LOG_MODEL_REPOSITORY_URL + A32F0N00_NET)
    with open(A32F0N00_NET, 'wb') as f:
        f.write(r.content)

if not os.path.exists(BPIC2017_OFFER_LOG):
    print("downloading: " + BPIC2017_OFFER_LOG)
    r = requests.get(LOG_MODEL_REPOSITORY_URL + BPIC2017_OFFER_LOG)
    with open(BPIC2017_OFFER_LOG, 'wb') as f:
        f.write(r.content)

if not os.path.exists(BPIC2017_OFFER_LOG):
    print("downloading: " + BPIC2017_OFFER_LOG)
    r = requests.get(LOG_MODEL_REPOSITORY_URL + BPIC2017_OFFER_LOG)
    with open(BPIC2017_OFFER_LOG, 'wb') as f:
        f.write(r.content)

if not os.path.exists(ROADTRAFFIC_CSV_GZ):
    print("downloading: " + ROADTRAFFIC_CSV_GZ)
    r = requests.get(LOG_MODEL_REPOSITORY_URL + ROADTRAFFIC_CSV_GZ)
    with open(ROADTRAFFIC_CSV_GZ, 'wb') as f:
        f.write(r.content)

a32f0n00_log = xes_importer.apply(A32F0N00_LOG)
a32f0n00_net, a32f0n00_im, a32f0n00_fm = petri_importer.apply(A32F0N00_NET)

T1 = [0.0, 1.0, 0.0]
T2 = [0.0, 1.0, 0.0]

if DEBUG:
    F = open("debug.csv", "w")
    F.write("T1;T2;T3;T4;T5;T6;T7;T8;T9;T10;T11;T12;T13;T14;T15;T16;T17;T18;T19;T20;T21;T22;T23;T24;T25\n")
    F.close()

# TEST 1: import bpic2017.xes.gz
t0 = time.time()
bpic2017_log = xes_importer.apply(A32F0N00_LOG)
t1 = time.time()
T1[0] = (t1 - t0)
T1[2] = math.ceil(T1[1] / (T1[0] + 0.00000001) * 1000.0)
bpic2017_log = None
gc.collect()
print("TEST 1 - Importing bpic2017.xes.gz - %.5f s (test score: %d)" % (T1[0], T1[2]))

