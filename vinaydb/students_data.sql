-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 26, 2019 at 08:36 AM
-- Server version: 10.3.15-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `students_data`
--

CREATE TABLE `students_data` (
  `s.no` tinyint(2) NOT NULL,
  `id` varchar(8) NOT NULL,
  `name` varchar(40) NOT NULL,
  `branch` varchar(6) NOT NULL,
  `year` tinyint(4) NOT NULL,
  `phone` bigint(12) NOT NULL,
  `sport` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students_data`
--

INSERT INTO `students_data` (`s.no`, `id`, `name`, `branch`, `year`, `phone`, `sport`) VALUES
(9, 'me101', 'fff', 'mec', 1, 5, NULL),
(10, 'me401', 'vinay', 'mec', 4, 89997566, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students_data`
--
ALTER TABLE `students_data`
  ADD PRIMARY KEY (`s.no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students_data`
--
ALTER TABLE `students_data`
  MODIFY `s.no` tinyint(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
