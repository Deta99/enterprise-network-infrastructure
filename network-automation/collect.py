import logging
import os
from datetime import datetime

from dotenv import load_dotenv
from netmiko import ConnectHandler

from devices import devices


# --------------------------------------------------
# Configuration
# --------------------------------------------------

load_dotenv()

username = os.getenv("NET_USERNAME")
password = os.getenv("NET_PASSWORD")

DRY_RUN = True

commands = [
    "show ip interface brief",
    "show ip route",
    "show version",
]


# --------------------------------------------------
# Directories
# --------------------------------------------------

os.makedirs("logs", exist_ok=True)
os.makedirs("reports", exist_ok=True)


# --------------------------------------------------
# Logging
# --------------------------------------------------

logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# Automation counters
# --------------------------------------------------

successful_devices = []
failed_devices = []


# --------------------------------------------------
# Start automation
# --------------------------------------------------

logger.info("Automation run started")

print("=" * 60)
print("NETWORK AUTOMATION")
print("=" * 60)
print(f"Started: {datetime.now()}")
print(f"Dry Run: {DRY_RUN}")
print("=" * 60)


# --------------------------------------------------
# Process devices
# --------------------------------------------------

for device in devices:

    name = device["name"]
    host = device["host"]

    print(f"\nDevice: {name}")
    print(f"IP: {host}")

    logger.info(f"Processing device: {name} ({host})")

    # --------------------------------------------------
    # Dry-run mode
    # --------------------------------------------------

    if DRY_RUN:

        print("DRY RUN — no connection made")

        logger.info(f"DRY RUN enabled for {name}")

        for command in commands:

            print(f"Would run: {command}")

            logger.info(
                f"{name} - Would run: {command}"
            )

        successful_devices.append(name)

        continue


    # --------------------------------------------------
    # Real connection
    # --------------------------------------------------

    connection = None

    try:

        logger.info(f"Connecting to {name}")

        connection = ConnectHandler(
            device_type=device["device_type"],
            host=host,
            username=username,
            password=password,
        )

        logger.info(f"Connected to {name}")

        print("Connected successfully")

        report = []

        # --------------------------------------------------
        # Execute commands
        # --------------------------------------------------

        for command in commands:

            print(f"Running: {command}")

            logger.info(
                f"{name} - Running: {command}"
            )

            output = connection.send_command(command)

            report.append(
                f"\n{'=' * 60}\n"
                f"{command}\n"
                f"{'=' * 60}\n"
                f"{output}\n"
            )


        # --------------------------------------------------
        # Save report
        # --------------------------------------------------

        report_file = f"reports/{name}.txt"

        with open(report_file, "w") as file:

            file.write(
                f"Device: {name}\n"
                f"IP: {host}\n"
                f"Collected: {datetime.now()}\n"
            )

            file.write("".join(report))


        print(f"Report saved: {report_file}")

        logger.info(
            f"{name} report saved successfully"
        )

        successful_devices.append(name)


    # --------------------------------------------------
    # Error handling
    # --------------------------------------------------

    except Exception as error:

        print(f"FAILED: {name}")
        print(f"Reason: {error}")

        logger.error(
            f"{name} failed: {error}"
        )

        failed_devices.append(name)


    # --------------------------------------------------
    # Disconnect
    # --------------------------------------------------

    finally:

        if connection:

            connection.disconnect()

            logger.info(
                f"Disconnected from {name}"
            )


# --------------------------------------------------
# Final summary
# --------------------------------------------------

logger.info("Automation run finished")

print("\n")
print("=" * 60)
print("AUTOMATION SUMMARY")
print("=" * 60)

print(f"Total devices : {len(devices)}")
print(f"Successful    : {len(successful_devices)}")
print(f"Failed        : {len(failed_devices)}")


if successful_devices:

    print("\nSuccessful devices:")

    for device in successful_devices:

        print(f"  [OK] {device}")


if failed_devices:

    print("\nFailed devices:")

    for device in failed_devices:

        print(f"  [FAILED] {device}")


print("\nAutomation finished.")
print("=" * 60)
