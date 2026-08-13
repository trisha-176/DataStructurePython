CREATE TABLE SUPPLIERS
(
    Supplier_No NUMBER(5) PRIMARY KEY,
    Sname VARCHAR2(25) NOT NULL,
    Saddress VARCHAR2(100) NOT NULL,
    Scity VARCHAR2(25)
);

CREATE TABLE COMPUTER_ITEMS
(
    Item_No NUMBER(5) PRIMARY KEY,
    Supplier_No NUMBER(5) NOT NULL,
    Item_Name VARCHAR2(30) NOT NULL,
    Quantity NUMBER(5)
);

ALTER TABLE COMPUTER_ITEMS
ADD CONSTRAINT FK_SUPPLIER
FOREIGN KEY (Supplier_No)
REFERENCES SUPPLIERS(Supplier_No);

INSERT INTO SUPPLIERS VALUES (101,'Microtech','MG Road','Bangalore');
INSERT INTO SUPPLIERS VALUES (102,'Cats','Anna Nagar','Chennai');
INSERT INTO SUPPLIERS VALUES (103,'Electrotech','Andheri','Mumbai');
INSERT INTO SUPPLIERS VALUES (104,'TechZone','Banjara Hills','Hyderabad');
INSERT INTO SUPPLIERS VALUES (105,'ByteWorld','Sector 18','Delhi');

INSERT INTO COMPUTER_ITEMS VALUES (1,101,'Monitor',15);
INSERT INTO COMPUTER_ITEMS VALUES (2,102,'Keyboard',20);
INSERT INTO COMPUTER_ITEMS VALUES (3,103,'Mouse',8);
INSERT INTO COMPUTER_ITEMS VALUES (4,101,'Printer',12);
INSERT INTO COMPUTER_ITEMS VALUES (5,103,'Keyboard',18);

COMMIT;

SELECT C.Item_No,
       C.Item_Name,
       C.Quantity,
       S.Supplier_No,
       S.Sname,
       S.Saddress,
       S.Scity
FROM COMPUTER_ITEMS C
JOIN SUPPLIERS S
ON C.Supplier_No = S.Supplier_No;

SELECT S.Sname
FROM SUPPLIERS S
JOIN COMPUTER_ITEMS C
ON S.Supplier_No = C.Supplier_No
WHERE C.Item_Name = 'Keyboard';

SELECT C.Item_Name
FROM COMPUTER_ITEMS C
JOIN SUPPLIERS S
ON C.Supplier_No = S.Supplier_No
WHERE S.Sname = 'Microtech';

SELECT C.Item_Name
FROM COMPUTER_ITEMS C
JOIN SUPPLIERS S
ON C.Supplier_No = S.Supplier_No
WHERE S.Sname IN ('Cats','Electrotech');

SELECT S.Sname,
       C.Item_Name,
       C.Quantity
FROM SUPPLIERS S
JOIN COMPUTER_ITEMS C
ON S.Supplier_No = C.Supplier_No
WHERE C.Quantity > 10;