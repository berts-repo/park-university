-- MySQL dump 10.16  Distrib 10.2.13-MariaDB, for Win32 (AMD64)
--
-- Host: localhost    Database: forAssign06
-- ------------------------------------------------------
-- Server version	10.2.13-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `ClientID` varchar(7) NOT NULL,
  `Name` text DEFAULT NULL,
  `LegalAddress` text DEFAULT NULL,
  `Phone` text DEFAULT NULL,
  PRIMARY KEY (`ClientID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES ('145696S','Sarah Silverston','PO Box 4622 Delaware 19707','555-555-0008'),('156836P','Joy Behar','PO Box 687 Delaware 19706','555-555-0007'),('278544C','Chris Rock','PO Box 354 Delaware 19703','555-555-0002'),('394204C','Conan Brian','PO Box 34344 Delaware 19707','555-555-0009'),('472507P','Charles Chaplin','PO Box 9587 Delaware 19707','555-555-0010'),('736533Q','Jay Leno','PO Box 216 Delaware 19702','555-555-0004'),('765256P','Eddie Murphee','PO Box 4287 Delaware 19703','555-555-0003'),('842471P','Whopie Goldberg','PO Box 884 Delaware 19706','555-555-0006'),('865263C','Wanda Sykes','PO Box 56944 Delaware 19706','555-555-0005'),('933256Q','Jerry Seinfeld','PO Box 12221 Delaware 19702','555-555-0001');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract`
--

DROP TABLE IF EXISTS `contract`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contract` (
  `ContractNo` varchar(7) NOT NULL,
  `ClientID` varchar(7) DEFAULT NULL,
  `IsLongTerm` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ContractNo`),
  KEY `FK_Contract_to_Client` (`ClientID`),
  CONSTRAINT `FK_Contract_to_Client` FOREIGN KEY (`ClientID`) REFERENCES `client` (`ClientID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract`
--

LOCK TABLES `contract` WRITE;
/*!40000 ALTER TABLE `contract` DISABLE KEYS */;
INSERT INTO `contract` VALUES ('CO0010','933256Q',0),('CO0011','278544C',1),('CO0012','765256P',0),('CO0013','736533Q',1),('CO0014','865263C',1),('CO0015','842471P',0),('CO0016','156836P',1),('CO0017','145696S',0),('CO0018','394204C',1),('CO0019','472507P',0);
/*!40000 ALTER TABLE `contract` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `driver`
--

DROP TABLE IF EXISTS `driver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `driver` (
  `DocumentID` varchar(7) NOT NULL,
  `FirstName` text DEFAULT NULL,
  `Initials` text DEFAULT NULL,
  `LastName` text DEFAULT NULL,
  `BasicSalary` float DEFAULT NULL,
  `CommissionPerTrip` float DEFAULT NULL,
  PRIMARY KEY (`DocumentID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `driver`
--

LOCK TABLES `driver` WRITE;
/*!40000 ALTER TABLE `driver` DISABLE KEYS */;
INSERT INTO `driver` VALUES ('145696S','Enrico','M','Caruso',120000,1.5),('156836P','Anna','D','Netrebko',120000,2),('278544C','Luis','A','Alva',110000,1),('394204C','Renee','H','Fleming',120000,1.8),('736533Q','Andrea','C','Boccelli',120000,1.3),('765256P','Kiri','T','Kanawa',120000,2),('787923C','Luciano','J','Pavarotti',120000,1),('842471P','Placido','S','Domingo',120000,1),('865263C','Maria','A','De los Angeles',120000,1.5),('933256Q','Maria','F','Callas',130000,1.5);
/*!40000 ALTER TABLE `driver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `longtermcontract`
--

DROP TABLE IF EXISTS `longtermcontract`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `longtermcontract` (
  `ContractNo` varchar(7) NOT NULL,
  `PricePerMile` float DEFAULT NULL,
  `InsurancePerPound` float DEFAULT NULL,
  `DateSigned` datetime DEFAULT NULL,
  PRIMARY KEY (`ContractNo`),
  CONSTRAINT `FK_LongTermContract_to_Contract` FOREIGN KEY (`ContractNo`) REFERENCES `contract` (`ContractNo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `longtermcontract`
--

LOCK TABLES `longtermcontract` WRITE;
/*!40000 ALTER TABLE `longtermcontract` DISABLE KEYS */;
INSERT INTO `longtermcontract` VALUES ('CO0011',5,2,'2017-05-10 11:30:00'),('CO0013',5.5,2,'2017-04-24 14:23:00'),('CO0014',7,2.2,'2017-05-30 09:25:00'),('CO0016',6.5,1.8,'2017-03-29 13:45:00'),('CO0018',4.5,2.5,'2017-04-20 15:36:00');
/*!40000 ALTER TABLE `longtermcontract` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shorttermcontract`
--

DROP TABLE IF EXISTS `shorttermcontract`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shorttermcontract` (
  `ContractNo` varchar(7) NOT NULL,
  `Origin` text DEFAULT NULL,
  `Destination` text DEFAULT NULL,
  `Price` float DEFAULT NULL,
  `InsuranceValue` float DEFAULT NULL,
  `DateSigned` datetime DEFAULT NULL,
  `VehicleAssigned` varchar(5) DEFAULT NULL,
  `DriverAssigned` varchar(7) DEFAULT NULL,
  `DeliveryStamp` datetime DEFAULT NULL,
  PRIMARY KEY (`ContractNo`),
  KEY `FK_ShortTermContract_to_Vehicle` (`VehicleAssigned`),
  KEY `FK_ShortTermContract_to_Driver` (`DriverAssigned`),
  CONSTRAINT `FK_ShortTermContract_to_Contract` FOREIGN KEY (`ContractNo`) REFERENCES `contract` (`ContractNo`),
  CONSTRAINT `FK_ShortTermContract_to_Driver` FOREIGN KEY (`DriverAssigned`) REFERENCES `driver` (`DocumentID`),
  CONSTRAINT `FK_ShortTermContract_to_Vehicle` FOREIGN KEY (`VehicleAssigned`) REFERENCES `vehicle` (`NumberPlate`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shorttermcontract`
--

LOCK TABLES `shorttermcontract` WRITE;
/*!40000 ALTER TABLE `shorttermcontract` DISABLE KEYS */;
INSERT INTO `shorttermcontract` VALUES ('CO0010','Boston, Massachusets','Jackson, Mississippi',3000,10000,'2017-07-06 14:30:00','GA744','787923C','2017-07-16 11:05:00'),('CO0012','Austin, Texas','Memphis, Tennessee',1000,13000,'2017-07-07 09:30:00','AB931','933256Q','2017-07-07 16:18:00'),('CO0015','Los Angeles, California','Santa Fe, New Mexico',2000,25000,'2017-07-08 10:20:00','AC872','278544C','2017-07-09 17:20:00'),('CO0017','Seattle, Washington','Portland, Oregon',1500,18000,'2017-07-09 10:45:00','AD464','765256P','2017-07-11 12:45:00'),('CO0019','New Orleans, Louisiana','Las Vegas, Nevada',5000,25000,'2017-07-10 16:23:00','FA748','736533Q','2017-07-13 14:12:00');
/*!40000 ALTER TABLE `shorttermcontract` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trip`
--

DROP TABLE IF EXISTS `trip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trip` (
  `TripNo` int(11) NOT NULL AUTO_INCREMENT,
  `ContractNo` varchar(7) DEFAULT NULL,
  `Origin` text DEFAULT NULL,
  `Destination` text DEFAULT NULL,
  `Distance` float DEFAULT NULL,
  `Weight` float DEFAULT NULL,
  `DepartureDate` datetime DEFAULT NULL,
  `VehicleAssigned` varchar(5) DEFAULT NULL,
  `DriverAssigned` varchar(7) DEFAULT NULL,
  `DeliveryStamp` datetime DEFAULT NULL,
  PRIMARY KEY (`TripNo`),
  KEY `FK_Trip_to_LongTermContract` (`ContractNo`),
  KEY `FK_Trip_to_Vehicle` (`VehicleAssigned`),
  KEY `FK_Trip_to_Driver` (`DriverAssigned`),
  CONSTRAINT `FK_Trip_to_Driver` FOREIGN KEY (`DriverAssigned`) REFERENCES `driver` (`DocumentID`),
  CONSTRAINT `FK_Trip_to_LongTermContract` FOREIGN KEY (`ContractNo`) REFERENCES `longtermcontract` (`ContractNo`),
  CONSTRAINT `FK_Trip_to_Vehicle` FOREIGN KEY (`VehicleAssigned`) REFERENCES `vehicle` (`NumberPlate`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trip`
--

LOCK TABLES `trip` WRITE;
/*!40000 ALTER TABLE `trip` DISABLE KEYS */;
INSERT INTO `trip` VALUES (1,'CO0011','Chicago, Illinois','New York, New York',790,2000,'2017-06-16 08:10:00','AE653','787923C','2017-06-17 13:17:00'),(2,'CO0013','Saint Agustine, Florida','Montogomery, Alabama',405,3500,'2017-06-17 08:25:00','AF742','933256Q','2017-06-18 15:52:00'),(3,'CO0014','Los Angeles, California','El Paso, Texas',802,2500,'2017-06-18 09:03:00','CA871','278544C','2017-06-20 12:30:00'),(4,'CO0011','Chicago, Illinois','New York, New York',790,2000,'2017-06-27 08:13:00','AE653','787923C','2017-06-28 14:31:00'),(5,'CO0013','Saint Agustine, Florida','Montogomery, Alabama',405,3500,'2017-06-28 08:17:00','AF742','933256Q','2017-06-30 18:27:00'),(6,'CO0014','Los Angeles, California','El Paso, Texas',802,2500,'2017-06-29 09:04:00','CA871','278544C','2017-07-01 19:24:00'),(7,'CO0011','Chicago, Illinois','New York, New York',790,2000,'2017-05-16 08:13:00','AE653','865263C','2017-05-18 15:43:00'),(8,'CO0013','Saint Agustine, Florida','Montogomery, Alabama',405,3500,'2017-05-17 09:11:00','AF742','842471P','2017-05-18 14:31:00'),(9,'CO0014','Los Angeles, California','El Paso, Texas',802,2500,'2017-05-18 10:01:00','CA871','156836P','2017-05-20 11:21:00'),(10,'CO0016','Franklin, Kentucky','Providence, Rhode Island',1060,1200,'2017-05-19 07:58:00','DA466','145696S','2017-05-21 09:48:00'),(11,'CO0018','Bismarck, North Dakota','Omaha, Nebraska',610,1400,'2017-05-20 09:47:00','EA657','394204C','2017-05-22 15:17:00'),(12,'CO0011','Chicago, Illinois','New York, New York',790,2000,'2017-04-16 08:27:00','AE653','865263C','2017-04-18 16:33:00'),(13,'CO0013','Saint Agustine, Florida','Montogomery, Alabama',405,3500,'2017-04-17 09:25:00','AF742','842471P','2017-04-19 17:28:00'),(14,'CO0014','Los Angeles, California','El Paso, Texas',802,2500,'2017-04-18 08:54:00','CA871','156836P','2017-04-21 12:51:00'),(15,'CO0016','Franklin, Kentucky','Providence, Rhode Island',1060,1200,'2017-04-19 08:36:00','DA466','145696S','2017-04-22 11:37:00'),(16,'CO0018','Bismarck, North Dakota','Omaha, Nebraska',610,1400,'2017-04-20 10:03:00','EA657','394204C','2017-04-23 15:39:00');
/*!40000 ALTER TABLE `trip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicle`
--

DROP TABLE IF EXISTS `vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vehicle` (
  `NumberPlate` varchar(5) NOT NULL,
  `Make` text DEFAULT NULL,
  `Model` text DEFAULT NULL,
  `Year` int(11) DEFAULT NULL,
  `Weight` float DEFAULT NULL,
  `VolumeCapacity` float DEFAULT NULL,
  `MaxWeightLoad` float DEFAULT NULL,
  PRIMARY KEY (`NumberPlate`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle`
--

LOCK TABLES `vehicle` WRITE;
/*!40000 ALTER TABLE `vehicle` DISABLE KEYS */;
INSERT INTO `vehicle` VALUES ('AB931','BMW','SE1000',2014,2000,12500,3000),('AC872','Volvo','RE5050',2014,2000,15000,3500),('AD464','GM','SC100',2015,3000,22500,5000),('AE653','Toyota','TR007',2016,3500,30000,4500),('AF742','Hyundai','M077',2016,4000,30000,5000),('CA871','BMW','SE2000',2015,4000,20000,6000),('DA466','Volvo','RE7050',2016,2000,17500,4000),('EA657','GM','SC100',2016,4000,32500,6000),('FA748','Toyota','TR100',2017,3500,40000,6000),('GA744','Hyundai','M077',2017,4000,40000,5500);
/*!40000 ALTER TABLE `vehicle` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-15 22:23:50
