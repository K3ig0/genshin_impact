#import
from datetime import datetime as dt, timedelta as td

#setting
minPerResin=8
ls={12:[], 24:[]}
thres=[20,40,60,160]

#main
def process():
        try:
                hour, minute = input("Fully replenished [hh mm]: ").split(" ")
                timelist = {"hr":hour, "min":minute}
                for k, v in timelist.items(): timelist[k] = int(v)
                if 0 <= int(minute) <= 59:
                        approxResinTimeLeft = (timelist["hr"]*60)+timelist["min"]
                        create_resin_datetime(approxResinTimeLeft)
                        print("\nResults:")
                        for i in ls[24]: print(i)
                        input("\nPress Enter to continue...")
                else:
                        raise ValueError
        except ValueError:
                print("\n***\nPlease try again. Format = hh mm (12 59 for example).\n***\n")
                process()

def intro():
        print("==> Good day to you, Traveler.")
        print("==> Please acquire the total time needed to fully replenish your resins.")
        print("==> Note: You can get it from Map function.\n")
        print(10*"-"+"\nResin List\n"+10*"-")
        print("20 resin = 1x Leyline or 1x Domain")
        print("40 resin = 1x condensed resin or 1x World Boss")
        print("60 resin = 1x Dvalin or 1x Boreas or 1x Childe\n")

def create_resin_datetime(approxResinTimeLeft):
        currentResin = 160-approxResinTimeLeft/8
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
