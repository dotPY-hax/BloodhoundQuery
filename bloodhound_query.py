import argparse

import ui


parser = argparse.ArgumentParser()
parser.add_argument("-f", help="Path to BloodHound.zip", default="./BloodHound.zip")
parser.add_argument("-i", help="Opens interactive mode which lets you parse the data by hand.", action='store_true', default=False)
args = parser.parse_args()

bloodhound_path = args.f

if args.i:
    ui.interactive_mode_ui(bloodhound_path)
else:
    ui.predefined_query_ui(bloodhound_path)


