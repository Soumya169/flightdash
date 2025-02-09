import mysql.connector

class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='indigo'
            )
            self.mycursor = self.conn.cursor()
            print('Connection Established')
        except:
            print('Connection Error')
    def fetch_city_name(self):
        city = []
        self.mycursor.execute("""
        SELECT DISTINCT(Destination) FROM indigo.flights_cleaned
        UNION
        SELECT DISTINCT(Source) FROM indigo.flights_cleaned
        """)
        data =self.mycursor.fetchall()
        for item in data:
           city.append(item[0])
        return city
    def fetch_all_flights(self,source,destination):

        self.mycursor.execute("""
        SELECT Airline,Route,Dep_Time,Duration,Price from indigo.flights_cleaned
        WHERE Source='{}' AND Destination='{}'
        
        """.format(source,destination))

        data=self.mycursor.fetchall()
        return data


    def fetch_airline_freq(self):

        airline=[]
        frequency =[]

        self.mycursor.execute("""
        SELECT Airline,COUNT(*) FROM indigo.flights_cleaned
        GROUP BY Airline
        """)

        data =self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
        return airline,frequency
    def busy_air_port(self):
        city = []
        frequency = []
        self.mycursor.execute("""
        SELECT Source,COUNT(*) FROM (SELECT Source FROM indigo.flights_cleaned
                              UNION ALL
                              SELECT Destination FROM indigo.flights_cleaned) t
                              
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
        """)
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])
        return city, frequency

    def dailyfreq(self):
        date = []
        frequency = []
        self.mycursor.execute("""
        SELECT Date_of_Journey,COUNT(*) FROM indigo.flights_cleaned
        GROUP BY Date_of_Journey
        """)
        data = self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
            frequency.append(item[1])
        return date, frequency

    def avg_price(self):
        month = []
        price = []
        self.mycursor.execute("""
        SELECT 
    SUBSTRING(Date_of_Journey, 6, 2) AS Month, 
    AVG(Price) AS avg_price
    FROM indigo.flights_cleaned 
    GROUP BY Month
    ORDER BY Month;
        """)
        data = self.mycursor.fetchall()
        for item in data:
            month.append(item[0])
            price.append(item[1])
        return month, price





