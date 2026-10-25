from cnf import AIRCRAFT_NAME, flight_rules
from ecam_core import boot_check

def main():
    status = boot_check(AIRCRAFT_NAME, flight_rules)
    print(f"Статус ECAM: [{status}]")

if __name__ == "__main__":
    main()
