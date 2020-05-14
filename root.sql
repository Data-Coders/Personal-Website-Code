-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 14, 2020 at 07:02 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `root`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(11) NOT NULL,
  `msg` text NOT NULL,
  `phno` varchar(15) NOT NULL,
  `name` text NOT NULL,
  `last` text NOT NULL,
  `email` varchar(25) NOT NULL,
  `subject` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `month` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `msg`, `phno`, `name`, `last`, `email`, `subject`, `date`, `month`) VALUES
(1, 'This is Alex Mercer', '8586047520', 'Alex', 'Mercer', 'alexmercerr07@gmail.com', 'Test', '2020-05-06 14:55:16', 'May'),
(2, 'gpijkbgdijopgbdpijdpijdgbpijdgbpijdgbopijdgbijopdgbopijdgbopijdfijopfdbijopfopij', '8586047520', 'Alexx', 'Mercerr', 'alexmercerr07@outlook.com', 'Test2', '0000-00-00 00:00:00', NULL),
(3, 'kjsadfljkhsdfkjbsdkjfbsdkjfbskjdbfksjdbfkjhsbdvfkjchbskjdbkjsdbfkjbdkjfbkjsdbfkjsbdkcbjbnsdjcnb', '8586047520', 'Alex', 'Mercer', 'alexmercerr07@outlook.com', 'Test3', '0000-00-00 00:00:00', NULL),
(4, 'sdfkjbasdfijhasdfuhjgasdjkgbf', '9935668258', 'Kumud', 'Ojha', 'som.kumud@gmail.com', 'Paper Kab Hoga', '0000-00-00 00:00:00', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` varchar(10000) NOT NULL,
  `img_file` varchar(12) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `posted` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `slug`, `content`, `img_file`, `date`, `posted`) VALUES
(1, 'First Blog Post', 'first-post', 'This is my First Blog Post While Creating this website back-end with the Python Framework named as Flask', 'finance.jpg', '2020-05-07 12:19:05', 'Admin'),
(2, 'This is the Second Post', 'second-post', 'This the second post for this Website through Backend', '', '2020-05-07 14:07:21', 'Admin'),
(3, 'Entering Via FrontEnd', 'admin-post', 'Entering Via FrontEnd', 'aman.png', '2020-05-12 00:19:41', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
