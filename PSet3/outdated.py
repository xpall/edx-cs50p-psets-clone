months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def main():
    date_converter("Date: ")

def date_converter(prompt):
    date = ""
    while True:
        try:
            date = str(input(prompt)).strip()
            date2 = date
            try:
                int(date2[0])
            except:
                if "/" in date2 or "," not in date2:
                    continue
            date = date.replace("/"," ").replace("-"," ").replace(",","").split()
            mm, dd, yyyy = date[0], date[1], date[2]
            if mm in months:
                mm = int(months.index(mm)) + 1
            if int(mm) < 0 or int(mm) > 12 or int(dd) < 1 or int(dd) > 31:
                continue
            else:
                pass
            mm, dd, yyyy = (str(mm)).zfill(2), (str(dd)).zfill(2), str(yyyy)
            print(f"{yyyy}-{mm}-{dd}")
        except IndexError:
            pass
        except ValueError:
            pass
        else:
            break

main()