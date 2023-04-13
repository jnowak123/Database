-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 30 Mar 2023, 11:40
-- Wersja serwera: 10.4.27-MariaDB
-- Wersja PHP: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `firma_kurierska`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auta`
--

CREATE TABLE `auta` (
  `nr_rejestracyjny` varchar(5) DEFAULT NULL,
  `marka` varchar(8) DEFAULT NULL,
  `model` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Zrzut danych tabeli `auta`
--

INSERT INTO `auta` (`nr_rejestracyjny`, `marka`, `model`) VALUES
('AA001', 'Citroen', 'Jumper'),
('AA002', 'Fiat', 'Ducato'),
('AA003', 'Citroen', 'Berlingo'),
('AA004', 'Ford', 'Transit'),
('AA005', 'Fiat', 'Ducato'),
('AA006', 'Iveco', 'Daily'),
('AA007', 'Ford', 'Transit'),
('AA008', 'Citroen', 'Jumper'),
('AA009', 'Mercedes', 'Vito'),
('AA010', 'Ford', 'Transit'),
('AA011', 'Citroen', 'Berlingo'),
('AA012', 'Fiat', 'Ducato'),
('AA013', 'Mercedes', 'Sprinter'),
('AA014', 'Citroen', 'Jumper'),
('AA015', 'Fiat', 'Ducato'),
('AA016', 'Mercedes', 'Vito'),
('AA017', 'Citroen', 'Berlingo'),
('AA018', 'Iveco', 'Daily'),
('AA019', 'Mercedes', 'Sprinter'),
('AA020', 'Citroen', 'Jumper'),
('AA021', 'Opel', 'Vivaro'),
('AA022', 'Mercedes', 'Sprinter'),
('AA023', 'Citroen', 'Berlingo'),
('AA024', 'Ford', 'Transit'),
('AA025', 'Iveco', 'Daily'),
('AA026', 'Mercedes', 'Sprinter'),
('AA027', 'Citroen', 'Jumper'),
('AA028', 'Fiat', 'Ducato'),
('AA029', 'Mercedes', 'Vito'),
('AA030', 'Ford', 'Transit');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `naprawy`
--

CREATE TABLE `naprawy` (
  `id_naprawy` varchar(3) DEFAULT NULL,
  `nazwa` varchar(36) DEFAULT NULL,
  `cena_materialow` int(4) DEFAULT NULL,
  `cena_roboczo_h` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Zrzut danych tabeli `naprawy`
--

INSERT INTO `naprawy` (`id_naprawy`, `nazwa`, `cena_materialow`, `cena_roboczo_h`) VALUES
('p1', 'wymiana klockow hamulcowych', 360, 80),
('p2', 'wymiana tarcz hamulcowych', 432, 80),
('p3', 'wymiana paska klinowego', 50, 35),
('p4', 'wymina amortyzatora', 400, 90),
('p5', 'wymiana koncowki drazka', 35, 45),
('p6', 'wymiana kola pasowego walu korbowego', 130, 85),
('p7', 'wymiana filtra paliwa', 190, 35),
('p8', 'wymiana filtra powietrza', 100, 30),
('p9', 'wymiana filtra oleju', 55, 30),
('p10', 'wymiana filtra kabinowego', 136, 45),
('p11', 'wymiana chlodnicy silnika', 680, 85),
('p12', 'wymiana sprezyny zawieszenia', 420, 95),
('p13', 'wymiana panewek walu korbowego', 690, 130),
('p14', 'wymiana wachaczy', 1000, 110),
('p15', 'wymiana swiec', 200, 70),
('p16', 'wymiana mechanizmu sprzegla ', 1900, 155),
('p17', 'wymiana kola zamachowego dwumasowego', 1800, 140),
('p18', 'wymiana pompy spryskiwacza', 100, 75),
('p19', 'wymiana linki gazu', 145, 46),
('p20', 'wymiana pompy paliwa', 650, 84),
('p21', 'wymiana lozyska kola', 505, 135),
('p22', 'wymiana resora', 605, 145);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `serwis`
--

CREATE TABLE `serwis` (
  `nr_rejestracyjny` varchar(5) DEFAULT NULL,
  `id_naprawy` varchar(3) DEFAULT NULL,
  `czasnaprawy` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Zrzut danych tabeli `serwis`
--

INSERT INTO `serwis` (`nr_rejestracyjny`, `id_naprawy`, `czasnaprawy`) VALUES
('AA001', 'p2', '02:46:00'),
('AA003', 'p9', '00:54:00'),
('AA004', 'p11', '02:30:00'),
('AA005', 'p6', '02:56:00'),
('AA006', 'p4', '02:47:00'),
('AA008', 'p16', '02:46:00'),
('AA009', 'p13', '02:43:00'),
('AA010', 'p4', '02:05:00'),
('AA011', 'p2', '01:45:00'),
('AA013', 'p5', '02:37:00'),
('AA014', 'p4', '00:41:00'),
('AA015', 'p15', '00:58:00'),
('AA016', 'p6', '01:19:00'),
('AA017', 'p3', '00:31:00'),
('AA019', 'p14', '02:12:00'),
('AA020', 'p1', '01:44:00'),
('AA021', 'p18', '00:31:00'),
('AA022', 'p7', '00:38:00'),
('AA024', 'p2', '02:25:00'),
('AA025', 'p6', '02:18:00'),
('AA026', 'p5', '02:15:00'),
('AA027', 'p11', '01:41:00'),
('AA028', 'p7', '00:34:00'),
('AA029', 'p4', '02:31:00'),
('AA019', 'p19', '00:37:00'),
('AA001', 'p19', '00:54:00'),
('AA005', 'p12', '02:04:00'),
('AA006', 'p8', '00:33:00'),
('AA007', 'p2', '01:59:00'),
('AA008', 'p2', '01:18:00'),
('AA009', 'p6', '01:20:00'),
('AA010', 'p5', '02:35:00'),
('AA011', 'p19', '01:07:00'),
('AA013', 'p8', '00:52:00'),
('AA014', 'p15', '00:55:00'),
('AA015', 'p18', '00:31:00'),
('AA016', 'p8', '00:45:00'),
('AA017', 'p15', '00:52:00'),
('AA018', 'p2', '02:41:00'),
('AA019', 'p16', '02:46:00'),
('AA020', 'p5', '01:26:00'),
('AA021', 'p19', '01:21:00'),
('AA022', 'p18', '01:01:00'),
('AA024', 'p10', '00:36:00'),
('AA025', 'p16', '02:32:00'),
('AA026', 'p6', '02:21:00'),
('AA027', 'p13', '01:38:00'),
('AA028', 'p4', '02:18:00'),
('AA029', 'p12', '01:42:00'),
('AA030', 'p5', '02:11:00'),
('AA001', 'p18', '01:07:00'),
('AA002', 'p8', '00:47:00'),
('AA003', 'p13', '01:43:00'),
('AA004', 'p1', '00:52:00'),
('AA005', 'p15', '00:37:00'),
('AA006', 'p2', '01:53:00'),
('AA007', 'p4', '02:26:00'),
('AA008', 'p18', '00:42:00'),
('AA009', 'p12', '02:20:00'),
('AA010', 'p3', '00:42:00'),
('AA011', 'p1', '01:28:00'),
('AA012', 'p14', '01:47:00'),
('AA013', 'p20', '01:37:00'),
('AA014', 'p11', '01:53:00'),
('AA015', 'p3', '00:59:00'),
('AA016', 'p2', '01:18:00'),
('AA017', 'p13', '02:12:00'),
('AA018', 'p15', '00:31:00'),
('AA019', 'p11', '02:13:00'),
('AA020', 'p7', '00:56:00'),
('AA021', 'p5', '01:21:00'),
('AA022', 'p2', '01:36:00'),
('AA019', 'p3', '00:23:00'),
('AA024', 'p22', '02:06:00'),
('AA025', 'p11', '01:54:00'),
('AA026', 'p20', '01:36:00'),
('AA027', 'p2', '02:03:00'),
('AA028', 'p22', '02:15:00'),
('AA029', 'p20', '01:32:00'),
('AA030', 'p15', '00:51:00'),
('AA001', 'p15', '00:45:00'),
('AA002', 'p19', '01:02:00'),
('AA003', 'p17', '02:42:00'),
('AA004', 'p21', '02:30:00'),
('AA005', 'p8', '00:50:00'),
('AA006', 'p8', '00:36:00'),
('AA007', 'p22', '02:39:00'),
('AA008', 'p7', '00:46:00'),
('AA009', 'p3', '00:37:00'),
('AA010', 'p6', '01:48:00'),
('AA011', 'p4', '02:52:00'),
('AA012', 'p13', '01:40:00'),
('AA013', 'p21', '02:41:00'),
('AA014', 'p22', '02:08:00'),
('AA015', 'p11', '00:58:00'),
('AA016', 'p10', '00:35:00'),
('AA017', 'p21', '00:38:00'),
('AA019', 'p3', '01:26:00'),
('AA019', 'p6', '02:49:00'),
('AA020', 'p13', '02:43:00'),
('AA021', 'p19', '01:13:00'),
('AA022', 'p13', '02:42:00'),
('AA019', 'p9', '01:08:00'),
('AA024', 'p13', '01:43:00'),
('AA025', 'p22', '02:50:00'),
('AA026', 'p22', '02:46:00'),
('AA027', 'p10', '00:43:00'),
('AA028', 'p19', '00:59:00'),
('AA029', 'p8', '00:36:00'),
('AA030', 'p5', '01:57:00'),
('AA001', 'p9', '01:00:00'),
('AA002', 'p14', '02:13:00'),
('AA003', 'p8', '00:27:00'),
('AA004', 'p5', '01:48:00'),
('AA005', 'p7', '00:43:00'),
('AA006', 'p5', '01:45:00'),
('AA007', 'p21', '02:21:00'),
('AA008', 'p4', '01:55:00'),
('AA009', 'p11', '02:06:00'),
('AA010', 'p12', '02:07:00'),
('AA019', 'p9', '00:41:00'),
('AA012', 'p8', '00:32:00'),
('AA013', 'p1', '01:21:00'),
('AA014', 'p3', '00:49:00'),
('AA015', 'p8', '00:49:00'),
('AA016', 'p2', '02:42:00'),
('AA017', 'p15', '00:32:00'),
('AA018', 'p9', '00:35:00'),
('AA019', 'p13', '02:50:00'),
('AA020', 'p10', '00:41:00'),
('AA021', 'p11', '01:40:00'),
('AA022', 'p7', '00:34:00'),
('AA019', 'p21', '02:24:00'),
('AA024', 'p2', '01:40:00'),
('AA025', 'p21', '02:50:00'),
('AA026', 'p12', '02:27:00'),
('AA027', 'p22', '02:22:00'),
('AA028', 'p17', '01:46:00'),
('AA029', 'p1', '00:48:00'),
('AA030', 'p6', '01:49:00'),
('AA001', 'p3', '00:59:00'),
('AA002', 'p1', '01:40:00'),
('AA003', 'p13', '01:50:00'),
('AA019', 'p9', '00:33:00'),
('AA005', 'p5', '01:55:00'),
('AA006', 'p18', '00:40:00'),
('AA007', 'p12', '02:59:00'),
('AA008', 'p17', '02:35:00'),
('AA009', 'p5', '01:57:00'),
('AA010', 'p11', '02:53:00'),
('AA011', 'p18', '00:57:00'),
('AA012', 'p17', '02:46:00'),
('AA013', 'p17', '02:49:00'),
('AA014', 'p8', '00:46:00'),
('AA015', 'p16', '02:03:00'),
('AA016', 'p18', '00:41:00'),
('AA017', 'p18', '00:39:00'),
('AA018', 'p4', '01:58:00'),
('AA019', 'p17', '02:13:00'),
('AA020', 'p5', '02:33:00'),
('AA021', 'p21', '02:10:00'),
('AA022', 'p21', '02:34:00'),
('AA019', 'p9', '00:57:00'),
('AA024', 'p12', '01:59:00'),
('AA025', 'p13', '02:13:00'),
('AA026', 'p17', '02:08:00'),
('AA027', 'p22', '01:53:00'),
('AA028', 'p9', '00:53:00'),
('AA029', 'p10', '00:42:00'),
('AA030', 'p1', '00:48:00');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
