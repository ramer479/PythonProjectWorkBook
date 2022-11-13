
def get_bill_split(bill, people, tip):
    total = ((100 + tip) * bill)/100
    print(total)
    bill_per_person  = total/people
    print(bill_per_person)
    return  bill_per_person


if __name__ == "__main__":
    total_bill = float(input("What is the total Bill: $"))
    num_person = int(input("How many people are there: "))
    tip_percent = float(input("What is the tip percentage you'd like to give: "))
    get_bill_split(total_bill,num_person,tip_percent)

