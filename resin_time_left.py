#import
from datetime import datetime as dt, timedelta as td
#setting
minPerResin=8
ls={12:[],24:[]}
thres=[20,40,60,160]
#main
def process():
        currentResin=int(input("Current resin: "))
        approxResinTimeLeft=int(input("Approx minute/s left for current resin: "))
        for counter in thres: create_resin_datetime(currentResin, approxResinTimeLeft, counter)
        print("\n[24-hr format] Results:")
        for i in ls[24]: print(i)
        bool12=str(input("\nDo you want to view results in 12-hr format too? (y/n): ")).lower()
        if(bool12 == 'y' or bool12 == 'yes'):
                print("\n[12-hr format] Results:")
                for i in ls[12]: print(i)
        input("\nPress Enter to continue...")
#function
def create_resin_datetime(currentResin, approxResinTimeLeft, resin_goal):
        if currentResin < resin_goal:
                required_resin = resin_goal - currentResin
                minutes_for_required_resin = required_resin * minPerResin - approxResinTimeLeft
                datetime_for_required_resin = dt.now() + td(minutes=minutes_for_required_resin)
                date=datetime_for_required_resin.strftime("%d/%h/%Y")
                formatted_12datetime_for_required_resin = datetime_for_required_resin.strftime("%I:%M%p")
                formatted_24datetime_for_required_resin = datetime_for_required_resin.strftime("%H:%M")
                ls[12].append(str(resin_goal)+" resin at "+formatted_12datetime_for_required_resin+", "+date)
                ls[24].append(str(resin_goal)+" resin at "+formatted_24datetime_for_required_resin+", "+date)

if __name__ == '__main__':
        process()
