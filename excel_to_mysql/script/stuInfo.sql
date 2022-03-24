/*
Navicat MariaDB Data Transfer

Source Server         : localhost_3306
Source Server Version : 100120
Source Host           : localhost:3306
Source Database       : stuinfo

Date: 2021-05-11 15:35:26
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS=0;


-- ----------------------------
-- Table structure for three_three
-- ----------------------------
DROP TABLE IF EXISTS `three_three`;
CREATE TABLE `three_three` (
	`stu_no` varchar(40) NOT NULL,
	`username` varchar(40) NOT NULL,
	`Chinese_score` decimal(10,2) DEFAULT NULL,
	`English_score` decimal(10,2) DEFAULT NULL,
	`Math_score` decimal(10,2) DEFAULT NULL,
	`gender` varchar(40) DEFAULT NULL,
	`create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`stu_no`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
