#!/usr/bin/env python3

# Created by: Navin Balekomebole
# Created on: Jan 30 2022
# This program gets input from the user
# and converts it into a proper address format.


# convert user input into proper format
def address_create(name, street_num, street_name,
                   city, province, postal_code, apt_num=""):
    name = name.upper()
    street_name = street_name.upper()
    city = city.upper()
    province = province.upper()
    postal_code = postal_code.upper()
    address = name + "\n" + apt_num + street_num + street_name
    address = address + "\n" + city + " " + province + " " + postal_code
    print("Your mailing address is:")
    print(address)


def main():
    # set apt_input
    apt_input = None
    # get inputs
    name_input = input("Enter your name: ")
    apt_answer = input("Do you live in an apartment? (Yes/No): ")
    if apt_answer.upper() == "Yes":
        apt_input = input("Enter your apartment number: ")
        apt_input = apt_input.upper() + "-"
    street_input = input("Enter your street number: ")
    street_name_input = input("Enter your street name: ")
    city_input = input("Enter your city: ")
    province_input = input("Enter your province as an abbreviation: ")
    postal_input = input("Enter your postal code: ")
    if apt_input is None:
        address_create(name_input, street_input, street_name_input,
                       city_input, province_input, postal_input)
    else:
        address_create(name_input, street_input, street_name_input,
                       city_input, province_input, postal_input, apt_input)


if __name__ == "__main__":
    main()
