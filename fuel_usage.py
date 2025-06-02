def miles_per_galon(end, start, gallons):
    mpg = (end-start)/gallons
    return mpg

def lp100k_from_mpg(mpg):
    lp100k = 235.215/mpg
    return lp100k

def main():
    start = int(input("Enter the first odomoter reading (miles): "))
    end = int(input("Enter the second odomoter reading (miles)"))
    gallons = float(input("Enter tha amount of fule used(gallons)"))

    print(f"{miles_per_galon(end, start, gallons):.1f} miles per gallon")
    print(f"{lp100k_from_mpg(miles_per_galon(end,start,gallons)):.2f} liters per 100 kilometers")

main()
