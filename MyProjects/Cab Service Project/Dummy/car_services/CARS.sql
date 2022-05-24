-- ques-1 number of drivers without covid_Certification

SELECT COUNT(*) AS NUM_OF_DRIVERS FROM DRIVER WHERE COVID_VACCINATION='NO';


-- ques-2rank the companies in order of the number of cabs used by them
SELECT C.CUST_NAME,COUNT(C.CUST_ID) AS NUM_OF_BOOKINGS ,DENSE_RANK() OVER (ORDER BY COUNT(C.CUST_ID) DESC ) AS RANK1 FROM
BOOKING B JOIN CUSTOMER C
ON B.CUST_ID=C.CUST_ID
WHERE B.TRANSACTION_ID IS NOT NULL
GROUP BY C.CUST_NAME;

SELECT COUNT(*),CUST_ID FROM BOOKING WHERE TRANSACTION_ID IS NOT NULL GROUP BY CUST_ID;
SELECT COUNT(*),CUST_ID FROM BOOKING WHERE TRANSACTION_ID IS NULL GROUP BY CUST_ID;

-- ques -3 find driver which driver has driven most
SELECT * FROM
(SELECT D.DRIVER_NAME,D.DRIVER_ID,COUNT(D.DRIVER_ID),DENSE_RANK() OVER ( ORDER BY COUNT(D.DRIVER_ID) DESC ) AS D_RANK FROM 
CABS C JOIN DRIVER D
ON C.DRIVER_ID=D.DRIVER_ID
JOIN BOOKING B
ON B.CAB_ID=C.CAB_ID
GROUP BY D.DRIVER_ID)A
WHERE D_RANK=1;

SELECT * FROM BOOKING;

-- ques-4 prove that there are 3 types of cabs with min count of 2 each in each area of north bangalore
SELECT A.AREA_ID,COUNT(*),CAR_TYPE_ID FROM REGION R JOIN AREA A ON 
R.REGION_ID=A.REGION_ID
JOIN CABS C ON
C.AREA_ID=A.AREA_ID
WHERE R.REGION_NAME='North_Bengaluru'
GROUP BY A.AREA_ID,CAR_TYPE_ID ;



SELECT * FROM DRIVER;#5
-- ques-5 num of drivers are given work by future cabs in entire bangalore
SELECT COUNT(*) AS NUM_OF_DRIVERS FROM DRIVER ;

SELECT COUNT(*) AS NUM_OF_DRIVERS FROM DRIVER WHERE DRIVING_LICENSE='YES' AND COVID_VACCINATION='YES';


-- ques-6 total no of pick-up points in each region of bangalore
select region_id,count(*) as NUM_OF_PICKUP_POINTS from area group by region_id;

select r.region_name,count(*) as NUM_OF_PICKUP_POINTS from area a join region r
on a.REGION_ID=r.REGION_ID group by a.region_id;

