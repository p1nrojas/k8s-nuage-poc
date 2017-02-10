import argparse
parser = argparse.ArgumentParser()
parser.add_argument('cspuser', type=str)
parser.add_argument('passwd', type=str)
args =  parser.parse_args()
print "\"vsd user is %s\"" % args.cspuser
