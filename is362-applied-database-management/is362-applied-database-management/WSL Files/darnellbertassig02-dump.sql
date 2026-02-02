-- MariaDB dump 10.19  Distrib 10.6.16-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: darnellbertassig02
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
-- Table structure for table `AIRPLANE`
--

DROP TABLE IF EXISTS `AIRPLANE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AIRPLANE` (
  `AirplaneID` varchar(7) NOT NULL,
  `TypeID` varchar(7) DEFAULT NULL,
  PRIMARY KEY (`AirplaneID`),
  KEY `fk_AIRPLANE_AIRPLANETYPE` (`TypeID`),
  CONSTRAINT `fk_AIRPLANE_AIRPLANETYPE` FOREIGN KEY (`TypeID`) REFERENCES `AIRPLANETYPE` (`TypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AIRPLANE`
--

LOCK TABLES `AIRPLANE` WRITE;
/*!40000 ALTER TABLE `AIRPLANE` DISABLE KEYS */;
INSERT INTO `AIRPLANE` VALUES ('A1','Type1'),('A10','Type1'),('A4','Type1'),('A7','Type1'),('A2','Type2'),('A5','Type2'),('A8','Type2'),('A3','Type3'),('A6','Type3'),('A9','Type3');
/*!40000 ALTER TABLE `AIRPLANE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AIRPLANETYPE`
--

DROP TABLE IF EXISTS `AIRPLANETYPE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AIRPLANETYPE` (
  `TypeID` varchar(7) NOT NULL,
  `TypeName` text DEFAULT NULL,
  `TypeDescription` text DEFAULT NULL,
  `NumberOfSeats` int(11) DEFAULT NULL,
  PRIMARY KEY (`TypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AIRPLANETYPE`
--

LOCK TABLES `AIRPLANETYPE` WRITE;
/*!40000 ALTER TABLE `AIRPLANETYPE` DISABLE KEYS */;
INSERT INTO `AIRPLANETYPE` VALUES ('Type1','Type 1','Description of Type 1',111),('Type2','Type 2','Description of Type 2',222),('Type3','Type 3','Description of Type 3',333);
/*!40000 ALTER TABLE `AIRPLANETYPE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FLIGHTCONCESSION`
--

DROP TABLE IF EXISTS `FLIGHTCONCESSION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FLIGHTCONCESSION` (
  `FlightNo` varchar(7) NOT NULL,
  `Origin` text DEFAULT NULL,
  `Destination` text DEFAULT NULL,
  `DayOfTheWeek` bit(7) DEFAULT NULL,
  `TimeOfDay` time DEFAULT NULL,
  PRIMARY KEY (`FlightNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FLIGHTCONCESSION`
--

LOCK TABLES `FLIGHTCONCESSION` WRITE;
/*!40000 ALTER TABLE `FLIGHTCONCESSION` DISABLE KEYS */;
INSERT INTO `FLIGHTCONCESSION` VALUES ('F001','New York','Los Angeles','','08:00:00'),('F002','Los Angeles','Chicago','','10:00:00'),('F003','Chicago','Houston','','12:00:00'),('F004','Houston','Miami','','14:00:00'),('F005','Miami','Seattle','','16:00:00');
/*!40000 ALTER TABLE `FLIGHTCONCESSION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LICENSED`
--

DROP TABLE IF EXISTS `LICENSED`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LICENSED` (
  `DocumentID` varchar(7) DEFAULT NULL,
  `AirplaneTypeID` varchar(7) DEFAULT NULL,
  `DateGranted` date DEFAULT NULL,
  `ExpiryDate` date DEFAULT NULL,
  KEY `fk_LICENSED_AIRPLANETYPE` (`AirplaneTypeID`),
  KEY `fk_LICENSED_PILOT` (`DocumentID`),
  CONSTRAINT `fk_LICENSED_AIRPLANETYPE` FOREIGN KEY (`AirplaneTypeID`) REFERENCES `AIRPLANETYPE` (`TypeID`),
  CONSTRAINT `fk_LICENSED_PILOT` FOREIGN KEY (`DocumentID`) REFERENCES `PILOT` (`PilotID`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LICENSED`
--

LOCK TABLES `LICENSED` WRITE;
/*!40000 ALTER TABLE `LICENSED` DISABLE KEYS */;
INSERT INTO `LICENSED` VALUES ('P001','Type1','2024-01-01','2025-01-01'),('P002','Type2','2024-02-02','2025-02-02'),('P003','Type3','2024-03-03','2025-03-03'),('P004','Type1','2024-04-04','2025-04-04'),('P005','Type2','2024-05-05','2025-05-05'),('P006','Type3','2024-06-06','2025-06-06'),('P007','Type1','2024-07-07','2025-07-07'),('P008','Type2','2024-08-08','2025-08-08'),('P009','Type3','2024-09-09','2025-09-09'),('P010','Type1','2024-10-10','2025-10-10');
/*!40000 ALTER TABLE `LICENSED` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PASSENGER`
--

DROP TABLE IF EXISTS `PASSENGER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PASSENGER` (
  `DocumentID` varchar(7) NOT NULL,
  `FirstName` text DEFAULT NULL,
  `Initials` text DEFAULT NULL,
  `LastName` text DEFAULT NULL,
  PRIMARY KEY (`DocumentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PASSENGER`
--

LOCK TABLES `PASSENGER` WRITE;
/*!40000 ALTER TABLE `PASSENGER` DISABLE KEYS */;
INSERT INTO `PASSENGER` VALUES ('PD001','PassFirstName1','A','PassLastName1'),('PD002','PassFirstName2','B','PassLastName2'),('PD003','PassFirstName3','C','PassLastName3'),('PD004','PassFirstName4','D','PassLastName4'),('PD005','PassFirstName5','E','PassLastName5'),('PD006','PassFirstName6','F','PassLastName6'),('PD007','PassFirstName7','G','PassLastName7'),('PD008','PassFirstName8','H','PassLastName8'),('PD009','PassFirstName9','I','PassLastName9'),('PD010','PassFirstName10','J','PassLastName10');
/*!40000 ALTER TABLE `PASSENGER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PILOT`
--

DROP TABLE IF EXISTS `PILOT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PILOT` (
  `PilotID` varchar(7) NOT NULL,
  `FirstName` text DEFAULT NULL,
  `Initials` text DEFAULT NULL,
  `LastName` text DEFAULT NULL,
  `Salary` float DEFAULT NULL,
  PRIMARY KEY (`PilotID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PILOT`
--

LOCK TABLES `PILOT` WRITE;
/*!40000 ALTER TABLE `PILOT` DISABLE KEYS */;
INSERT INTO `PILOT` VALUES ('P001','FirstName1','A','LastName1',200000),('P002','FirstName2','B','LastName2',210000),('P003','FirstName3','C','LastName3',220000),('P004','FirstName4','D','LastName4',230000),('P005','FirstName5','E','LastName5',240000),('P006','FirstName6','F','LastName6',250000),('P007','FirstName7','G','LastName7',260000),('P008','FirstName8','H','LastName8',270000),('P009','FirstName9','I','LastName9',280000),('P010','FirstName10','J','LastName10',290000);
/*!40000 ALTER TABLE `PILOT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SCHEDULEDFLIGHT`
--

DROP TABLE IF EXISTS `SCHEDULEDFLIGHT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SCHEDULEDFLIGHT` (
  `FlightNo` varchar(7) NOT NULL,
  `FlightDate` date NOT NULL,
  `PilotID` varchar(7) DEFAULT NULL,
  `AirplaneID` varchar(7) DEFAULT NULL,
  PRIMARY KEY (`FlightNo`,`FlightDate`),
  KEY `fk_SCHEDULEDFLIGHT_PILOT` (`PilotID`),
  KEY `fk_SCHEDULEDFLIGHT_AIRPLANE` (`AirplaneID`),
  CONSTRAINT `fk_SCHEDULEDFLIGHT_AIRPLANE` FOREIGN KEY (`AirplaneID`) REFERENCES `AIRPLANE` (`AirplaneID`),
  CONSTRAINT `fk_SCHEDULEDFLIGHT_FLIGHTCONCESSION` FOREIGN KEY (`FlightNo`) REFERENCES `FLIGHTCONCESSION` (`FlightNo`),
  CONSTRAINT `fk_SCHEDULEDFLIGHT_PILOT` FOREIGN KEY (`PilotID`) REFERENCES `PILOT` (`PilotID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SCHEDULEDFLIGHT`
--

LOCK TABLES `SCHEDULEDFLIGHT` WRITE;
/*!40000 ALTER TABLE `SCHEDULEDFLIGHT` DISABLE KEYS */;
INSERT INTO `SCHEDULEDFLIGHT` VALUES ('F001','2024-03-25','P001','A1'),('F002','2024-03-26','P002','A2'),('F003','2024-03-27','P003','A3'),('F004','2024-03-28','P004','A4'),('F005','2024-03-29','P005','A5');
/*!40000 ALTER TABLE `SCHEDULEDFLIGHT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SEATEDPASSENGER`
--

DROP TABLE IF EXISTS `SEATEDPASSENGER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SEATEDPASSENGER` (
  `FlightNo` varchar(7) NOT NULL,
  `FlightDate` date NOT NULL,
  `Seat` varchar(3) NOT NULL,
  `DocumentID` varchar(7) DEFAULT NULL,
  PRIMARY KEY (`Seat`),
  KEY `fk_SEATEDPASSENGER_PASSENGER` (`DocumentID`),
  KEY `FlightNo` (`FlightNo`,`FlightDate`),
  CONSTRAINT `SEATEDPASSENGER_ibfk_1` FOREIGN KEY (`FlightNo`, `FlightDate`) REFERENCES `SCHEDULEDFLIGHT` (`FlightNo`, `FlightDate`),
  CONSTRAINT `SEATEDPASSENGER_ibfk_2` FOREIGN KEY (`FlightNo`, `FlightDate`) REFERENCES `SCHEDULEDFLIGHT` (`FlightNo`, `FlightDate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SEATEDPASSENGER`
--

LOCK TABLES `SEATEDPASSENGER` WRITE;
/*!40000 ALTER TABLE `SEATEDPASSENGER` DISABLE KEYS */;
INSERT INTO `SEATEDPASSENGER` VALUES ('F001','2024-03-25','S00','PD001'),('F001','2024-03-25','s1A','PD001'),('F001','2024-03-25','s1B','PD002'),('F002','2024-03-26','s2A','PD003'),('F002','2024-03-26','s2B','PD004'),('F003','2024-03-27','s3A','PD005'),('F003','2024-03-27','s3B','PD006'),('F004','2024-03-28','s4A','PD007'),('F004','2024-03-28','s4B','PD008'),('F005','2024-03-29','s5A','PD009'),('F005','2024-03-29','s5B','PD010');
/*!40000 ALTER TABLE `SEATEDPASSENGER` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-24 14:46:35
