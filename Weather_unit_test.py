from weather import Weather


def main():
    """Unit test that test the Weather class """
    # passes data through the weather class and creates a instance 
    weather1 = Weather((32,60),"partly cloudy",.25,("NW",5))
    # this test that all the data types can be correclty imputed in to the class
    # next we call upon the method make_desctption 
    weather1 = weather1.make_description()
    # this method should print out the data with the appropriate formatting






if __name__ == "__main__":
    main()