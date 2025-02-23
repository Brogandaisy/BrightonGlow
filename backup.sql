-- MySQL dump 10.13  Distrib 9.2.0, for macos15.2 (arm64)
--
-- Host: localhost    Database: brightonglow_db
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_customer`
--

DROP TABLE IF EXISTS `accounts_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `phone` varchar(15) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `address_country` varchar(255) DEFAULT NULL,
  `address_county` varchar(255) DEFAULT NULL,
  `address_line1` varchar(255) DEFAULT NULL,
  `address_postcode` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `email` (`email`),
  CONSTRAINT `accounts_customer_user_id_11606857_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customer`
--

LOCK TABLES `accounts_customer` WRITE;
/*!40000 ALTER TABLE `accounts_customer` DISABLE KEYS */;
INSERT INTO `accounts_customer` VALUES (1,'07792349369','2025-02-13 11:40:52.965905',2,'brogancarpenter@hotmail.co.uk','england','sussex','Flat 2','bn3221'),(2,'01234567777','2025-02-14 14:54:25.190116',3,'annabel@gmail.com','england','hampshire','6 hadden court','te456ht');
/*!40000 ALTER TABLE `accounts_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add product',7,'add_product'),(26,'Can change product',7,'change_product'),(27,'Can delete product',7,'delete_product'),(28,'Can view product',7,'view_product'),(29,'Can add customer',8,'add_customer'),(30,'Can change customer',8,'change_customer'),(31,'Can delete customer',8,'delete_customer'),(32,'Can view customer',8,'view_customer'),(33,'Can add category',9,'add_category'),(34,'Can change category',9,'change_category'),(35,'Can delete category',9,'delete_category'),(36,'Can view category',9,'view_category'),(37,'Can add order item',10,'add_orderitem'),(38,'Can change order item',10,'change_orderitem'),(39,'Can delete order item',10,'delete_orderitem'),(40,'Can view order item',10,'view_orderitem'),(41,'Can add order',11,'add_order'),(42,'Can change order',11,'change_order'),(43,'Can delete order',11,'delete_order'),(44,'Can view order',11,'view_order');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$6Fa1e2Uv16ehWYFFTPgKTJ$lZjDDQuj1zSupM1/JUBNuKX1AewXhhSv9K0fzXu/mhk=','2025-02-23 15:58:09.632437',1,'brogancarpenter','','','brogancarpenter@hotmail.co.uk',1,1,'2025-02-07 20:37:01.116412'),(2,'pbkdf2_sha256$870000$SRbRznMfBe1AJMUp04NuYc$wwa1h/5KGe+N8eAZpHOKV3n5yQ5hEo7qbMm5Ggzm7N0=','2025-02-22 10:21:08.828792',0,'brogandaisy','','','',0,1,'2025-02-13 11:40:52.619352'),(3,'pbkdf2_sha256$870000$dk6eQ9FnougVfEnCANil2G$L8Hxvw6xiAaVp4C+Lb9rz8vMg06l7mgUX6r3RzZm97A=','2025-02-14 15:01:32.136008',0,'annabel1','','','annabel@gmail.com',0,1,'2025-02-14 14:54:24.852995');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-02-17 18:45:26.766435','4','Order 4 by brogandaisy',2,'[{\"changed\": {\"fields\": [\"User\"]}}]',11,1),(2,'2025-02-17 21:59:53.663761','1','BrightonGlow Candle',3,'',7,1),(3,'2025-02-21 18:51:42.018867','44','Order 44 by brogancarpenter',3,'',11,1),(4,'2025-02-21 18:51:42.018911','43','Order 43 by brogancarpenter',3,'',11,1),(5,'2025-02-21 18:51:42.018926','42','Order 42 by brogancarpenter',3,'',11,1),(6,'2025-02-21 18:51:42.018937','41','Order 41 by brogancarpenter',3,'',11,1),(7,'2025-02-21 18:51:42.018947','40','Order 40 by brogancarpenter',3,'',11,1),(8,'2025-02-21 18:51:42.018957','39','Order 39 by brogancarpenter',3,'',11,1),(9,'2025-02-21 18:51:42.018968','38','Order 38 by brogancarpenter',3,'',11,1),(10,'2025-02-21 18:51:42.018977','37','Order 37 by brogancarpenter',3,'',11,1),(11,'2025-02-21 18:51:42.018987','36','Order 36 by brogancarpenter',3,'',11,1),(12,'2025-02-21 18:51:42.018997','35','Order 35 by brogancarpenter',3,'',11,1),(13,'2025-02-21 18:51:42.019006','34','Order 34 by brogancarpenter',3,'',11,1),(14,'2025-02-21 18:51:42.019016','33','Order 33 by brogancarpenter',3,'',11,1),(15,'2025-02-21 18:51:42.019025','32','Order 32 by brogancarpenter',3,'',11,1),(16,'2025-02-21 18:51:42.019034','31','Order 31 by brogancarpenter',3,'',11,1),(17,'2025-02-21 18:51:42.019043','30','Order 30 by brogancarpenter',3,'',11,1),(18,'2025-02-21 18:51:42.019053','29','Order 29 by brogancarpenter',3,'',11,1),(19,'2025-02-21 18:51:42.019063','28','Order 28 by brogancarpenter',3,'',11,1),(20,'2025-02-21 18:51:42.019072','26','Order 26 by brogancarpenter',3,'',11,1),(21,'2025-02-21 18:51:42.019082','25','Order 25 by brogancarpenter',3,'',11,1),(22,'2025-02-21 18:51:42.019091','24','Order 24 by brogancarpenter',3,'',11,1),(23,'2025-02-21 18:51:42.019101','23','Order 23 by brogancarpenter',3,'',11,1),(24,'2025-02-21 18:51:42.019110','22','Order 22 by brogancarpenter',3,'',11,1),(25,'2025-02-21 18:51:42.019119','21','Order 21 by brogancarpenter',3,'',11,1),(26,'2025-02-21 18:51:42.019128','19','Order 19 by brogancarpenter',3,'',11,1),(27,'2025-02-21 18:51:42.019137','18','Order 18 by brogancarpenter',3,'',11,1),(28,'2025-02-21 18:51:42.019147','17','Order 17 by brogancarpenter',3,'',11,1),(29,'2025-02-21 18:51:42.019156','16','Order 16 by brogancarpenter',3,'',11,1),(30,'2025-02-21 18:51:42.019165','15','Order 15 by brogancarpenter',3,'',11,1),(31,'2025-02-21 18:51:42.019174','14','Order 14 by brogancarpenter',3,'',11,1),(32,'2025-02-21 18:51:42.019183','13','Order 13 by brogancarpenter',3,'',11,1),(33,'2025-02-21 18:51:42.019192','12','Order 12 by brogancarpenter',3,'',11,1),(34,'2025-02-21 18:51:42.019201','11','Order 11 by brogancarpenter',3,'',11,1),(35,'2025-02-21 18:51:42.019210','10','Order 10 by brogancarpenter',3,'',11,1),(36,'2025-02-21 18:51:42.019220','9','Order 9 by brogancarpenter',3,'',11,1),(37,'2025-02-21 18:51:42.019230','8','Order 8 by brogancarpenter',3,'',11,1),(38,'2025-02-21 18:51:42.019240','7','Order 7 by brogancarpenter',3,'',11,1),(39,'2025-02-21 18:51:42.019250','6','Order 6 by brogancarpenter',3,'',11,1),(40,'2025-02-21 18:51:42.019260','5','Order 5 by brogancarpenter',3,'',11,1),(41,'2025-02-21 18:51:42.019270','3','Order 3 by brogancarpenter',3,'',11,1),(42,'2025-02-21 18:51:42.019280','2','Order 2 by brogancarpenter',3,'',11,1),(43,'2025-02-21 18:51:42.019289','1','Order 1 by brogancarpenter',3,'',11,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (8,'accounts','customer'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'orders','order'),(10,'orders','orderitem'),(9,'products','category'),(7,'products','product'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-02-07 20:35:22.901819'),(2,'auth','0001_initial','2025-02-07 20:35:22.973732'),(3,'admin','0001_initial','2025-02-07 20:35:22.993681'),(4,'admin','0002_logentry_remove_auto_add','2025-02-07 20:35:22.996390'),(5,'admin','0003_logentry_add_action_flag_choices','2025-02-07 20:35:22.998460'),(6,'contenttypes','0002_remove_content_type_name','2025-02-07 20:35:23.014500'),(7,'auth','0002_alter_permission_name_max_length','2025-02-07 20:35:23.025648'),(8,'auth','0003_alter_user_email_max_length','2025-02-07 20:35:23.038629'),(9,'auth','0004_alter_user_username_opts','2025-02-07 20:35:23.040756'),(10,'auth','0005_alter_user_last_login_null','2025-02-07 20:35:23.049273'),(11,'auth','0006_require_contenttypes_0002','2025-02-07 20:35:23.049752'),(12,'auth','0007_alter_validators_add_error_messages','2025-02-07 20:35:23.051827'),(13,'auth','0008_alter_user_username_max_length','2025-02-07 20:35:23.062272'),(14,'auth','0009_alter_user_last_name_max_length','2025-02-07 20:35:23.073041'),(15,'auth','0010_alter_group_name_max_length','2025-02-07 20:35:23.078140'),(16,'auth','0011_update_proxy_permissions','2025-02-07 20:35:23.080544'),(17,'auth','0012_alter_user_first_name_max_length','2025-02-07 20:35:23.091912'),(18,'sessions','0001_initial','2025-02-07 20:35:23.096782'),(19,'products','0001_initial','2025-02-12 16:48:19.277732'),(20,'accounts','0001_initial','2025-02-13 11:22:20.082256'),(21,'accounts','0002_customer_email_alter_customer_phone','2025-02-14 10:17:50.045898'),(22,'products','0002_category','2025-02-14 10:17:50.063665'),(23,'accounts','0003_remove_customer_address_customer_address_country_and_more','2025-02-14 10:46:25.950207'),(24,'orders','0001_initial','2025-02-14 15:18:55.301135'),(25,'orders','0002_order_stripe_payment_intent','2025-02-15 17:07:32.990199'),(26,'orders','0003_order_shipping_address_order_shipping_city_and_more','2025-02-21 17:40:19.072718');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('vmwginbod6olseay8w95mnuav4uypakb','e30:1tmENG:Fpv2EkYCGOqIIaNFaCtFHlgE0aQv1NJHUNWSeLYqS_c','2025-02-24 15:58:34.000262'),('vvmi4c197gg01aqw14unfb6gybg00w59','.eJx1j7FuhDAQRP9la2SBwcbrMn2-AY3tvYPkBAmYIjrx72ekK-6KbLHFzJuR5k4D9jwO-ybrMCXypKl61QLit8ynkb4wXxcVlzmvU1Anop7upj6XJLePJ_tWMGIbS1o6G7RrxbJAS-fQG45IcBBj2_7CNqTOtc6C5WJ6Rh2BOvUGKGqUUpqXjBv5rlHs-OVMRQFX8ndqzve7Y85T_iPfVPSzTiXrG1bMR1XG_QNorerjOB58vFVM:1tk9Do:r_KBexVXuvG1Zl4mOgMwTqtGc05eQp7wvsp9G6HU8Mc','2025-03-03 22:04:12.741019');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_order`
--

DROP TABLE IF EXISTS `orders_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(20) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `stripe_payment_intent` varchar(255) DEFAULT NULL,
  `shipping_address` varchar(255) DEFAULT NULL,
  `shipping_city` varchar(100) DEFAULT NULL,
  `shipping_country` varchar(50) DEFAULT NULL,
  `shipping_name` varchar(255) DEFAULT NULL,
  `shipping_postcode` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_order_user_id_e9b59eb1_fk_auth_user_id` (`user_id`),
  CONSTRAINT `orders_order_user_id_e9b59eb1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_order`
--

LOCK TABLES `orders_order` WRITE;
/*!40000 ALTER TABLE `orders_order` DISABLE KEYS */;
INSERT INTO `orders_order` VALUES (62,'PENDING',22.00,'2025-02-22 13:51:33.310799','2025-02-22 13:51:33.310827',1,NULL,NULL,NULL,NULL,NULL,NULL),(63,'PENDING',44.00,'2025-02-22 15:50:37.527176','2025-02-22 15:50:37.527205',1,NULL,NULL,NULL,NULL,NULL,NULL),(64,'PENDING',42.00,'2025-02-22 15:52:40.980943','2025-02-22 15:52:40.980992',1,NULL,NULL,NULL,NULL,NULL,NULL),(65,'PENDING',64.00,'2025-02-22 15:57:35.934161','2025-02-22 15:57:36.643143',1,'cs_test_a1ZyZM0MCMsT4Gv5XC15eRJC7GcWfITfREgOLGyMj8G1mtk840SFXcPFZG',NULL,NULL,NULL,NULL,NULL),(66,'PENDING',64.00,'2025-02-22 16:08:50.889230','2025-02-22 16:08:51.571323',1,'cs_test_a14Hqi7YgwkF8DYDtdl24SAlwIEbwqrmXSLXvupVYLVXTVWqcIs24N3tQM',NULL,NULL,NULL,NULL,NULL),(67,'PENDING',22.00,'2025-02-22 16:10:57.821758','2025-02-22 16:10:58.447647',1,'cs_test_a1akF01IKIDfpzilgmb2XRy957SprSBiWDnT8TpsJgpdYInt5MVs69ufdS',NULL,NULL,NULL,NULL,NULL),(68,'PENDING',22.00,'2025-02-22 16:12:40.731520','2025-02-22 16:12:41.363474',1,'cs_test_a1ZpmxO4u8r27UwaMoK85yxaE874Z8tRYyqkf7P63lDEPL9RvhW5mgXBuw',NULL,NULL,NULL,NULL,NULL),(69,'PENDING',22.00,'2025-02-22 16:19:48.309698','2025-02-22 16:19:48.991044',1,'cs_test_a14SIic4kTmJKMlIQaWozQ4FD5nGkXmbf2KaokDi2qnGGfTky1k2oI9jw9',NULL,NULL,NULL,NULL,NULL),(70,'PENDING',66.00,'2025-02-22 17:11:31.489417','2025-02-22 17:11:32.178713',1,'cs_test_a1HdVrSiOM4uQhcNTgnRQr4RNVl1bUa4nsWfZisLByN8cSYcYQkGrDRTsw',NULL,NULL,NULL,NULL,NULL),(71,'PENDING',44.00,'2025-02-22 17:25:53.891456','2025-02-22 17:25:54.502937',1,'cs_test_a1a3xT9KhQfd8lyOWmVshvRFNcVxwvkkihFxSFqkYGSB1CL3oqVfMBTAoT',NULL,NULL,NULL,NULL,NULL),(72,'PENDING',138.00,'2025-02-22 19:46:24.845731','2025-02-22 19:46:25.494912',1,'cs_test_a1eJm110tgcenKP7GAT7lJvSjWTRp1QaLYR2SzvuZ0FZvLVRsaGzikJ3rF',NULL,NULL,NULL,NULL,NULL),(73,'PENDING',50.00,'2025-02-22 22:20:23.771664','2025-02-22 22:20:24.429182',1,'cs_test_a11ysH3i3WjGEUe2vHUwkpyFxAtjF3vofu2e0drO8w5iVFaMS6ePeJLLXB',NULL,NULL,NULL,NULL,NULL),(74,'PENDING',22.00,'2025-02-22 22:21:29.189815','2025-02-22 22:21:29.867318',1,'cs_test_a1bUBjVb6HHukFWMxmFRzaH4FxKst8wdyCcfKhQlVVPpKHjbdAZuueM6vf',NULL,NULL,NULL,NULL,NULL),(75,'PENDING',140.00,'2025-02-22 22:23:20.008432','2025-02-22 22:23:20.564833',1,'cs_test_a1mRnOPAzajuZFlH03wtdMrjw7sAgq5rDYYqJDJoaINQmBa8VeUzgLKtls',NULL,NULL,NULL,NULL,NULL),(76,'PENDING',24.00,'2025-02-22 22:25:16.345950','2025-02-22 22:25:16.911775',1,'cs_test_a1VkyOtI9SrBJ5gnYDSdwpcrNfEokPuXXi5zrlTPMwAdRh9CPFq1IbXoEf',NULL,NULL,NULL,NULL,NULL),(77,'PENDING',26.00,'2025-02-22 22:30:53.649046','2025-02-22 22:30:54.201632',1,'cs_test_a1FGbzRUQLDcWQQ4A86qDFLdEO3eTrs1BPbMKeyJ7tErTsTTTzAxHvUdM4',NULL,NULL,NULL,NULL,NULL),(78,'PENDING',22.00,'2025-02-23 12:59:39.377035','2025-02-23 12:59:39.981540',1,'cs_test_a1QaSlQcLtDXnLvpOpoUgZWex1HMXRxalrzwvN0N9xb7HknjeSjrOikKPT',NULL,NULL,NULL,NULL,NULL),(79,'PENDING',24.00,'2025-02-23 13:01:55.938563','2025-02-23 13:01:56.514173',1,'cs_test_a1AUl3l6LvHeJLtzP622XgPCAix1HbybCiztF7B0acaVnYMxaBTH4mjqMG',NULL,NULL,NULL,NULL,NULL),(80,'PENDING',32.00,'2025-02-23 13:28:17.042865','2025-02-23 13:28:17.560733',1,'cs_test_a1mlQNs0FA51VwavKvvwhTKkRt9d8OqxHKnbLHKNWUel4KuuKYMvM830Zh',NULL,NULL,NULL,NULL,NULL),(81,'PAID',24.00,'2025-02-23 13:56:46.388452','2025-02-23 13:57:12.326778',1,'cs_test_a1P7X7OJMRwRHBzNlbq3lDIweXRDmG5KeY3q6tDdTd5ygQ2riMgWdDYiz1','12 Testard Road','Guildford','GB','brogan','GU2 4JT'),(82,'PAID',29.00,'2025-02-23 15:48:26.189745','2025-02-23 15:49:03.568211',1,'cs_test_a1IWlcF4jZ6S7rhAseRTTxYiX0tHwxW0bwuHS0OpFZWpwuJSsDZawMT0XB','123 Westbourne Road','Birmingham','GB','brogan','B21 8AU'),(83,'PENDING',32.00,'2025-02-23 15:57:20.584988','2025-02-23 15:57:21.194853',1,'cs_test_a17ituEV9EiNfBhR0ddqT7Jq4du4KNyr7Yad3sb70oZetB2fDQ3zRxKbAi',NULL,NULL,NULL,NULL,NULL),(84,'PENDING',26.00,'2025-02-23 15:58:33.348432','2025-02-23 15:58:33.994143',1,'cs_test_a1dhDfYa7eHkKsww72sNr5SfJ5z2w98flZvAUpYpyZQtXc4fVdEHOgKhWM',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `orders_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_orderitem`
--

DROP TABLE IF EXISTS `orders_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_orderitem_order_id_fe61a34d_fk_orders_order_id` (`order_id`),
  KEY `orders_orderitem_product_id_afe4254a_fk_products_product_id` (`product_id`),
  CONSTRAINT `orders_orderitem_order_id_fe61a34d_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`),
  CONSTRAINT `orders_orderitem_product_id_afe4254a_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`),
  CONSTRAINT `orders_orderitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_orderitem`
--

LOCK TABLES `orders_orderitem` WRITE;
/*!40000 ALTER TABLE `orders_orderitem` DISABLE KEYS */;
INSERT INTO `orders_orderitem` VALUES (20,1,22.00,62,2),(21,2,22.00,63,2),(22,1,42.00,64,12),(23,1,22.00,65,2),(24,1,42.00,65,12),(25,1,22.00,66,2),(26,1,42.00,66,12),(27,1,22.00,67,2),(28,1,22.00,68,2),(29,1,22.00,69,2),(30,3,22.00,70,2),(31,2,22.00,71,2),(32,1,22.00,72,2),(33,4,29.00,72,8),(34,1,26.00,73,3),(35,1,24.00,73,5),(36,1,22.00,74,2),(37,3,32.00,75,6),(38,1,44.00,75,7),(39,1,24.00,76,5),(40,1,26.00,77,4),(41,1,22.00,78,2),(42,1,24.00,79,5),(43,1,32.00,80,6),(44,1,24.00,81,5),(45,1,29.00,82,8),(46,1,32.00,83,6),(47,1,26.00,84,4);
/*!40000 ALTER TABLE `orders_orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_category`
--

DROP TABLE IF EXISTS `products_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_category`
--

LOCK TABLES `products_category` WRITE;
/*!40000 ALTER TABLE `products_category` DISABLE KEYS */;
INSERT INTO `products_category` VALUES (1,'Cleansers'),(5,'Gift Sets'),(4,'Masks'),(2,'Moisturisers'),(3,'Serums');
/*!40000 ALTER TABLE `products_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_product`
--

DROP TABLE IF EXISTS `products_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `description` longtext,
  `stock` int NOT NULL,
  `image_url` varchar(200) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `category_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_category` (`category_id`),
  CONSTRAINT `fk_category` FOREIGN KEY (`category_id`) REFERENCES `products_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_product`
--

LOCK TABLES `products_product` WRITE;
/*!40000 ALTER TABLE `products_product` DISABLE KEYS */;
INSERT INTO `products_product` VALUES (2,'Foam Face Cleanser',22.00,'A gentle, eco-friendly foaming cleanser that deeply cleanses without stripping moisture, perfect for sensitive skin.',10,'https://example.com/foamfacecleanser.jpg','2025-02-12 17:37:33.211201',1),(3,'Oil Face Cleanser',26.00,'A nourishing oil-based cleanser that dissolves makeup and impurities while maintaining skin’s natural balance.',10,'https://example.com/oilfacecleanser.jpg','2025-02-12 17:37:33.212895',1),(4,'Day Cream',26.00,'A lightweight, hydrating day cream infused with antioxidants for all-day moisture and protection.',10,'products/daycream.jpg','2025-02-12 17:37:33.212924',2),(5,'Night Cream',24.00,'A rich, replenishing night cream that deeply nourishes and restores skin overnight.',10,'products/nightcream.jpg','2025-02-12 17:37:33.212943',2),(6,'Vitamin C Serum',32.00,'A potent yet gentle vitamin C serum that brightens and evens skin tone while protecting against environmental stressors.',10,'products/vitc.jpg','2025-02-12 17:37:33.212959',3),(7,'Retinal Serum',44.00,'A high-performance retinal serum that smooths fine lines and enhances skin renewal without irritation.',10,'products/retinal.jpg','2025-02-12 17:37:33.212975',3),(8,'Hyaluronic Acid Serum',29.00,'A deeply hydrating serum that plumps and smooths skin with pure, eco-sourced hyaluronic acid.',10,'products/haserum.jpg','2025-02-12 17:37:33.212990',3),(9,'Clay Mask',28.00,'A purifying clay mask that detoxifies and refines pores without drying out sensitive skin.',10,'products/claymask.jpg','2025-02-12 17:37:33.213005',4),(10,'Hydration Mask',28.00,'An ultra-hydrating mask that replenishes moisture and soothes even the most sensitive skin.',10,'products/hydrationmask.jpg','2025-02-12 17:37:33.213020',4),(11,'The Starter Set',56.00,'A curated set of skincare essentials for a simple yet effective routine, perfect for beginners.',10,'products/thestarterset.jpg','2025-02-12 17:37:33.213035',5),(12,'Overnight Set',42.00,'A luxurious nighttime skincare set designed to hydrate, repair, and rejuvenate while you sleep.',10,'products/overnightset.jpg','2025-02-12 17:37:33.213049',5);
/*!40000 ALTER TABLE `products_product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-23 16:11:25
