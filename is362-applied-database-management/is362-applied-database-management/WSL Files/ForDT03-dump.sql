-- MySQL dump 10.16  Distrib 10.2.13-MariaDB, for Win32 (AMD64)
--
-- Host: localhost    Database: ForDT03
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
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article` (
  `ArticleID` varchar(7) NOT NULL,
  `Title` text DEFAULT NULL,
  `Subject` text DEFAULT NULL,
  `NoOFWords` int(11) DEFAULT NULL,
  `PrivateReport` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ArticleID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
INSERT INTO `article` VALUES ('AB00931','The Bull Market of the 2010\'s','Finances',4000,0),('AC01872','Industry Prospects in Africa','Industry',5050,1),('AD03464','Competitive Advantages of South American Investments','Finances',6025,1),('AE12653','Flex Time Increases Productivity','Productivity',1023,1),('AF24742','Report on Gender Compensation Gaps','Human Resources',2356,1),('CA01871','What to do Monseuir Baruch?','General Economy',2517,0),('DA03466','War and War','GeoPolitics',104000,0),('EA12657','Journey to the East','General Economy',3000,0),('FA24748','Concerting with the Devil','GeoPolitics',1000,0),('GA24744','For Whom does the Buzzer Buzz?','Productivity',2560,0);
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company` (
  `CompanyID` varchar(7) NOT NULL,
  `CompanyName` text DEFAULT NULL,
  PRIMARY KEY (`CompanyID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES ('FB','Facebook'),('GOOGL','Alphabet Inc.'),('IBM','International Business Machines'),('MSFT','Microsoft Corporation');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issue`
--

DROP TABLE IF EXISTS `issue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `issue` (
  `IssueNo` int(11) NOT NULL AUTO_INCREMENT,
  `Volume` int(11) DEFAULT NULL,
  `Month` text DEFAULT NULL,
  `Year` int(11) DEFAULT NULL,
  PRIMARY KEY (`IssueNo`)
) ENGINE=InnoDB AUTO_INCREMENT=1204 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue`
--

LOCK TABLES `issue` WRITE;
/*!40000 ALTER TABLE `issue` DISABLE KEYS */;
INSERT INTO `issue` VALUES (1201,21,'January',2016),(1202,21,'February',2016),(1203,21,'March',2016);
/*!40000 ALTER TABLE `issue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `journalist`
--

DROP TABLE IF EXISTS `journalist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `journalist` (
  `JournalistID` varchar(7) NOT NULL,
  `FirstName` text DEFAULT NULL,
  `Initials` text DEFAULT NULL,
  `LastName` text DEFAULT NULL,
  `Office` text DEFAULT NULL,
  `PhoneNo` text DEFAULT NULL,
  PRIMARY KEY (`JournalistID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `journalist`
--

LOCK TABLES `journalist` WRITE;
/*!40000 ALTER TABLE `journalist` DISABLE KEYS */;
INSERT INTO `journalist` VALUES ('145696S','Enrico','Micheal','Caruso','208','555-555-0008'),('156836P','Anna','Divine','Netrebko','207','555-555-0007'),('278544C','Luis','Alberto','Alva','202','555-555-0002'),('394204C','Renee','Haydee','Fleming','209','555-555-0009'),('472507P','Luciano','Guiseppe','Pavarotti','210','555-555-0010'),('736533Q','Andrea','Caramo','Boccelli','204','555-555-0004'),('765256P','Kiri','Te','Kanawa','203','555-555-0003'),('842471P','Placido','Sabado','Domingo','206','555-555-0006'),('865263C','Maria','Angelica','De los Angeles','205','555-555-0005'),('933256Q','Maria','Fernanda','Callas','201','555-555-0001');
/*!40000 ALTER TABLE `journalist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `printed`
--

DROP TABLE IF EXISTS `printed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `printed` (
  `IssueNo` int(11) NOT NULL,
  `ArticleID` varchar(7) NOT NULL,
  `StartPage` int(11) DEFAULT NULL,
  `EndPage` int(11) DEFAULT NULL,
  PRIMARY KEY (`IssueNo`,`ArticleID`),
  KEY `FK_Printed_to_Article` (`ArticleID`),
  CONSTRAINT `FK_Printed_to_Article` FOREIGN KEY (`ArticleID`) REFERENCES `article` (`ArticleID`),
  CONSTRAINT `FK_Printed_to_Issue` FOREIGN KEY (`IssueNo`) REFERENCES `issue` (`IssueNo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `printed`
--

LOCK TABLES `printed` WRITE;
/*!40000 ALTER TABLE `printed` DISABLE KEYS */;
INSERT INTO `printed` VALUES (1201,'CA01871',933,945),(1201,'DA03466',403,415),(1202,'EA12657',723,787),(1202,'FA24748',211,221),(1203,'AB00931',66,75),(1203,'GA24744',356,379);
/*!40000 ALTER TABLE `printed` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `private`
--

DROP TABLE IF EXISTS `private`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `private` (
  `ArticleID` varchar(7) NOT NULL,
  `CompanyID` varchar(7) NOT NULL,
  `Price` float DEFAULT NULL,
  PRIMARY KEY (`ArticleID`,`CompanyID`),
  KEY `FK_Private_to_Company` (`CompanyID`),
  CONSTRAINT `FK_Private_to_Article` FOREIGN KEY (`ArticleID`) REFERENCES `article` (`ArticleID`),
  CONSTRAINT `FK_Private_to_Company` FOREIGN KEY (`CompanyID`) REFERENCES `company` (`CompanyID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `private`
--

LOCK TABLES `private` WRITE;
/*!40000 ALTER TABLE `private` DISABLE KEYS */;
INSERT INTO `private` VALUES ('AC01872','IBM',20000),('AD03464','GOOGL',17300),('AE12653','FB',23000),('AF24742','MSFT',16000);
/*!40000 ALTER TABLE `private` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `webpublished`
--

DROP TABLE IF EXISTS `webpublished`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `webpublished` (
  `ArticleID` varchar(7) NOT NULL,
  `Website` text DEFAULT NULL,
  PRIMARY KEY (`ArticleID`),
  CONSTRAINT `FK_WebPublished_to_Article` FOREIGN KEY (`ArticleID`) REFERENCES `article` (`ArticleID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webpublished`
--

LOCK TABLES `webpublished` WRITE;
/*!40000 ALTER TABLE `webpublished` DISABLE KEYS */;
INSERT INTO `webpublished` VALUES ('AB00931','https://www.ourcompany.com/AB00931'),('CA01871','https://www.ourcompany.com/CA01871'),('DA03466','https://www.ourcompany.com/DA03466'),('EA12657','https://www.ourcompany.com/EA12657'),('FA24748','https://www.ourcompany.com/FA24748'),('GA24744','https://www.ourcompany.com/GA24744');
/*!40000 ALTER TABLE `webpublished` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `writtenby`
--

DROP TABLE IF EXISTS `writtenby`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `writtenby` (
  `JournalistID` varchar(7) NOT NULL,
  `ArticleID` varchar(7) NOT NULL,
  `AuthorRank` int(11) DEFAULT NULL,
  PRIMARY KEY (`JournalistID`,`ArticleID`),
  KEY `FK_WrittenBy_to_Article` (`ArticleID`),
  CONSTRAINT `FK_WrittenBy_to_Article` FOREIGN KEY (`ArticleID`) REFERENCES `article` (`ArticleID`),
  CONSTRAINT `FK_WrittenBy_to_Journalist` FOREIGN KEY (`JournalistID`) REFERENCES `journalist` (`JournalistID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `writtenby`
--

LOCK TABLES `writtenby` WRITE;
/*!40000 ALTER TABLE `writtenby` DISABLE KEYS */;
INSERT INTO `writtenby` VALUES ('145696S','AD03464',2),('145696S','DA03466',2),('145696S','EA12657',1),('156836P','AC01872',2),('156836P','DA03466',1),('156836P','EA12657',2),('278544C','AC01872',1),('394204C','AE12653',2),('394204C','CA01871',2),('394204C','FA24748',1),('472507P','AB00931',2),('472507P','AF24742',2),('472507P','GA24744',1),('736533Q','AE12653',1),('765256P','AD03464',1),('842471P','CA01871',1),('865263C','AF24742',1),('865263C','FA24748',2),('865263C','GA24744',2),('933256Q','AB00931',1);
/*!40000 ALTER TABLE `writtenby` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-17 14:24:17
