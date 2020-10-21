CREATE DATABASE  IF NOT EXISTS `project`;
USE `project`;
-- MariaDB dump 10.17  Distrib 10.4.10-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	10.4.10-MariaDB

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
-- Table structure for table `billing`
--

DROP TABLE IF EXISTS `billing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `billing` (
  `billing_id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` varchar(100) DEFAULT NULL,
  `total_amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`billing_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `billing`
--

LOCK TABLES `billing` WRITE;
/*!40000 ALTER TABLE `billing` DISABLE KEYS */;
INSERT INTO `billing` VALUES (1,'600.0','678.0'),(2,'2991.0','3379.83'),(3,'17.0','19.21'),(4,'21.0','23.73');
/*!40000 ALTER TABLE `billing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login` (
  `login_id` int(11) NOT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (1234,'password');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_store`
--

DROP TABLE IF EXISTS `product_store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_store` (
  `product_number` varchar(100) NOT NULL,
  `number_of_units` varchar(100) DEFAULT NULL,
  `product_wholesale_price` varchar(100) DEFAULT NULL,
  `product_expiry_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_number`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_store`
--

LOCK TABLES `product_store` WRITE;
/*!40000 ALTER TABLE `product_store` DISABLE KEYS */;
INSERT INTO `product_store` VALUES ('Q01','100.0','2.0','10-Dec-2020'),('Q02','150.0','16.0','20-Jan-2021'),('Q03','100.0','3.0','10-Jan-2021'),('Q04','150.0','5.0','19-Oct-2020'),('Q05','200.0','7.0','11-Nov-2020'),('Q06','100.0','9.0','20-Mar-2021'),('Q08','20.0','11.0','12-Sep-2021'),('Q09','50.0','24.0','Sep 2022');
/*!40000 ALTER TABLE `product_store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `product_number` varchar(100) NOT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  `product_description` varchar(200) DEFAULT NULL,
  `product_unit_price` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_number`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('Q01','Eggs','Chicken Eggs','1.0'),('Q02','Malboro-Cig','Malboro Products','15.0'),('Q03','Red Bull','Beverage drinks','2.0'),('Q04','Coca-Cola','Beverage Drinks 500ML','4.0'),('Q05','Tim Bits','Dessert','6.0'),('Q06','Fask Masks','Masks','8.0'),('Q08','Sanitizer','Health and Safety','10.0'),('Q09','Cloth','Cloth','21.0');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_products_billing`
--

DROP TABLE IF EXISTS `store_products_billing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `store_products_billing` (
  `billing_id` int(11) DEFAULT NULL,
  `product_number` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  KEY `billing_id` (`billing_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_products_billing`
--

LOCK TABLES `store_products_billing` WRITE;
/*!40000 ALTER TABLE `store_products_billing` DISABLE KEYS */;
INSERT INTO `store_products_billing` VALUES (1,'Q04','100.0','4.0'),(1,'Q04','50.0','4.0'),(2,'Q01','80.0','1.0'),(2,'Q02','145.0','15.0'),(2,'Q06','92.0','8.0'),(3,'Q02','1.0','15.0'),(3,'Q03','1.0','2.0'),(4,'Q09','1.0','21.0');
/*!40000 ALTER TABLE `store_products_billing` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-19 21:24:57
