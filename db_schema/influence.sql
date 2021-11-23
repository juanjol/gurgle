-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 23-11-2021 a las 01:01:25
-- Versión del servidor: 10.3.29-MariaDB
-- Versión de PHP: 7.3.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `abde`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `influence`
--

CREATE TABLE IF NOT EXISTS `influence` (
  `Timestamp` datetime NOT NULL,
  `EventDate` date NOT NULL,
  `EventTime` time NOT NULL,
  `StarSystem` varchar(150) NOT NULL,
  `Distance` float NOT NULL,
  `SystemSecurity` text DEFAULT NULL,
  `SystemAllegiance` text DEFAULT NULL,
  `SystemGovernment` text DEFAULT NULL,
  `SystemEconomy` text DEFAULT NULL,
  `SystemFaction` text DEFAULT NULL,
  `Faction1Name` text DEFAULT NULL,
  `Faction1Influence` double DEFAULT NULL,
  `Faction1State` text DEFAULT NULL,
  `Faction1PendingState` text DEFAULT NULL,
  `Faction1RecoveringState` text DEFAULT NULL,
  `Faction2Name` text DEFAULT NULL,
  `Faction2Influence` float DEFAULT NULL,
  `Faction2State` text DEFAULT NULL,
  `Faction2PendingState` text DEFAULT NULL,
  `Faction2RecoveringState` text DEFAULT NULL,
  `Faction3Name` text DEFAULT NULL,
  `Faction3Influence` float DEFAULT NULL,
  `Faction3State` text DEFAULT NULL,
  `Faction3PendingState` text DEFAULT NULL,
  `Faction3RecoveringState` text DEFAULT NULL,
  `Faction4Name` text DEFAULT NULL,
  `Faction4Influence` float DEFAULT NULL,
  `Faction4State` text DEFAULT NULL,
  `Faction4PendingState` text DEFAULT NULL,
  `Faction4RecoveringState` text DEFAULT NULL,
  `Faction5Name` text DEFAULT NULL,
  `Faction5Influence` float DEFAULT NULL,
  `Faction5State` text DEFAULT NULL,
  `Faction5PendingState` text DEFAULT NULL,
  `Faction5RecoveringState` text DEFAULT NULL,
  `Faction6Name` text DEFAULT NULL,
  `Faction6Influence` text DEFAULT NULL,
  `Faction6State` text DEFAULT NULL,
  `Faction6PendingState` text DEFAULT NULL,
  `Faction6RecoveringState` text DEFAULT NULL,
  `Faction7Name` text DEFAULT NULL,
  `Faction7Influence` float DEFAULT NULL,
  `Faction7State` text DEFAULT NULL,
  `Faction7PendingState` text DEFAULT NULL,
  `Faction7RecoveringState` text DEFAULT NULL,
  `Faction8Name` text DEFAULT NULL,
  `Faction8Influence` float DEFAULT NULL,
  `Faction8State` text DEFAULT NULL,
  `Faction8PendingState` text DEFAULT NULL,
  `Faction8RecoveringState` text DEFAULT NULL,
  `Faction9Name` text DEFAULT NULL,
  `Faction9Influence` text DEFAULT NULL,
  `Faction9State` text DEFAULT NULL,
  `Faction9PendingState` text DEFAULT NULL,
  `Faction9RecoveringState` text DEFAULT NULL,
  `Faction10Name` text DEFAULT NULL,
  `Faction10Influence` float DEFAULT NULL,
  `Faction10State` text DEFAULT NULL,
  `Faction10PendingState` text DEFAULT NULL,
  `Faction10RecoveringState` text DEFAULT NULL,
  PRIMARY KEY (`EventDate`,`EventTime`,`StarSystem`),
  UNIQUE KEY `EventDate` (`EventDate`,`EventTime`,`StarSystem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
