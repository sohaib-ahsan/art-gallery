Insert into user
Values
('Muji', '12345678','Artist'),
('hashirscam', '12345678','Artist'),
('samama', '12345678','Artist'),
('sohaib', '12345678','Artist'),
('hussain', '12345678','Artist'),
('umerkhan', '12345678','Artist'),
('lemonmaxbar', '12345678','Artist'),
('hina', '12345678','Customer'),
('Ma9ahil', '12345678','Customer'),
('shalina', '12345678','Customer'),
('Abdullah', '12345678','Customer'),
('Rouhan', '12345678','Customer'),
('MHBA', '12345678','Customer'),
('Habib', '12345678','Customer'),
('Azan', '12345678','Customer');

Insert into categories
Values
(1, 'Love'),
(2, 'Illusion'),
(3, 'Oil Painting'),
(4, 'Nature'),
(5, 'Abstract');

Insert into artist
Values
(1, 'Mujtaba Shafqat', 'mujtabashafqat0@gmail.com', '03392929929', 'Pop Art', 'Muji'),
(2, 'Hashir Ahmad', 'hashirscam@gmail.com', '03192943929', 'Pop Art', 'hashirscam'),
(3, 'Samama Farooq', 'samilionaire@gmail.com', '0313429929', 'Pop Art', 'samama'),
(4, 'Sohaib Ahsan', 'sohaibahsan@gmail.com', '03192345929', 'Abstract', 'sohaib'),
(5, 'Syed Hussain', 'hussainhammad@gmail.com', '03345929929', 'Abstract', 'hussain'),
(6, 'Umer Khan', 'umerkhan@gmail.com', '03192934539', 'Abstract', 'umerkhan'),
(7, 'Faizyab Ali', 'lemonmaxbar@gmail.com', '03193253929', 'Abstract', 'lemonmaxbar');


Insert into customer
Values
(1, 'Abdullah Aleem', 'abdullah@gmail.com','03189219382','Islamabad','Abdullah'),
(2, 'Rouhan Faisal', 'rouhan@gmail.com','03189219382','Islamabad','Rouhan'),
(3, 'Hassan Bin Adeel', 'mhba@gmail.com','03189219382','Karachi','MHBA'),
(4, 'Habibullah Khan', 'Habibullah@gmail.com','03189219382','Islamabad','Habib'),
(5, 'Azan Siddiq', 'azan@gmail.com','03189219382','Lahore', 'Azan'),
(6, 'Hina Naeem', 'hinanaeem0@gmail.com', '0319223432', 'Islamabad','hina'),
(7, 'Manahil Ahmad', 'manahilahmad@gmail.com', '03193434929', 'Lahore','Ma9ahil'),
(8, 'Shalina Riaz', 'shalinariaz@gmail.com', '03198745349', 'Islamabad','shalina');

Insert into artwork
Values
(1, 'Starry Night', '2002','1500', 3, 1, '20'),
(2, 'Darkness', '2005','1500', 3, 2, '22'),
(3, 'Peacock', '2006','1500', 1, 3, '24'),
(4, 'Winds', '2007','5000', 1, 4, '34'),
(5, 'Light', '2003','1100', 1, 5, '20'),
(6, 'Extreme', '2002','1200',1, 2, '30'),
(7, 'Sofa', '2003','1300', 3, 3, '50'),
(8, 'Illusions', '2002','5000', 2, 3, '30'),
(9, 'Dancing in the wind', '2100','1500', 2, 2, '10'),
(10, 'Hello world', '2002','1500', 2, 2, '22'),
(11, 'Stars', '2002','1500', 6, 1, '24'),
(12, 'My books', '2002','1000', 6, 5, '24'),
(13, 'Daffodils', '2002','4000', 6, 4, '25'),
(14, 'Mist', '2002','10000', 3, 4, '21'),
(15, 'Us Together', '2002','5100', 5, 2, '20'),
(16, 'Starry Night', '2002','1500', 5,1, '22'),
(17, 'Wolfs', '2002','1500', 3, 4, '22');


Insert into sales
Values
(1,3,'12-02-12'),
(2,2,'12-02-12'),
(3,2,'12-02-12'),
(4,2,'12-02-12'),
(5,2,'12-02-12'),
(6,1,'12-02-12'),
(7,1,'12-02-12'),
(8,1,'12-02-12'),
(9,5,'12-02-12'),
(10,5,'12-02-12'),
(11,5,'12-02-12');