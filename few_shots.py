few_shots = [
    {'Question' : "How many units are available for a commercial property , which is vaastu compliant and has marble flooring type ?",
     'SQLQuery' : "SELECT SUM(pd.Units_Available) FROM property_details pd JOIN property_amenities pa ON pd.ID = pa.ID WHERE pa.Vaastu_Compliant = '1' AND pd.Flooring_Type LIKE '%Marble%';",
     'SQLResult': "Result of the SQL query",
     'Answer' : "12531"},
    {'Question': "what is the average price of a property in hyderabad which is semi-furnished and has a modular kitchen?",
     'SQLQuery':" SELECT AVG(Price) FROM property_details pd JOIN property_amenities pa on pd.ID=pa.ID WHERE pa.Modular_Kitchen='1' AND furnished_Type='Semi-Furnished';",
     'SQLResult': "Result of the SQL query",
     'Answer': "31631560.797376752"},
    {'Question': "how many properties are available with internet facility and booking amount less than 1 lakh" ,
     'SQLQuery' : "SELECT count(*) FROM property_details pd JOIN property_amenities pa on pd.ID=pa.ID WHERE pd.Booking_Amount<100000 AND pa.Internet_WiFi_Connectivity='1';",
     'SQLResult': "Result of the SQL query",
     'Answer': "853"},
     {'Question': "get me the name of the property in hyderabad with the lowest price and what is the price" ,
     'SQLQuery' : "SELECT Project_Name, Price FROM property_details WHERE City = 'Hyderabad' AND Price IS NOT NULL AND Project_Name IS NOT NULL AND Project_Name != 'NA' ORDER BY Price ASC LIMIT 1;",
     'SQLResult': "Result of the SQL query",
     'Answer': "[('Orchid Residency', 8000000.0)]"},
     {'Question': "get me the name of the property in mumbai with the lowest booking price " ,
     'SQLQuery' : "SELECT Project_Name, Booking_Amount FROM property_details WHERE City = 'Mumbai'AND Booking_Amount IS NOT NULL AND Project_Name IS NOT NULL AND Project_Name != 'NA' ORDER BY Booking_Amount ASC LIMIT 1;",
     'SQLResult': "Result of the SQL query",
     'Answer': "[('Vastu Labh', 0.0)]"}
     

]