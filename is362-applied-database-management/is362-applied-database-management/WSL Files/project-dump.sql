-- MariaDB dump 10.19  Distrib 10.6.16-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	10.6.16-MariaDB-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `CustomerID` varchar(7) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Phone` varchar(12) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`CustomerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('CUST001','customerName1','email1@example.com','phone1','address1'),('CUST002','customerName2','email2@example.com','phone2','address2'),('CUST003','customerName3','email3@example.com','phone3','address3'),('CUST004','customerName4','email4@example.com','phone4','address4'),('CUST005','customerName5','email5@example.com','phone5','address5'),('CUST006','customerName6','email6@example.com','phone6','address6'),('CUST007','customerName7','email7@example.com','phone7','address7'),('CUST008','customerName8','email8@example.com','phone8','address8'),('CUST009','customerName9','email9@example.com','phone9','address9'),('CUST010','customerName10','email10@example.com','phone10','address10'),('CUST011','customerName11','email11@example.com','phone11','address11'),('CUST012','customerName12','email12@example.com','phone12','address12'),('CUST013','customerName13','email13@example.com','phone13','address13'),('CUST014','customerName14','email14@example.com','phone14','address14'),('CUST015','customerName15','email15@example.com','phone15','address15'),('CUST016','customerName16','email16@example.com','phone16','address16'),('CUST017','customerName17','email17@example.com','phone17','address17'),('CUST018','customerName18','email18@example.com','phone18','address18'),('CUST019','customerName19','email19@example.com','phone19','address19'),('CUST020','customerName20','email20@example.com','phone20','address20');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `DepartmentID` varchar(3) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `AisleStart` int(11) DEFAULT NULL,
  `AisleEnd` int(11) DEFAULT NULL,
  `RowStart` int(11) DEFAULT NULL,
  `RowEnd` int(11) DEFAULT NULL,
  PRIMARY KEY (`DepartmentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES ('BLD','Building Materials',7,8,1,99),('ELC','Electrical',5,6,1,99),('FLR','Floor',NULL,NULL,NULL,NULL),('GRD','Gardening & Outdoors',6,7,1,99),('HDW','Hardware',2,3,1,99),('MIX','Multiple Departments',100,999,1,9999),('MNG','Management',NULL,NULL,NULL,NULL),('PLM','Plumbing',4,5,1,99),('PNT','Paint',3,4,1,99),('REC','Recieving',NULL,NULL,NULL,NULL),('REG','Registers',0,1,1,25),('TLS','Tools',1,2,1,99);
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `EmployeeID` varchar(7) NOT NULL,
  `Name` char(25) DEFAULT NULL,
  `Position` varchar(30) DEFAULT NULL,
  `Phone` varchar(12) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `Wage` float DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('EMP01','EmployeeName1','Owner','EMPPhone1','Address1',NULL),('EMP02','EmployeeName2','Owner','EMPPhone2','Address1',NULL),('EMP03','EmployeeName3','Cashier','EMPPhone3','Address3',12),('EMP04','EmployeeName4','Associate','EMPPhone4','Address4',13),('EMP05','EmployeeName5','Manager','EMPPhone5','Address5',20),('EMP06','EmployeeName6','Cashier','EMPPhone6','Address6',12),('EMP07','EmployeeName7','Associate','EMPPhone7','Address7',13),('EMP08','EmployeeName8','Manager','EMPPhone8','Address8',20),('EMP09','EmployeeName9','Cashier','EMPPhone9','Address9',12),('EMP10','EmployeeName10','Associate','EMPPhone10','Address10',13),('EMP11','EmployeeName11','Manager','EMPPhone11','Address11',20),('EMP12','EmployeeName12','Cashier','EMPPhone12','Address12',12),('EMP13','EmployeeName13','Associate','EMPPhone13','Address13',13),('EMP14','EmployeeName14','Manager','EMPPhone14','Address14',20),('EMP15','EmployeeName15','Cashier','EMPPhone15','Address15',12),('EMP16','EmployeeName16','Associate','EMPPhone16','Address16',13),('EMP17','EmployeeName17','Manager','EMPPhone17','Address17',20),('EMP18','EmployeeName18','Cashier','EMPPhone18','Address18',12),('EMP19','EmployeeName19','Associate','EMPPhone19','Address19',13),('EMP20','EmployeeName20','Manager','EMPPhone20','Address20',14);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location` (
  `LocationID` varchar(7) NOT NULL,
  `Aisle` varchar(2) DEFAULT NULL,
  `Row` int(11) DEFAULT NULL,
  PRIMARY KEY (`LocationID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES ('A1R1','1',1),('A1R2','1',2),('A1R3','1',3),('A1R4','1',4),('A1R5','1',5),('A1R6','1',6),('A2R1','2',1),('A2R3','2',3),('A3R1','3',1),('A3R2','3',2),('A4R1','4',1),('A4R2','4',2),('A5R1','5',1),('A5R2','5',2),('A6R1','6',1),('A6R2','6',2),('A7R1','7',1),('A7R2','7',2),('A8R1','8',1),('A8R2','8',2);
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `ProductID` varchar(7) NOT NULL,
  `Location` varchar(7) DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Description` char(255) DEFAULT NULL,
  `Price` float NOT NULL,
  `Supply` varchar(7) DEFAULT NULL,
  PRIMARY KEY (`ProductID`),
  KEY `fk_Location_to_location` (`Location`),
  KEY `fk_Supply_to_supply` (`Supply`),
  CONSTRAINT `fk_Location_to_location` FOREIGN KEY (`Location`) REFERENCES `location` (`LocationID`),
  CONSTRAINT `fk_Supply_to_supply` FOREIGN KEY (`Supply`) REFERENCES `supply` (`SupplyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('PID0001','A1R1','Hammer','Used to smash things',30.99,'truck1'),('PID0002','A1R2','Screwdriver','Used to screw things',15.99,'truck2'),('PID0003','A1R3','Level','3ft level',20.99,'truck3'),('PID0004','A1R4','Drill','3/4 impact drill',120.99,'truck4'),('PID0005','A2R1','Nails','Carpenter nails',12.99,'truck5'),('PID0006','A2R3','Screws','Drywall screws',16.99,'truck6'),('PID0007','A3R1','Primer','Paint primer',30.99,'truck7'),('PID0008','A3R2','Paint','White paint',30.99,'truck8'),('PID0009','A4R1','SharkBite','1/2 to 1/4 adapter',14.99,'truck9'),('PID0010','A4R2','Fitting','10ft 1/4 copper roll',70.99,'truck10'),('PID0011','A5R1','FuseBox','8 breaker box',41.99,'truck11'),('PID0012','A5R2','Lightbult','1200 lumens',6.99,'truck12'),('PID0013','A6R1','Shovel','Wedge shovel',30.99,'truck13'),('PID0014','A6R2','Hose','20ft garden hose',35.99,'truck14'),('PID0015','A7R1','Concrete','Gravel concrete',15.99,'truck15'),('PID0016','A7R2','Ladder','10ft laddder',99,'truck16'),('PID0017','A8R1','Gum','Bubble tape',2.99,'truck17'),('PID0018','A8R2','Soda','Surge',1.99,'truck18'),('PID0019','A1R5','Saw','Wood saw',20.99,'truck19'),('PID0020','A1R6','Saw blade','3/4 16in saw blade',35.99,'truck20');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase`
--

DROP TABLE IF EXISTS `purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `purchase` (
  `PurchaseID` int(11) NOT NULL AUTO_INCREMENT,
  `CustomerID` varchar(7) DEFAULT NULL,
  `TransactionID` varchar(7) DEFAULT NULL,
  `ProductID` varchar(7) NOT NULL,
  `Quantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`PurchaseID`),
  KEY `fk_CustomerID_to_history` (`CustomerID`),
  KEY `fk_TransactionID_to_transaction` (`TransactionID`),
  KEY `fk_ProductID_to_product` (`ProductID`),
  CONSTRAINT `fk_ProductID_to_product` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ProductID`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase`
--

LOCK TABLES `purchase` WRITE;
/*!40000 ALTER TABLE `purchase` DISABLE KEYS */;
INSERT INTO `purchase` VALUES (21,'CUST001','TRN0001','PID0020',1),(22,'CUST002','TRN0002','PID0019',2),(23,'CUST003','TRN0003','PID0018',3),(24,'CUST004','TRN0004','PID0003',2),(25,'CUST005','TRN0005','PID0004',1),(26,'CUST006','TRN0006','PID0005',3),(27,'CUST007','TRN0007','PID0006',2),(28,'CUST008','TRN0008','PID0007',1),(29,'CUST009','TRN0009','PID0008',4),(30,'CUST010','TRN0010','PID0009',2),(31,'CUST011','TRN0011','PID0010',1),(32,'CUST012','TRN0012','PID0011',3),(33,'CUST013','TRN0013','PID0012',2),(34,'CUST014','TRN0014','PID0013',1),(35,'CUST015','TRN0015','PID0014',3),(36,'CUST016','TRN0016','PID0015',2),(37,'CUST017','TRN0017','PID0016',1),(38,'CUST018','TRN0018','PID0017',4),(39,'CUST019','TRN0019','PID0018',2),(40,'CUST020','TRN0020','PID0019',1);
/*!40000 ALTER TABLE `purchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supplier` (
  `SupplierID` varchar(7) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Phone` varchar(12) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `Details` char(255) DEFAULT NULL,
  PRIMARY KEY (`SupplierID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES ('S000','Vendor0','Phone1','Address1','Registers supplier'),('S001','Vendor1','Phone2','Address2','Tools supplier'),('S002','Vendor2','Phone3','Address3','Hardware retailer'),('S003','Vendor3','Phone4','Address4','Paint supplier'),('S004','Vendor4','Phone5','Address5','Plumbing supplier'),('S005','Vendor5','Phone6','Address6','Electric supplier'),('S006','Vendor6','Phone7','Address7','Garden supplier'),('S007','Vendor7','Phone8','Address8','Building Materials supplier'),('S008','Vendor8','Phone9','Address9','Mixed supplier');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supply`
--

DROP TABLE IF EXISTS `supply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supply` (
  `SupplyID` varchar(7) NOT NULL,
  `SupplierID` varchar(7) DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `RecievedDate` date DEFAULT NULL,
  PRIMARY KEY (`SupplyID`),
  KEY `fk_SupplierID_to_supplier` (`SupplierID`),
  CONSTRAINT `fk_SupplierID_to_supplier` FOREIGN KEY (`SupplierID`) REFERENCES `supplier` (`SupplierID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supply`
--

LOCK TABLES `supply` WRITE;
/*!40000 ALTER TABLE `supply` DISABLE KEYS */;
INSERT INTO `supply` VALUES ('truck1','S001',20,'2000-01-01'),('truck10','S001',20,'2000-01-02'),('truck11','S002',20,'2000-01-02'),('truck12','S003',20,'2000-01-02'),('truck13','S004',20,'2000-01-02'),('truck14','S005',20,'2000-01-02'),('truck15','S006',20,'2000-01-02'),('truck16','S007',20,'2000-01-02'),('truck17','S008',20,'2000-01-02'),('truck18','S002',20,'2000-01-02'),('truck19','S001',20,'2000-01-02'),('truck2','S002',20,'2000-01-01'),('truck20','S001',20,'2000-01-02'),('truck3','S003',20,'2000-01-01'),('truck4','S004',20,'2000-01-01'),('truck5','S005',20,'2000-01-01'),('truck6','S006',20,'2000-01-01'),('truck7','S007',20,'2000-01-01'),('truck8','S008',20,'2000-01-01'),('truck9','S002',20,'2000-01-01');
/*!40000 ALTER TABLE `supply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaction` (
  `TransactionID` varchar(7) NOT NULL,
  `Total` float DEFAULT NULL,
  `SalesPerson` varchar(7) DEFAULT NULL,
  `PurchaseDate` date NOT NULL,
  `PurchaseTime` datetime NOT NULL,
  PRIMARY KEY (`TransactionID`),
  KEY `fk_SalesPerson_to_employee` (`SalesPerson`),
  CONSTRAINT `fk_SalesPerson_to_employee` FOREIGN KEY (`SalesPerson`) REFERENCES `employee` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES ('TRN0001',50.99,'EMP01','2024-04-13','2024-04-13 09:30:00'),('TRN0002',35.75,'EMP02','2024-04-13','2024-04-13 10:15:00'),('TRN0003',120.5,'EMP03','2024-04-13','2024-04-13 11:00:00'),('TRN0004',25,'EMP04','2024-04-13','2024-04-13 11:45:00'),('TRN0005',75.25,'EMP05','2024-04-13','2024-04-13 12:30:00'),('TRN0006',90.1,'EMP06','2024-04-13','2024-04-13 13:15:00'),('TRN0007',60.75,'EMP07','2024-04-13','2024-04-13 14:00:00'),('TRN0008',42.99,'EMP08','2024-04-13','2024-04-13 14:45:00'),('TRN0009',110.25,'EMP09','2024-04-13','2024-04-13 15:30:00'),('TRN0010',70.5,'EMP10','2024-04-13','2024-04-13 16:15:00'),('TRN0011',85.3,'EMP11','2024-04-13','2024-04-13 17:00:00'),('TRN0012',95.25,'EMP12','2024-04-13','2024-04-13 17:45:00'),('TRN0013',130.75,'EMP13','2024-04-13','2024-04-13 18:30:00'),('TRN0014',55.99,'EMP14','2024-04-13','2024-04-13 19:15:00'),('TRN0015',40.25,'EMP15','2024-04-13','2024-04-13 20:00:00'),('TRN0016',88.1,'EMP16','2024-04-13','2024-04-13 20:45:00'),('TRN0017',65.75,'EMP17','2024-04-13','2024-04-13 21:30:00'),('TRN0018',75.99,'EMP18','2024-04-13','2024-04-13 22:15:00'),('TRN0019',95.25,'EMP19','2024-04-13','2024-04-13 23:00:00'),('TRN0020',120.5,'EMP20','2024-04-13','2024-04-13 23:45:00');
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works`
--

DROP TABLE IF EXISTS `works`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `works` (
  `DateTime` datetime NOT NULL,
  `DepartmentID` varchar(3) DEFAULT NULL,
  `Employee` varchar(7) DEFAULT NULL,
  PRIMARY KEY (`DateTime`),
  KEY `fk_DepartmentID_to_department` (`DepartmentID`),
  KEY `fk_works_to_employee` (`Employee`),
  CONSTRAINT `fk_DepartmentID_to_department` FOREIGN KEY (`DepartmentID`) REFERENCES `department` (`DepartmentID`),
  CONSTRAINT `fk_works_to_employee` FOREIGN KEY (`Employee`) REFERENCES `employee` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works`
--

LOCK TABLES `works` WRITE;
/*!40000 ALTER TABLE `works` DISABLE KEYS */;
INSERT INTO `works` VALUES ('2000-01-01 00:08:00','MNG','EMP01'),('2000-01-01 00:09:01','FLR','EMP04'),('2000-01-01 00:09:02','REG','EMP03'),('2000-01-02 00:08:00','MNG','EMP02'),('2000-01-02 00:09:01','FLR','EMP04'),('2000-01-02 00:09:02','REG','EMP03');
/*!40000 ALTER TABLE `works` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-22 18:44:12
