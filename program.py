#!/usr/bin/env python3

# Created by: Igor
# Created on: Nov 2021
# this is program


def adress_1(
    name,
    question,
    number_of_house_from_user,
    name_of_street,
    city,
    province,
    pc,
    number_of_flat_from_user=None,
):

    # this is function

    apt_street_num = ""
    if question == "y":
        apt_street_num = "{0}-{1}".format(
            number_of_flat_from_user, number_of_house_from_user
        )
    else:
        apt_street_num = number_of_house_from_user

    adress = "\n{0}\n{1} {2}\n{3} {4}  {5}".format(
        name, apt_street_num, name_of_street, city, province, pc
    )
    adress = adress.upper()

    return adress


def main():
    # This is main function
    
    print("This program formats your address to a mailing address.")
    # input
    name = input("Enter your full name: ")

    while True:
        question = input("Do you live in an apartment? (y/n): ")
        if question == "y":
            integer1 = input("Enter your apartment number: ")
            break
        elif question == "n":
            integer1 = None
            break
        else:
            print("Invalid input")

    integer2 = input("Enter your street number:")
    name_of_street = input("Enter your street name AND type(Main St, Express Pkwy...): ")
    city = input("Enter your city: ")
    province = input("Enter your province (as an abreviation, ex: ON, BC...):")
    pc = input("Enter your postal code (123 456): ")

    try:
        number_of_house_from_user = int(integer2)
        if integer1 != None:
            number_of_flat_from_user = int(integer1)

        adress = adress_1(
            name,
            question,
            number_of_house_from_user,
            name_of_street,
            city,
            province,
            pc,
            number_of_flat_from_user,
        )

        print(adress)
    except Exception:
        print("\nInvalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
