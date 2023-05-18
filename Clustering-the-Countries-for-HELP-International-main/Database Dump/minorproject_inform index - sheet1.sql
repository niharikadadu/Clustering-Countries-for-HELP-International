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
-- Table structure for table `inform index - sheet1`
--

DROP TABLE IF EXISTS `inform index - sheet1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inform index - sheet1` (
  `Iso3` text,
  `CountryName` text,
  `HA` double DEFAULT NULL,
  `VU` double DEFAULT NULL,
  `CC` double DEFAULT NULL,
  `INFORM` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inform index - sheet1`
--

LOCK TABLES `inform index - sheet1` WRITE;
/*!40000 ALTER TABLE `inform index - sheet1` DISABLE KEYS */;
INSERT INTO `inform index - sheet1` VALUES ('AFG','Afghanistan',8.9,8.5,7.1,8.1),('ALB','Albania',3.8,1.7,4.4,3.1),('DZA','Algeria',3.6,2.9,4.4,3.6),('AGO','Angola',2.7,5.1,6.9,4.6),('ATG','Antigua and Barbuda',2,1.5,3.7,2.2),('ARG','Argentina',2.4,2.9,3.6,2.9),('ARM','Armenia',8.4,2.6,4.5,4.6),('AUS','Australia',2.9,2.2,2.1,2.4),('AUT','Austria',1.5,3,1.5,1.9),('AZE','Azerbaijan',8.5,5,4.6,5.8),('BHS','Bahamas',1.8,1.7,3.1,2.1),('BHR','Bahrain',0.5,1.1,3,1.2),('BGD','Bangladesh',6.3,5.5,4.9,5.5),('BRB','Barbados',2.1,1.4,2.6,2),('BLR','Belarus',1.1,1.7,3,1.8),('BEL','Belgium',1.1,2.5,1.9,1.7),('BLZ','Belize',3.2,3.6,5.2,3.9),('BEN','Benin',1.7,4.7,6.7,3.8),('BTN','Bhutan',2,3.5,4.4,3.1),('BOL','Bolivia',3.1,3.8,5.3,4),('BIH','Bosnia and Herzegovina',2.3,3.8,4.9,3.5),('BWA','Botswana',1.5,3.6,4.6,2.9),('BRA','Brazil',5.7,3.8,4.3,4.5),('BRN','Brunei',1.4,1.1,3.5,1.8),('BGR','Bulgaria',2,3.2,3.2,2.7),('BFA','Burkina Faso',7.1,7.7,6.4,7),('BDI','Burundi',4.7,6.6,6.8,6),('CPV','Cape Verde',1,3.7,3.8,2.4),('KHM','Cambodia',3.5,4,5.9,4.4),('CMR','Cameroon',7.1,6.7,5.9,6.5),('CAN','Canada',2.5,2.3,2.4,2.4),('CAF','Central African Republic',8.1,8.7,8.8,8.5),('TCD','Chad',7.2,7.6,8.8,7.8),('CHL','Chile',3.8,3.8,2.8,3.4),('CHN','China',5,3,3.3,3.7),('COL','Colombia',6.9,6.2,3.6,5.4),('COM','Comoros',1.5,4.6,7.1,3.7),('COD','Congo, Dem. Rep.',7.3,7.5,8.1,7.6),('COG','Congo, Rep.',2.8,6.5,7.6,5.2),('CRI','Costa Rica',3.7,4.6,2.5,3.5),('CIV','Cote d\'Ivoire',2.5,5.6,6.6,4.5),('HRV','Croatia',2.8,2,3.1,2.6),('CUB','Cuba',3.3,1.2,2.9,2.3),('CYP','Cyprus',2.4,4.1,2.6,2.9),('CZE','Czech Republic',0.9,3.4,2,1.8),('DNK','Denmark',0.7,2.1,1.3,1.2),('DJI','Djibouti',3.4,5.4,6.1,4.8),('DMA','Dominica',2.8,2.5,4.1,3.1),('DOM','Dominican Republic',4.1,3.8,4.4,4.1),('TLS','Timor-Leste',2.6,4.4,5.8,4),('ECU','Ecuador',4.9,4.9,4,4.6),('EGY','Egypt',6.1,3.8,4.5,4.7),('SLV','El Salvador',3.9,4.4,4.6,4.3),('GNQ','Equatorial Guinea',1.6,3.3,7.3,3.4),('ERI','Eritrea',7.1,4.4,7.7,6.2),('EST','Estonia',0.5,2.6,1.6,1.3),('SWZ','Eswatini',1.5,4.3,5.5,3.3),('ETH','Ethiopia',7.3,7.1,6.7,7),('FJI','Fiji',2.2,3.4,2.7,2.7),('FIN','Finland',0.3,2.1,1.3,0.9),('FRA','France',2.1,3,1.9,2.3),('GAB','Gabon',1.4,3.4,6.1,3.1),('GMB','Gambia',1.7,5.4,5.4,3.7),('GEO','Georgia',2.5,4.8,3.2,3.4),('DEU','Germany',1.6,3.8,1.6,2.1),('GHA','Ghana',2.2,4.1,4.9,3.5),('GRC','Greece',3.5,2.8,2.3,2.8),('GRD','Grenada',0.9,2.2,3.7,1.9),('GTM','Guatemala',4.2,5.7,5.4,5.1),('GIN','Guinea',3.3,4.2,7,4.6),('GNB','Guinea-Bissau',1.4,4.8,7.9,3.8),('GUY','Guyana',2.1,4.4,5.1,3.6),('HTI','Haiti',6.4,5.9,7.2,6.5),('HND','Honduras',3.9,6.3,5.3,5.1),('HUN','Hungary',2,2,2.1,2),('ISL','Iceland',1.2,1.2,1.9,1.4),('IND','India',7.4,4.8,4.2,5.3),('IDN','Indonesia',6.7,3.3,4.4,4.6),('IRN','Iran',6.7,4.4,4.6,5.1),('IRQ','Iraq',7.8,5.8,6.5,6.6),('IRL','Ireland',1.3,2,1.7,1.6),('ISR','Israel',5.9,1.7,2.2,2.8),('ITA','Italy',3,2.6,2.2,2.6),('JAM','Jamaica',3.2,2.5,3.6,3.1),('JPN','Japan',5.4,1.3,1.5,2.2),('JOR','Jordan',2.7,6.2,4.4,4.2),('KAZ','Kazakhstan',2.4,0.7,3.7,1.8),('KEN','Kenya',8.5,6.1,5.8,6.7),('KIR','Kiribati',2,3.9,5.2,3.4),('PRK','Korea Dem.People\'s Rep.',3.1,3.9,6.4,4.3),('KWT','Kuwait',1,1.5,3.7,1.8),('KGZ','Kyrgyz Republic',2.9,2.3,4.3,3.1),('LAO','Lao',2.9,3.5,5.9,3.9),('LVA','Latvia',1.1,2.5,2.5,1.9),('LBN','Lebanon',3.2,6.4,4.4,4.5),('LSO','Lesotho',1.5,5.8,6.8,3.9),('LBR','Liberia',2.2,5.9,7.8,4.7),('LBY','Libya',8.2,4,7.1,6.2),('LIE','Liechtenstein',0.7,0.7,1,0.8),('LTU','Lithuania',0.8,2.6,2.2,1.7),('LUX','Luxembourg',0.5,1.9,1.1,1),('MDG','Madagascar',3.9,5.3,7.1,5.3),('MWI','Malawi',2.6,5.5,6.4,4.5),('MYS','Malaysia',2.9,3,3,3),('MDV','Maldives',1.7,2,4,2.4),('MLI','Mali',7.3,6.8,6.6,6.9),('MLT','Malta',1.3,2.2,2.3,1.9),('MHL','Marshall Islands',2,4.6,6.2,3.8),('MRT','Mauritania',3.2,5.6,6.5,4.9),('MUS','Mauritius',2.1,1.6,2.8,2.1),('MEX','Mexico',6.9,4.3,4.4,5.1),('FSM','Micronesia, Fed. Sts.',2.3,3.9,5,3.6),('MDA','Moldova',2.3,3.7,4.5,3.4),('MNG','Mongolia',1.6,2.3,4.6,2.6),('MNE','Montenegro',2.4,2.6,3.2,2.7),('MAR','Morocco',2.7,3.4,4.6,3.5),('MOZ','Mozambique',7.8,7.8,6.2,7.2),('MMR','Myanmar',9.2,5.5,6.1,6.8),('NAM','Namibia',2.6,4.9,5,4),('NRU','Nauru',1.6,4,5.1,3.2),('NPL','Nepal',3.6,4.4,5.5,4.4),('NLD','Netherlands',1.1,2.5,1.3,1.5),('NZL','New Zealand',2.5,0.9,1.8,1.6),('NIC','Nicaragua',4.2,3.7,5.3,4.4),('NER','Niger',7.3,7.6,7.5,7.5),('NGA','Nigeria',7.2,5.8,6.3,6.4),('MKD','Macedonia, FYR',2.1,2.1,3.6,2.5),('NOR','Norway',0.3,1.9,1.5,0.9),('OMN','Oman',2.9,1.6,3.7,2.6),('PAK','Pakistan',7.2,5.8,5.4,6.1),('PLW','Palau',2,4.4,4,3.3),('PSE','Palestine',4.1,6.1,4,4.6),('PAN','Panama',3.8,3.8,4.1,3.9),('PNG','Papua New Guinea',5.1,5.5,7.3,5.9),('PRY','Paraguay',1.4,2.9,4.2,2.6),('PER','Peru',4.6,5.5,4.4,4.8),('PHL','Philippines',7.8,4.4,4.1,5.2),('POL','Poland',1.3,3.9,3,2.5),('PRT','Portugal',1.9,2.1,2,2),('QAT','Qatar',0.9,1,2.9,1.4),('ROU','Romania',2.3,2.5,3.4,2.7),('RUS','Russia',4.4,3.6,4.3,4.1),('RWA','Rwanda',3,5.9,5,4.5),('KNA','Saint Kitts and Nevis',1.5,1.8,2.8,2),('LCA','Saint Lucia',1.4,2.3,3.9,2.3),('VCT','St. Vincent and the Grenadines',1.4,2.6,3.5,2.3),('WSM','Samoa',2,3.4,4.2,3.1),('STP','Sao Tome and Principe',0.6,4.8,5.3,2.5),('SAU','Saudi Arabia',8.1,1.6,3.4,3.5),('SEN','Senegal',2.6,5,5.5,4.2),('SRB','Serbia',2.5,2.4,3.7,2.8),('SYC','Seychelles',1.6,1.4,2.9,1.9),('SLE','Sierra Leone',2.2,5.8,6.8,4.4),('SGP','Singapore',0.5,0.3,1,0.5),('SVK','Slovak Republic',1.5,2.6,2.6,2.2),('SVN','Slovenia',1.9,1.3,1.6,1.6),('SLB','Solomon Islands',3.4,4,6.5,4.5),('SOM','Somalia',8.9,8.6,8.6,8.7),('ZAF','South Africa',6.8,5.4,4,5.3),('KOR','South Korea',3.5,1.2,1.6,1.9),('SSD','South Sudan',7.2,8.8,9.4,8.4),('ESP','Spain',2.4,2.7,1.8,2.3),('LKA','Sri Lanka',3.3,2.7,4,3.3),('SDN','Sudan',7.3,7.2,6.7,7.1),('SUR','Suriname',2.3,3,4.9,3.2),('SWE','Sweden',0.6,2.9,1.5,1.4),('CHE','Switzerland',1.3,2.5,0.9,1.4),('SYR','Syrian Arab Republic',7.8,7.8,5.5,6.9),('TJK','Tajikistan',3.7,3.8,4.9,4.1),('TZA','Tanzania',5.6,5.5,6.2,5.8),('THA','Thailand',5.6,2.9,3.9,4),('TGO','Togo',1.7,5.1,7.5,4),('TON','Tonga',3,4.4,4.2,3.8),('TTO','Trinidad and Tobago',1.7,3.3,3.3,2.6),('TUN','Tunisia',2.7,2.1,4.7,3),('TUR','Turkey',6.6,4.8,3.2,4.7),('TKM','Turkmenistan',2.1,1.6,5.9,2.7),('TUV','Tuvalu',2,4.6,5,3.6),('UGA','Uganda',7.4,6.8,7,7.1),('UKR','Ukraine',5.4,5.4,4.5,5.1),('ARE','United Arab Emirates',2.4,1.2,1.8,1.7),('GBR','United Kingdom',1.8,2.4,1.6,1.9),('USA','United States',4.6,3.1,2.2,3.2),('URY','Uruguay',0.9,2.5,2.6,1.8),('UZB','Uzbekistan',3.2,3.1,3.8,3.4),('VUT','Vanuatu',3.3,4,5.5,4.2),('VEN','Venezuela',6.6,3.8,5,5),('VNM','Vietnam',4.7,2,4,3.4),('YEM','Yemen',8.4,8.1,7.9,8.1),('ZMB','Zambia',2.1,6,5.9,4.2),('ZWE','Zimbabwe',3,5.4,5.8,4.5);
/*!40000 ALTER TABLE `inform index - sheet1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-30 17:17:04
