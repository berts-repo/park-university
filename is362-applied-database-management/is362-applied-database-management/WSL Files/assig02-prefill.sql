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
  KEY `fk_LICENSED_PILOT` (`DocumentID`),
  KEY `fk_LICENSED_AIRPLANETYPE` (`AirplaneTypeID`),
  CONSTRAINT `fk_LICENSED_AIRPLANETYPE` FOREIGN KEY (`AirplaneTypeID`) REFERENCES `AIRPLANETYPE` (`TypeID`),
  CONSTRAINT `fk_LICENSED_PILOT` FOREIGN KEY (`DocumentID`) REFERENCES `PILOT` (`PilotID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LICENSED`
--

LOCK TABLES `LICENSED` WRITE;
/*!40000 ALTER TABLE `LICENSED` DISABLE KEYS */;
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
  `Seat` varchar(3) DEFAULT NULL,
  `DocumentID` varchar(7) DEFAULT NULL,
  PRIMARY KEY (`FlightNo`,`FlightDate`),
  UNIQUE KEY `Seat` (`Seat`),
  KEY `fk_SEATEDPASSENGER_PASSENGER` (`DocumentID`),
  CONSTRAINT `fk_SEATEDPASSENGER_PASSENGER` FOREIGN KEY (`DocumentID`) REFERENCES `PASSENGER` (`DocumentID`),
  CONSTRAINT `fk_SEATEDPASSENGER_SCHEDULEDFLIGHT` FOREIGN KEY (`FlightNo`, `FlightDate`) REFERENCES `SCHEDULEDFLIGHT` (`FlightNo`, `FlightDate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SEATEDPASSENGER`
--

LOCK TABLES `SEATEDPASSENGER` WRITE;
/*!40000 ALTER TABLE `SEATEDPASSENGER` DISABLE KEYS */;
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

-- Dump completed on 2024-03-24 11:13:10
