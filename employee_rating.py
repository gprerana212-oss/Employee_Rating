import sys
def calculate_rating(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg <= 89:
        return "A"
    elif 65 <= avg <= 79:
        return "B"
    elif 50 <= avg <= 64:
        return "C"
    elif 40 <= avg <= 49:
        return "D"
    else:
        return "F"

def main():
    if len(sys.argv) == 7:
        name = sys.argv[1]
        department = sys.argv[2]
        experience = sys.argv[3]
        s1 = int(sys.argv[4])
        s2 = int(sys.argv[5])
        s3 = int(sys.argv[6])
    else:
        name = "Anjum"
        department = "IT"
        experience = "3"
        s1, s2, s3 = 85, 90, 80

    avg = (s1 + s2 + s3) / 3
    rating = calculate_rating(avg)

    print("Employee Name:", name)
    print("Department:", department)
    print("Experience:", experience, "years")
    print("Scores:", s1, s2, s3)
    print("Average Score:", avg)
    print("Performance Rating:", rating)

if __name__ == "__main__":
    main()

