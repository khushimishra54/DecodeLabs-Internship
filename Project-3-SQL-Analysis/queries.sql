-- Total Orders
SELECT COUNT(*) AS Total_Orders
FROM orders;

-- Total Revenue
SELECT SUM(CAST(TotalPrice AS REAL)) AS Total_Revenue
FROM orders;

-- Average Order Value
SELECT AVG(CAST(TotalPrice AS REAL)) AS Average_Order_Value
FROM orders;

-- Orders by Status
SELECT OrderStatus, COUNT(*) AS Total_Orders
FROM orders
GROUP BY OrderStatus;

-- Revenue by Payment Method
SELECT PaymentMethod,
       SUM(CAST(TotalPrice AS REAL)) AS Revenue
FROM orders
GROUP BY PaymentMethod;

-- Top 5 Highest Value Orders
SELECT OrderID,
       CustomerID,
       TotalPrice
FROM orders
ORDER BY CAST(TotalPrice AS REAL) DESC
LIMIT 5;

-- Shipped Orders
SELECT *
FROM orders
WHERE OrderStatus = 'Shipped';