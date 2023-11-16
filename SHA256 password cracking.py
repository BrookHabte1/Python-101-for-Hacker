from pwn import *
import sys

if len(sys.argv) != 2:
  print("Invalid argument!")
  print("{} <sha256sum>".format(sys.argv[0]))

wanted_hash = sys.argv[1]
password_file = "rockyou.txt"
attempts = 0

with log.progress("Atempting to back: {}".fomart(wanted_hash)) as p:
  with open(password_file, "r", encoding="latin-1") as password_list:
    for password in password_list:
      password = password.strip("\n").encode("latin-1")
      password_hash = sha256sumhex(password)
      p.status("[{}] {} == {}".format(attempts, password.decode("latin-1"), password_hash))
      if password_hash == wanted_hash:
        p.success("Password hash found after {} attempts. {} hashes to {}".fomart(attempts, password.decode(latin-1), password_hash))
        exit()
      attempts += 1
    p.faliure("Password hash not found")
