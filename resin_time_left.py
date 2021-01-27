# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import sys

MINUTES_PER_RESIN = 8

def process():
	current_resin = int(input("Enter your current resin: "))
	print_resin_datetime(current_resin, 20)
	print_resin_datetime(current_resin, 40)
	print_resin_datetime(current_resin, 60)
	print_resin_datetime(current_resin, 160)
	raw_input("\nPress Enter to continue...")

def print_resin_datetime(current_resin, resin_goal):
	if current_resin < resin_goal:
		required_resin = resin_goal - current_resin
		minutes_for_required_resin = required_resin * MINUTES_PER_RESIN
		datetime_for_required_resin = datetime.now() + timedelta(minutes=minutes_for_required_resin)
		formatted_datetime_for_required_resin = datetime_for_required_resin.strftime("%H:%M:%S")
		print "==> " + str(resin_goal) + " resin at", formatted_datetime_for_required_resin

if __name__ == '__main__':
    process()