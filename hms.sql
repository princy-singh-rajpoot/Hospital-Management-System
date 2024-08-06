-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 06, 2024 at 10:03 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hms`
--

-- --------------------------------------------------------

--
-- Table structure for table `doctors`
--

CREATE TABLE `doctors` (
  `did` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `doctorname` varchar(50) NOT NULL,
  `dept` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctors`
--

INSERT INTO `doctors` (`did`, `email`, `doctorname`, `dept`) VALUES
(1, 't@gmail.com', 't', 'toilet'),
(2, 'r@gmail.com', 'gg', 'gobar'),
(4, 'drrana@gmail.com', 'dr. rana', 'darna'),
(5, 'princyvandanasingh@gmail.com', 'ggg', 'ggg');

-- --------------------------------------------------------

--
-- Table structure for table `patients`
--

CREATE TABLE `patients` (
  `pid` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `slot` varchar(50) NOT NULL,
  `disease` varchar(50) NOT NULL,
  `time` time(6) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `dept` varchar(50) NOT NULL,
  `number` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patients`
--

INSERT INTO `patients` (`pid`, `email`, `name`, `gender`, `slot`, `disease`, `time`, `date`, `dept`, `number`) VALUES
(1, 'q@gmail.com', 'q', 'male', 'morning', 'abc', '23:59:00.000000', '2024-12-31', 'toilet', '558445454'),
(5, 'q@gmail.com', 'qq', 'male', 'morning', 'qq', '23:59:00.000000', NULL, 'gobar', '1283753893'),
(6, 'q@gmail.com', 'qq', 'male', 'morning', 'qq', '23:59:00.000000', NULL, 'gobar', '1283753893'),
(7, 'q@gmail.com', 'qq', 'male', 'morning', 'qq', '23:59:00.000000', NULL, 'gobar', '1283753893'),
(8, 'q@gmail.com', 'qq', 'male', 'morning', 'qq', '23:59:00.000000', NULL, 'gobar', '6379254829'),
(9, 'q@gmail.com', 'qq', 'male', 'morning', 'qq', '23:59:00.000000', NULL, 'gobar', '6379254829'),
(10, 'q@gmail.com', 'qq', 'male', 'morning', 'qq', '23:59:00.000000', NULL, 'gobar', '6379254829'),
(16, 'princyvandanasingh@gmail.com', 'dateupdated', 'male', 'morning', 'date update testing', '23:59:00.000000', '2024-12-31', 'toilet', '07757827359');

--
-- Triggers `patients`
--
DELIMITER $$
CREATE TRIGGER `PatientInserted` AFTER INSERT ON `patients` FOR EACH ROW insert into trigr VALUES(null , NEW.pid, NEW.email, NEW.name, 'PATIENT INSERTED', NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `PatientUpdate` AFTER UPDATE ON `patients` FOR EACH ROW insert into trigr VALUES(null , NEW.pid, NEW.email, NEW.name, 'PATIENT UPDATED', NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `PatientdDeleted` BEFORE DELETE ON `patients` FOR EACH ROW insert into trigr VALUES(null , OLD.pid, OLD.email, OLD.name, 'PATIENT DELETED', NOW())
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `trigr`
--

CREATE TABLE `trigr` (
  `tid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `action` varchar(50) NOT NULL,
  `timestamp` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `trigr`
--

INSERT INTO `trigr` (`tid`, `pid`, `email`, `name`, `action`, `timestamp`) VALUES
(1, 15, 'princyvandanasingh@gmail.com', 'pp', 'PATIENT INSERTED', '2024-08-06 02:55:41'),
(2, 15, 'princyvandanasingh@gmail.com', 'pp', 'PATIENT UPDATED', '2024-08-06 02:59:06'),
(3, 12, 'princyvandanasingh@gmail.com', 'princy', 'PATIENT UPDATED', '2024-08-06 02:59:32'),
(4, 16, 'princyvandanasingh@gmail.com', 'd', 'PATIENT INSERTED', '2024-08-06 03:01:11'),
(5, 16, 'princyvandanasingh@gmail.com', 'dateupdated', 'PATIENT UPDATED', '2024-08-06 03:01:37'),
(6, 11, 'princyvandanasingh@gmail.com', 'princy', 'PATIENT DELETED', '2024-08-06 03:04:29'),
(7, 12, 'princyvandanasingh@gmail.com', 'princy', 'PATIENT DELETED', '2024-08-06 03:04:32'),
(8, 13, 'princyvandanasingh@gmail.com', 'princy', 'PATIENT DELETED', '2024-08-06 03:04:32'),
(9, 15, 'princyvandanasingh@gmail.com', 'pp', 'PATIENT DELETED', '2024-08-06 03:04:33');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
(1, 't', 't@gmail.com', 'scrypt:32768:8:1$QpXRIzMFYVi6ZApP$f90ce7cd99d0c41b76c1e09bc984c4c2c62246c33e2d53be016921416107b42b7e3183a7461ea52b10159f00b2bbedab02d4be365743793e0bb5fe650fd15daa'),
(2, 'q', 'q@gmail.com', 'scrypt:32768:8:1$MgvEl50plIdDEAVc$954e043e6903ca172227589fc454c688f23a105aef322d0b5bf9875f9fdcb1ff723ebb9efa01b8c103401ab5fd8287ed2384e3d2872ccb37d3143c21ea322ec5'),
(3, 'p', 'princyvandanasingh@gmail.com', 'scrypt:32768:8:1$WxQW1DVSC4yAWeJJ$bd3302238c08e47a205d8a82c837d21df90ae8687174612ba145585907672324dd0c294658f469d06d7bd0ed5af8a7a8dba3ae7897ebdfa6d060c5ab697e9ca8');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `doctors`
--
ALTER TABLE `doctors`
  ADD PRIMARY KEY (`did`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `trigr`
--
ALTER TABLE `trigr`
  ADD PRIMARY KEY (`tid`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `doctors`
--
ALTER TABLE `doctors`
  MODIFY `did` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `patients`
--
ALTER TABLE `patients`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `trigr`
--
ALTER TABLE `trigr`
  MODIFY `tid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
