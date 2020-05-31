import os
import requests
import pm4py

LOG_MODEL_REPOSITORY_URL = "http://www.alessandroberti.it/"
A32F0N00_LOG = "a32f0n00.xes"
A32F0N00_NET = "a32f0n00.pnml"
BPIC2017_OFFER_LOG = "bpic2017.xes.gz"
ROADTRAFFIC_CSV_GZ = "roadtraffic.csv.gz"
DEBUG = True

if not os.path.exists(A32F0N00_LOG):
    print("downloading: "+A32F0N00_LOG)
    r = requests.get(LOG_MODEL_REPOSITORY_URL+A32F0N00_LOG)
    with open(A32F0N00_LOG, 'wb') as f:
        f.write(r.content)

if not os.path.exists(A32F0N00_NET):
    print("downloading: "+A32F0N00_NET)
    r = requests.get(LOG_MODEL_REPOSITORY_URL+A32F0N00_NET)
    with open(A32F0N00_NET, 'wb') as f:
        f.write(r.content)

if not os.path.exists(BPIC2017_OFFER_LOG):
    print("downloading: "+BPIC2017_OFFER_LOG)
    r = requests.get(LOG_MODEL_REPOSITORY_URL+BPIC2017_OFFER_LOG)
    with open(BPIC2017_OFFER_LOG, 'wb') as f:
        f.write(r.content)

if not os.path.exists(BPIC2017_OFFER_LOG):
    print("downloading: "+BPIC2017_OFFER_LOG)
    r = requests.get(LOG_MODEL_REPOSITORY_URL+BPIC2017_OFFER_LOG)
    with open(BPIC2017_OFFER_LOG, 'wb') as f:
        f.write(r.content)

if not os.path.exists(ROADTRAFFIC_CSV_GZ):
    print("downloading: "+ROADTRAFFIC_CSV_GZ)
    r = requests.get(LOG_MODEL_REPOSITORY_URL+ROADTRAFFIC_CSV_GZ)
    with open(ROADTRAFFIC_CSV_GZ, 'wb') as f:
        f.write(r.content)

if DEBUG:
    F = open("debug.csv", "w")
    F.write("T1;T2;T3;T4;T5;T6;T7;T8;T9;T10;T11;T12;T13;T14;T15;T16;T17;T18;T19;T20;T21;T22;T23;T24;T25\n")
    F.close()

