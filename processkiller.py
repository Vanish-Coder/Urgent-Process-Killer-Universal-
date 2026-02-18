import os
print("FIRST RESPONDER PROCESS KILLER ACTIVTED. don't mind of errors.")

while True:
    user_input = input("Enter the name of the process EXACTLY WITH EXTENSIONS to kill please:")

    os.system(f"pkill {user_input}")
    os.system(f"killall {user_input}")
    os.system(f"killall -9 {user_input}")
    os.system(f"kill -9 {user_input}")
    os.system(f"kill -9 $(pgrep {user_input})")
    os.system(f"taskkill /F /IM {user_input}")
    os.system(f"taskkill /F /PID {user_input}")
    os.system(f"taskkill /F /T /IM {user_input}")
    os.system(f"taskkill /F /T /PID {user_input}")
    os.system(f"taskkill /F /IM {user_input} /T")
    os.system(f"taskkill /F /PID {user_input} /T")
    os.system(f"taskkill /F /IM {user_input} /T")
    os.system(f"Stop-Process -Name {user_input} -Force")
    os.system(f"Stop-Process -Id {user_input} -Force")
    os.system(f"Stop-Process -Name {user_input} -Force")
    os.system(f"Stop-Process -Id {user_input} -Force")
    os.system(f"Stop-Process -Name {user_input} -Force")
    os.system(f"Stop-Process -Id {user_input} -Force")

    print(f"Attempted to kill process(s): {user_input}")








