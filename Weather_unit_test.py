from weather import Weather


def main():
    """Unit test that test the Weather class """

    weather1 = Weather((32,60),"partly cloudy",.25,("NW",5))
    weather1 = weather1.make_description()






if __name__ == "__main__":
    main()