CREATE DATABASE art_gallery;
USE art_gallery;

CREATE TABLE `art_gallery`.`artist` (
  `Artist_id` INT NOT NULL,
  `Name` VARCHAR(20) NULL,
  `Email` VARCHAR(40) NULL,
  `Phone` VARCHAR(13) NULL,
  `Style_of_art` VARCHAR(20) NULL,
  `user_name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`Artist_id`));
  
CREATE TABLE `art_gallery`.`artwork` (
  `Art_id` INT NOT NULL,
  `Title` VARCHAR(20) NULL,
  `Year_made` YEAR(4) NULL,
  `Price` DECIMAL(10, 2) NULL,
  `Artist_id` INT not NULL,
  `Category_id` INT not NULL,
  `Likes` INT,
  PRIMARY KEY (`Art_id`));
  
CREATE TABLE `art_gallery`.`categories` (
  `Category_id` INT NOT NULL,
  `Name` VARCHAR(20) NULL,
  PRIMARY KEY (`Category_id`));
  
CREATE TABLE `art_gallery`.`sales` (
  `Art_id` INT NOT NULL,
  `Customer_id` INT not NULL,
  `Date` DATE NULL,
  PRIMARY KEY (`Art_id`));
  
CREATE TABLE `art_gallery`.`customer` (
  `Customer_id` INT NOT NULL,
  `Name` VARCHAR(20) NULL,
  `Email` VARCHAR(40) NULL,
  `Phone` VARCHAR(13) NULL,
  `Address` VARCHAR(30) NULL,
  `user_name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`Customer_id`));
  
CREATE TABLE `art_gallery`.`user` (
  `user_name` VARCHAR(20) NOT NULL,
  `password` VARCHAR(20) NOT NULL,
  `type` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`user_name`));

ALTER TABLE artwork
ADD FOREIGN KEY (Artist_id) REFERENCES artist(Artist_id)
on delete cascade
on update cascade;

ALTER TABLE artwork
ADD FOREIGN KEY (Category_id) REFERENCES categories(Category_id)
on delete cascade
on update cascade;

ALTER TABLE sales
ADD FOREIGN KEY (Art_id) REFERENCES artwork(Art_id)
on delete cascade
on update cascade;

ALTER TABLE sales
ADD FOREIGN KEY (Customer_id) REFERENCES customer(Customer_id)
on delete cascade
on update cascade;

ALTER TABLE artist
ADD FOREIGN KEY (user_name) REFERENCES user(user_name)
on delete cascade
on update cascade;

ALTER TABLE customer
ADD FOREIGN KEY (user_name) REFERENCES user(user_name)
on delete cascade
on update cascade;
