/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - find_my_bus
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`find_my_bus` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `find_my_bus`;

/*Table structure for table `buses` */

DROP TABLE IF EXISTS `buses`;

CREATE TABLE `buses` (
  `bus_id` int(11) NOT NULL AUTO_INCREMENT,
  `bus_name` varchar(50) DEFAULT NULL,
  `reg_number` varchar(50) DEFAULT NULL,
  `noofseats` int(10) DEFAULT NULL,
  PRIMARY KEY (`bus_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `buses` */

insert  into `buses`(`bus_id`,`bus_name`,`reg_number`,`noofseats`) values (10,'Sreelakshmi','KL-3720',55),(11,'Jeeva','kL-5625',45),(12,'Roseland','KL-5648',50);

/*Table structure for table `buslocation` */

DROP TABLE IF EXISTS `buslocation`;

CREATE TABLE `buslocation` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `bus_id` int(11) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  `datetime` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `buslocation` */

insert  into `buslocation`(`location_id`,`bus_id`,`latitude`,`longitude`,`datetime`) values (2,5,'9.97632086277008','76.28620326519012','2020-01-11 00:00:00'),(3,7,'0','0','2020-01-12 00:00:00'),(4,8,'0','0','2021-01-19'),(5,9,'0','0','2021-01-19'),(6,10,'0','0','2022-02-09'),(7,11,'0','0','2022-02-09'),(8,12,'0','0','2022-02-09');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `reply` varchar(500) DEFAULT NULL,
  `complaint_date` date DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`user_id`,`description`,`reply`,`complaint_date`) values (1,1,'test','sfg','2020-01-03'),(2,2,'Hdhhd','NA','2020-01-11');

/*Table structure for table `conductor` */

DROP TABLE IF EXISTS `conductor`;

CREATE TABLE `conductor` (
  `conductor_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_id` int(11) DEFAULT NULL,
  `bus_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `age` varchar(20) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`conductor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `conductor` */

insert  into `conductor`(`conductor_id`,`log_id`,`bus_id`,`fname`,`lname`,`age`,`phone`) values (1,4,4,'jj','jj','30','8767888767'),(2,5,5,'pp','pp','55','9876678998'),(3,7,7,'hjgv','jb','33','2345555555'),(4,8,10,'jj','jjj','23','8988888888');

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `age` varchar(20) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`user_id`,`log_id`,`first_name`,`last_name`,`age`,`gender`,`phone`,`email`) values (1,2,'Anjana','Bose','24','female','8958476123','anju@gmail.com'),(2,3,'Jsh','Xhx','25','Male','8527419856','hshs@did.djd');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`log_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'anju','anju','customer'),(3,'Kk','kk','customer'),(5,'po','po','conductor'),(6,'ok','ok','conductor'),(7,'pp','pp','conductor'),(8,'kk','kks','conductor');

/*Table structure for table `otherplaces` */

DROP TABLE IF EXISTS `otherplaces`;

CREATE TABLE `otherplaces` (
  `other_place_id` int(11) NOT NULL AUTO_INCREMENT,
  `other_places_name` varchar(50) DEFAULT NULL,
  `other_places_type` varchar(50) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`other_place_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `otherplaces` */

insert  into `otherplaces`(`other_place_id`,`other_places_name`,`other_places_type`,`latitude`,`longitude`) values (2,'haripad','abc','9.986348845905287','76.27498626708984'),(3,'cdc ',' cnkkmx','9.983047950720747','76.27773661370402'),(5,'Muvattupuzha','jhkjhk','9.97812998958572','76.29275221697999'),(6,'kalampoor','dsgfdh','9.968012687551948','76.29506964556886');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `reservation_id` int(11) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`reservation_id`,`amount`,`payment_date`) values (1,2,'360','2020-01-13');

/*Table structure for table `places` */

DROP TABLE IF EXISTS `places`;

CREATE TABLE `places` (
  `place_id` int(11) NOT NULL AUTO_INCREMENT,
  `place_name` varchar(50) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`place_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `places` */

insert  into `places`(`place_id`,`place_name`,`latitude`,`longitude`) values (1,'Ernakulam','9.988293036447752','76.28811836242676'),(5,'Muvattupuzha','9.984141313749737','76.56796263187286'),(6,'Vannapuram','9.99156368501386','76.78223937341878');

/*Table structure for table `rate` */

DROP TABLE IF EXISTS `rate`;

CREATE TABLE `rate` (
  `rate_id` int(11) NOT NULL AUTO_INCREMENT,
  `mincharge` varchar(100) DEFAULT NULL,
  `stage_charge` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rate_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `rate` */

insert  into `rate`(`rate_id`,`mincharge`,`stage_charge`,`date`) values (1,'10','2','2020-09-13');

/*Table structure for table `reservations` */

DROP TABLE IF EXISTS `reservations`;

CREATE TABLE `reservations` (
  `reservation_id` int(11) NOT NULL AUTO_INCREMENT,
  `no_of_seats` varchar(50) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `trip_id` int(11) DEFAULT NULL,
  `from_place_id` int(11) DEFAULT NULL,
  `to_place_id` int(11) DEFAULT NULL,
  `reservation_amount` varchar(50) DEFAULT NULL,
  `reservation_status` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `qrcode` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`reservation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `reservations` */

insert  into `reservations`(`reservation_id`,`no_of_seats`,`user_id`,`trip_id`,`from_place_id`,`to_place_id`,`reservation_amount`,`reservation_status`,`date`,`qrcode`) values (1,'2',1,1,1,1,'600','wefj','01/01/2020',NULL),(2,'12',2,2,1,2,'360','Payed','13-01-2020',NULL),(3,'2',1,2,1,2,'60','pending','13-01-2020',NULL),(4,'3',2,2,2,1,'90','Payed','13-01-2020',NULL),(5,'2',1,6,1,2,'40','pending','19-01-2021',NULL),(6,'2',1,6,1,2,'40','pending','19-01-2021',NULL),(7,'12',1,6,4,1,'120','pending','08-02-2022',NULL),(8,'1',1,8,5,1,'68','pending','09-02-2022',''),(9,'1',1,8,5,1,'68','pending','09-02-2022',''),(10,'1',1,8,5,1,'67','pending','09-02-2022','static/qrcode/6d437549-006c-4481-a518-d5b400f9cc2b.png');

/*Table structure for table `routes` */

DROP TABLE IF EXISTS `routes`;

CREATE TABLE `routes` (
  `route_id` int(11) NOT NULL AUTO_INCREMENT,
  `route_name` varchar(50) DEFAULT NULL,
  `splace_id` int(11) DEFAULT NULL,
  `eplace_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`route_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `routes` */

insert  into `routes`(`route_id`,`route_name`,`splace_id`,`eplace_id`) values (2,'kollam',1,2),(3,'Eranakulam-Thrissur',1,2),(5,'Ernakulam',5,1),(6,'Vannapuram',5,6);

/*Table structure for table `stops` */

DROP TABLE IF EXISTS `stops`;

CREATE TABLE `stops` (
  `stop_id` int(11) NOT NULL AUTO_INCREMENT,
  `trip_id` int(11) DEFAULT NULL,
  `place_id` int(11) DEFAULT NULL,
  `stopnum` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`stop_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `stops` */

insert  into `stops`(`stop_id`,`trip_id`,`place_id`,`stopnum`) values (1,6,1,'1'),(2,6,2,'8'),(3,6,3,'3'),(4,7,1,'1'),(5,7,2,'5'),(6,8,5,'1'),(7,8,1,'32');

/*Table structure for table `trips` */

DROP TABLE IF EXISTS `trips`;

CREATE TABLE `trips` (
  `trip_id` int(11) NOT NULL AUTO_INCREMENT,
  `bus_id` int(11) DEFAULT NULL,
  `route_id` int(11) DEFAULT NULL,
  `stime` varchar(50) DEFAULT NULL,
  `etime` varchar(50) DEFAULT NULL,
  `stops` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`trip_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `trips` */

insert  into `trips`(`trip_id`,`bus_id`,`route_id`,`stime`,`etime`,`stops`) values (1,2,1,'07:00:00','22:00:00',NULL),(2,5,1,'06:00:00','17:00:00',NULL),(3,2,1,'12:00','13:00',NULL),(5,7,1,'09:00','11:00','6'),(6,7,1,'09:00','11:00','6'),(8,10,5,'14:00','17:00','30');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
