import ssl
import sys
import requests

baseurl = "http://127.0.0.1:6543/"

if len(sys.argv) != 2:
    print("Usage: python readygosetup.py <envname>")
    sys.exit(1)

envname = sys.argv[1]

if not envname:
    print("Error: Both arguments are required.")
    print("Usage: python readygosetup.py <envname>")
    sys.exit(1)

print("╔════════════╣ ReadyGoSetup ╠═════════════╗\n"
      "║                                         ║\n"
      "║    An App For Auto-Setting Up Envs!     ║\n"
      "║         Made Proudly in India,          ║\n"
      "║        To Be Used By The World.         ║\n"
      "║    https://bit.ly/PrattayElecsGithub    ║\n"
      "║                                         ║\n"
      "╚═════════════════════════════════════════╝\n")

print("|+- Trying To Connect To URL...")

urlcode = requests.get(baseurl + envname, verify=False)

try:
    urlcode = requests.get(baseurl + envname)
    print("|+- Successfully Connected To URL!")
    pass
except:
    print("|+- Something Has Gone Wrong! Exiting...")
    exit(1)
print("|+- Trying To Get Env Code...")
try:
    envcode = urlcode.text
except:
    print("|+- Something Has Gone Wrong! Exiting...")
print("|+- Successfully Got Env Code!")
print("|+- Switching Over To Code Output...\n")
print("════════════ CODE OUTPUT ════════════")
exec(envcode)
