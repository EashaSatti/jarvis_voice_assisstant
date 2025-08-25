import multiprocessing
import subprocess
import time
import re

def run_adb_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}")
    return result.returncode, result.stdout, result.stderr

def setup_device():
    print("Setting up device connection...")
    # Check if device is already connected via TCP/IP
    returncode, stdout, stderr = run_adb_command("adb devices")
    ip = "192.168.0.108"  # Fallback IP
    if f"{ip}:5037" in stdout:
        print(f"Device already connected at {ip}:5037")
        return ip
    # Run device.bat to set up connection
    returncode, stdout, stderr = run_adb_command("P:\\jarvis\\jarvis\\device.bat")
    if returncode != 0:
        print("Error: device.bat failed to set up the connection.")
        return None
    # Extract IP from device.bat output
    ip_match = re.search(r"Connected successfully to (\d+\.\d+\.\d+\.\d+):5037", stdout)
    if not ip_match:
        print("Error: Could not find IP address in device.bat output.")
        return None
    ip = ip_match.group(1)
    print(f"Device connected at {ip}:5037")
    return ip

def startJarvis():
    print("Process 1 is running (Jarvis).")
    from main import start
    start()

def listenHotword():
    print("Process 2 is running (Hotword).")
    from engine.features import hotword
    hotword()

if __name__ == '__main__':
    # Set up the device connection
    ip = setup_device()
    if not ip:
        print("Failed to set up device connection. Exiting...")
        exit(1)

    # Verify the connection
    print("Verifying device connection...")
    returncode, stdout, stderr = run_adb_command("adb devices")
    if f"{ip}:5037" not in stdout:
        print(f"Error: Device {ip}:5037 not found in adb devices.")
        exit(1)

    # Start both processes
    p1 = multiprocessing.Process(target=startJarvis)
    p2 = multiprocessing.Process(target=listenHotword)
    p1.start()
    time.sleep(3)  # Increased delay to ensure stability
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("System stopped")