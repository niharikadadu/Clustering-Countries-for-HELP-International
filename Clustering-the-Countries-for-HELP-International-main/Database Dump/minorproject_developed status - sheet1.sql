-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: minorproject
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `developed status - sheet1`
--

DROP TABLE IF EXISTS `developed status - sheet1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `developed status - sheet1` (
  `Country` text,
  `Developed status` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `developed status - sheet1`
--

LOCK TABLES `developed status - sheet1` WRITE;
/*!40000 ALTER TABLE `developed status - sheet1` DISABLE KEYS */;
INSERT INTO `developed status - sheet1` VALUES ('Afghanistan','L'),('Albania','UM'),('Algeria','UM'),('American Samoa','UM'),('Andorra','H'),('Angola','LM'),('Antigua and Barbuda','UM'),('Argentina','UM'),('Armenia','LM'),('Aruba','H'),('Australia','H'),('Austria','H'),('Azerbaijan','UM'),('Bahamas','H'),('Bahrain','H'),('Bangladesh','L'),('Barbados','H'),('Belarus','UM'),('Belgium','H'),('Belize','LM'),('Benin','L'),('Bermuda','H'),('Bhutan','LM'),('Bolivia','LM'),('Bosnia and Herzegovina','UM'),('Botswana','UM'),('Brazil','UM'),('British Virgin Islands','..'),('Brunei','H'),('Bulgaria','UM'),('Burkina Faso','L'),('Burundi','L'),('Cape Verde','LM'),('Cambodia','L'),('Cameroon','LM'),('Canada','H'),('Cayman Islands','H'),('Central African Republic','L'),('Chad','L'),('Channel Islands','H'),('Chile','UM'),('China','UM'),('Colombia','UM'),('Comoros','L'),('Congo, Dem. Rep.','L'),('Congo, Rep.','LM'),('Costa Rica','UM'),('Cote d\'Ivoire','LM'),('Croatia','H'),('Cuba','UM'),('CuraÃ§ao','H'),('Cyprus','H'),('Czech Republic','H'),('Denmark','H'),('Djibouti','LM'),('Dominica','UM'),('Dominican Republic','UM'),('Ecuador','UM'),('Egypt','LM'),('El Salvador','LM'),('Equatorial Guinea','H'),('Eritrea','L'),('Estonia','H'),('Eswatini','LM'),('Ethiopia','L'),('Faeroe Islands','H'),('Fiji','LM'),('Finland','H'),('France','H'),('French Polynesia','H'),('Gabon','UM'),('Gambia','L'),('Georgia','LM'),('Germany','H'),('Ghana','LM'),('Gibraltar','H'),('Greece','H'),('Greenland','H'),('Grenada','UM'),('Guam','H'),('Guatemala','LM'),('Guinea','L'),('Guinea-Bissau','L'),('Guyana','LM'),('Haiti','L'),('Honduras','LM'),('Hong Kong SAR, China','H'),('Hungary','H'),('Iceland','H'),('India','LM'),('Indonesia','LM'),('Iran','UM'),('Iraq','LM'),('Ireland','H'),('Isle of Man','H'),('Israel','H'),('Italy','H'),('Jamaica','UM'),('Japan','H'),('Jordan','UM'),('Kazakhstan','UM'),('Kenya','L'),('Kiribati','LM'),('Korea, Dem. Rep.','L'),('South Korea','H'),('Kosovo','LM'),('Kuwait','H'),('Kyrgyz Republic','L'),('Lao','LM'),('Latvia','UM'),('Lebanon','UM'),('Lesotho','LM'),('Liberia','L'),('Libya','UM'),('Liechtenstein','H'),('Lithuania','UM'),('Luxembourg','H'),('Macao SAR, China','H'),('Madagascar','L'),('Malawi','L'),('Malaysia','UM'),('Maldives','UM'),('Mali','L'),('Malta','H'),('Marshall Islands','LM'),('Mauritania','LM'),('Mauritius','UM'),('Mexico','UM'),('Micronesia, Fed. Sts.','LM'),('Moldova','LM'),('Monaco','H'),('Mongolia','LM'),('Montenegro','UM'),('Morocco','LM'),('Mozambique','L'),('Myanmar','L'),('Namibia','UM'),('Nauru','..'),('Nepal','L'),('Netherlands','H'),('New Caledonia','H'),('New Zealand','H'),('Nicaragua','LM'),('Niger','L'),('Nigeria','LM'),('Macedonia, FYR','UM'),('Northern Mariana Islands','H'),('Norway','H'),('Oman','H'),('Pakistan','LM'),('Palau','UM'),('Panama','UM'),('Papua New Guinea','LM'),('Paraguay','LM'),('Peru','UM'),('Philippines','LM'),('Poland','H'),('Portugal','H'),('Puerto Rico','H'),('Qatar','H'),('Romania','UM'),('Russia','UM'),('Rwanda','L'),('Samoa','LM'),('San Marino','H'),('SÃ£o TomÃ© and PrÃ­ncipe','LM'),('Saudi Arabia','H'),('Senegal','LM'),('Serbia','UM'),('Seychelles','UM'),('Sierra Leone','L'),('Singapore','H'),('Sint Maarten (Dutch part)','H'),('Slovak Republic','H'),('Slovenia','H'),('Solomon Islands','LM'),('Somalia','L'),('South Africa','UM'),('South Sudan','..'),('Spain','H'),('Sri Lanka','LM'),('St. Kitts and Nevis','UM'),('St. Lucia','UM'),('St. Martin (French part)','H'),('St. Vincent and the Grenadines','UM'),('Sudan','LM'),('Suriname','UM'),('Sweden','H'),('Switzerland','H'),('Syrian Arab Republic','LM'),('Taiwan, China','H'),('Tajikistan','L'),('Tanzania','L'),('Thailand','UM'),('Timor-Leste','LM'),('Togo','L'),('Tonga','LM'),('Trinidad and Tobago','H'),('Tunisia','UM'),('Turkey','UM'),('Turkmenistan','LM'),('Turks and Caicos Islands','H'),('Tuvalu','LM'),('Uganda','L'),('Ukraine','LM'),('United Arab Emirates','H'),('United Kingdom','H'),('United States','H'),('Uruguay','UM'),('Uzbekistan','LM'),('Vanuatu','LM'),('Venezuela','UM'),('Vietnam','LM'),('Virgin Islands (U.S.)','H'),('West Bank and Gaza','LM'),('Yemen','LM'),('Zambia','LM'),('Zimbabwe','L');
/*!40000 ALTER TABLE `developed status - sheet1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-30 17:17:05
