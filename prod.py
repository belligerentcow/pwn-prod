from pwn import *
import argparse

def argParser():
  parser = argparse.ArgumentParser(description='Prod at systems and find patterns.')
  remote_or_local = parser.add_mutually_exclusive_group(required=True)
  remote_or_local.add_argument("-r", "--remote", nargs=2)
  remote_or_local.add_argument("-l", "--local", nargs=1)
  parser.add_argument("-c", "--characterlist", nargs=1, default="./strings/common-chars.txt")
  return parser.parse_args()

def connectToTarget(cli_args):
  """
  Consumes arguments, decides whether to connect to remote or local target and returns target object
  """
  target = None
  if not cli_args.remote:
    target = process(cli_args.local)
  else:
    target = remote(cli_args.remote[0], cli_args.remote[1])
  return target    

def pwnIt(payload, target):
  """
  Consumes payload from runCharList() and target returned from connectToTarget(), returns target output
  """
  target.recv()
  target.sendline(payload)
  response = target.recv()
  return response

def runCharList(wordlist):
  """
  Attempts every line in the wordlist given by cli arg '-c'
  """
  with open(wordlist, 'r') as all_chars:
    for a_char in all_chars:
      print("Trying: "+ a_char + " " + str(pwnIt(a_char, connectToTarget(argParser()))))

runCharList(argParser().characterlist)