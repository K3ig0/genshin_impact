#import
from datetime import datetime as dt, timedelta as td

#setting
minPerResin=8
ls={12:[], 24:[]}
thres=[20,40,60,80,120,160]

#main
def process():
        try:
                resinNow = int(input("Current resin [n]: ")) #33
                if 0 <= resinNow <= 159:
                        approxResinTimeLeft = (160 - resinNow) * 8
                        print(f"\nFully replenish: around {str(approxResinTimeLeft/60).split('.')[0]} hours\n")
                        create_resin_datetime(resinNow)
                        print("\nResults:")
                        for i in ls[12]: print(i)
                        input("\nPress Enter to continue...")
                else:
                        raise ValueError
        except ValueError:
                print("\n***\nPlease try again. Format = n (1 for example).\n***\n")
                process()

def intro():
        print("==> Good day to you, Traveler.")
        print("==> Please acquire the total time needed to fully replenish your resins.")
        print("==> Note: You can get it from Map function.\n")
        print(10*"-"+"\nResin List\n"+10*"-")
        print("20 resin = 1x Leyline or 1x Domain")
        print("40 resin = 1x condensed resin or 1x World Boss")
        print("60 resin = 1x Dvalin or 1x Boreas or 1x Childe\n")

def create_resin_datetime(resinNow):
        #currentResin = 160-approxResinTimeLeft/8
        currentResin = resinNow
        for goal in thres:
                if goal >= currentResin:
                        requiredResin = goal - currentResin
                        datetime_for_required_resin = dt.now() + td(minutes=requiredResin*8)
                        date=datetime_for_required_resin.strftime("%d/%h/%Y")
                        formatted_12datetime_for_required_resin = datetime_for_required_resin.strftime("%I:%M%p")
                        formatted_24datetime_for_required_resin = datetime_for_required_resin.strftime("%H:%M:%S")
                        ls[12].append("==> "+str(goal)+" resin at "+formatted_12datetime_for_required_resin+", "+date)
                        ls[24].append("==> "+str(goal)+" resin at "+formatted_24datetime_for_required_resin+", "+date)

if __name__ == '__main__':
        intro()
        process()
