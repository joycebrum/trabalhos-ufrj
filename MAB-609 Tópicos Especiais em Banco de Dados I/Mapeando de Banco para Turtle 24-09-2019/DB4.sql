-- phpMyAdmin SQL Dump
-- version 4.2.10
-- http://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Generation Time: May 10, 2016 at 08:47 PM
-- Server version: 5.5.38
-- PHP Version: 5.6.2
CREATE DATABASE DB4;
USE DB4;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `r2rml`
--

-- --------------------------------------------------------

--
-- Table structure for table `DEPT`
--

CREATE TABLE `DEPT` (
  `DEPTNO` int(11) NOT NULL,
  `DNAME` varchar(30) DEFAULT NULL,
  `LOC` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`DEPTNO`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `DEPT2`
--

INSERT INTO `DEPT` (`DEPTNO`, `DNAME`, `LOC`) VALUES
(10, 'APPSERVER', 'NEW YORK'),
(20, 'RESEARCH', 'BOSTON');

-- --------------------------------------------------------

--
-- Table structure for table `EMP`
--

CREATE TABLE `EMP` (
  `EMPNO` int(11) NOT NULL,
  `ENAME` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`EMPNO`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `EMP2`
--

INSERT INTO `EMP` (`EMPNO`, `ENAME`) VALUES
(7369, 'SMITH'),
(7400, 'JONES');

-- --------------------------------------------------------

--
-- Table structure for table `EMP2DEPT`
--

CREATE TABLE `EMP2DEPT` (
  `EMPNO` int(11) NOT NULL,
  `DEPTNO` int(11) NOT NULL,
  `JOB` varchar(20) DEFAULT NULL,
  FOREIGN KEY (`EMPNO`) references EMP(`EMPNO`),
  FOREIGN KEY (`DEPTNO`) references DEPT(`DEPTNO`),
  PRIMARY KEY (`EMPNO`, `DEPTNO`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `EMP2DEPT`
--

INSERT INTO `EMP2DEPT` (`EMPNO`, `DEPTNO`, `JOB`) VALUES
(7369, 10, 'CLERK'),
(7369, 20, 'NIGHTGUARD'),
(7400, 10, 'ENGINEER');