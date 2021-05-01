# The main code for this bypass was made by @msemple1111 and @michaelshumshum, full congrats to them.
# ALL THE OTHER CODE IN THIS REPOSITORY WAS WRITTEN BY ME.
# I just cleaned this up a bit, and fixed a bug to get it in working order.
# This joins a user with a name generator bypass, but doesen't have any functional control.

from session_connect import kahoot, error

verify = True

pin = "1499599"
name = "Bruh"

if pin == "":
  pin = input("Enter the Kahoot Pin: ")
if name == "":
  name = input("Enter your desired name: ")

print("\n[Status] Connecting...")

send = kahoot(pin, name)
send.verify = verify
send.connect()

print("[Success] Connected!\n")
