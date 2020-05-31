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
from pm4py.objects.log.adapters.pandas import csv_import_adapter
from pm4py.objects.petri.importer import importer as petri_importer
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay
from pm4py.algo.conformance.alignments import algorithm as alignments
from pm4py.simulation.playout import simulator as playout


LOG_MODEL_REPOSITORY_URL = "http://www.alessandroberti.it/"
A32F0N00_LOG = "a32f0n00.xes"
A32F0N00_NET = "a32f0n00.pnml"
BPIC2017_OFFER_LOG = "bpic2017.xes.gz"
ROADTRAFFIC_CSV_GZ = "rogz"

DEBUG = True
ENABLE_TESTS = False


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
T3 = [0.0, 1.0, 0.0]
T4 = [0.0, 1.0, 0.0]
T5 = [0.0, 1.0, 0.0]

if DEBUG:
    F = open("debug.csv", "w")
    F.write("T1;T2;T3;T4;T5;T6;T7;T8;T9;T10;T11;T12;T13;T14;T15;T16;T17;T18;T19;T20;T21;T22;T23;T24;T25\n")
    F.close()

print("\nPM4Py-Benchmark version (PM4Py version: %s)\n\n" % (pm4py.__version__))

if ENABLE_TESTS:
    # TEST 1: import bpic2017.xes.gz
    t0 = time.time()
    xes_importer.apply(A32F0N00_LOG)
    t1 = time.time()
    T1[0] = (t1 - t0)
    T1[2] = math.ceil(T1[1] / (T1[0] + 0.00000001) * 1000.0)
    gc.collect()
    print("TEST 1 - Importing bpic2017.xes.gz - %.5f s (test score: %d)" % (T1[0], T1[2]))

if ENABLE_TESTS:
    # TEST 2: import roadtraffic.csv.gz
    t0 = time.time()
    roadtraffic_df = csv_import_adapter.import_dataframe_from_path(decompress(ROADTRAFFIC_CSV_GZ))
    t1 = time.time()
    T2[0] = (t1 - t0)
    T2[2] = math.ceil(T2[1] / (T2[0] + 0.00000001) * 1000.0)
    print("TEST 2 - Importing roadtraffic.csv.gz - %.5f s (test score: %d)" % (T2[0], T2[2]))

if ENABLE_TESTS:
    # TEST 3: perform token-based replay between A32F0N00 log and model
    t0 = time.time()
    token_replay.apply(a32f0n00_log, a32f0n00_net, a32f0n00_im, a32f0n00_fm)
    t1 = time.time()
    T3[0] = (t1 - t0)
    T3[2] = math.ceil(T3[1] / (T3[0] + 0.00000001) * 1000.0)
    print("TEST 3 - Applying token-based replay between A32F0N00 log and model - %.5f s (test score: %d)" % (
    T3[0], T3[2]))

if ENABLE_TESTS:
    # TEST 4: perform alignments between A32F0N00 log and model
    t0 = time.time()
    alignments.apply(a32f0n00_log, a32f0n00_net, a32f0n00_im, a32f0n00_fm,
                     variant=alignments.Variants.VERSION_DIJKSTRA_NO_HEURISTICS)
    t1 = time.time()
    T4[0] = (t1 - t0)
    T4[2] = math.ceil(T4[1] / (T4[0] + 0.00000001) * 1000.0)
    print("TEST 4 - Applying alignments between A32F0N00 log and model - %.5f s (test score: %d)" % (T4[0], T4[2]))

if ENABLE_TESTS:
    # TEST 5: perform playout of the a32f0n00 Petri net
    t0 = time.time()
    playout.apply(a32f0n00_net, a32f0n00_im, a32f0n00_fm)
    t1 = time.time()
    T5[0] = (t1 - t0)
    T5[2] = math.ceil(T5[1] / (T5[0] + 0.00000001) * 1000.0)
    print("TEST 5 - Doing playout - %.5f s (test score: %d)" % (T5[0], T5[2]))
