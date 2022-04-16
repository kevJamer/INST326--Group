from weather import Day


def main():
    """Unit test that test the Weather class """
    # passes data through the weather class and creates a instance 
    day_test = Day(1,1,2000)
    # this test that all the data types can be correclty imputed in to the class
    # next we call upon the method make_desctption 
    print(day_test.date)
    print(day_test.Month)
    print(day_test.Year)
    # this method should print out the data with the appropriate formatting






if __name__ == "__main__":
    main()