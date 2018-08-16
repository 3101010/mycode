/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50640
Source Host           : localhost:3306
Source Database       : sjcj

Target Server Type    : MYSQL
Target Server Version : 50640
File Encoding         : 65001

Date: 2018-05-22 22:55:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for news
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `标题` varchar(500) DEFAULT NULL,
  `日期` varchar(30) DEFAULT NULL,
  `内容` text,
  `URL` varchar(255) DEFAULT NULL,
  `来源` varchar(50) DEFAULT NULL,
  `采集时间` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `URL` (`URL`)
) ENGINE=InnoDB AUTO_INCREMENT=9335 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of news
-- ----------------------------
