import mysql.connector

class RestaurantDatabase:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="Restaurant_reservations"
        )
        self.cursor = self.connection.cursor()

    def add_reservation (self, customer_name, reservation_time, number_of_guests, special_requests):
        self.cursor.execute("SELECT customerId FROM Customers WHERE customerName = %s", (customer_name,))
        result = self.cursor.fetchone()
        
        if result:
            customer_id = result[0]
        else:
            self.cursor.execute("INSERT INTO Customers (customerName) VALUES (%s)", (customer_name,))
            self.connection.commit()
            customer_id = self.cursor.lastrowid

        self.cursor.execute("""
            INSERT INTO Reservations (customerId, reservationTime, numberOfGuests, specialRequests)
            VALUES (%s, %s, %s, %s)
        """, (customer_id, reservation_time, number_of_guests, special_requests))
        self.connection.commit()
        print(f"Reservation added for {customer_name}")

    def add_special_request(self, reservation_id, requests):
        self.cursor.execute("""
            UPDATE Reservations
            SET specialRequests = %s
            WHERE reservationId = %s
        """, (requests, reservation_id))
        self.connection.commit()
        print(f"Special request updated for reservation ID {reservation_id}")

    def find_reservations(self, customer_id):
        self.cursor.execute("SELECT * FROM Reservations WHERE customerId = %s", (customer_id,))
        result = self.cursor.fetchall()
        print("Reservations:")
        for row in result:
            print(row)

    def getAllReservations(self):
        try:
            self.cursor.execute("SELECT * FROM Reservations")
            reservations = self.cursor.fetchall()
            return reservations
        except mysql.connector.Error as err:
            print("Error: {}".format(err))

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    db = RestaurantDatabase()
    db.add_reservation("John Doe", "2024-06-01 19:00:00", 4, "Window seat")
    db.add_special_request(1, "Vegetarian meal")
    db.find_reservations(1)
    db.close_connection()

    
