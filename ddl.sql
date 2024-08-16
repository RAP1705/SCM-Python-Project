CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    product_price NUMERIC(10, 2) NOT NULL,
    product_stock INTEGER NOT NULL
);


INSERT INTO products (product_name, product_price, product_stock) VALUES
('iPad', 329.99, 100),
('MacBook', 999.99, 30),
('iPhone', 699.99, 50),
('AirPods', 159.99, 200),
('Apple Watch', 399.99, 80);


select * from products;


ALTER TABLE products
ADD COLUMN barcode VARCHAR(255);


UPDATE products SET barcode = '1234567890123' WHERE product_name = 'iPad';
UPDATE products SET barcode = '2345678901234' WHERE product_name = 'MacBook';
UPDATE products SET barcode = '3456789012345' WHERE product_name = 'iPhone';
UPDATE products SET barcode = '4567890123456' WHERE product_name = 'AirPods';
UPDATE products SET barcode = '5678901234567' WHERE product_name = 'Apple Watch';


INSERT INTO products (product_name, product_price, product_stock, barcode) VALUES
('NVIDIA', 1000.99, 2, 'X001GNLTSF');