DROP TABLE IF EXISTS craft_items;

CREATE TABLE craft_items
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    item_name TEXT NOT NULL,
    price INT NOT NULL
);