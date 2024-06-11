-- customers table
-- | id | name  |
-- | -- | ----- |
-- | 1  | Joe   |
-- | 2  | Henry |
-- | 3  | Sam   |
-- | 4  | Max   |

-- order table
-- | id | customerId |
-- | -- | ---------- |
-- | 1  | 3          |
-- | 2  | 1          |

-- 输出
-- | Customers |
-- | --------- |
-- | Henry     |
-- | Max       |

select customers.name as 'Customers'``
from customers
where customers.id not in
(
    select customerid from orders
);


SELECT name AS 'Customers'
FROM Customers
LEFT JOIN Orders ON Customers.Id = Orders.CustomerId
WHERE Orders.CustomerId IS NULL
