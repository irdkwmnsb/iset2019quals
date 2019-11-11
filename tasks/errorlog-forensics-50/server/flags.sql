SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


CREATE TABLE `flags` (
  `id` int(11) NOT NULL,
  `flag` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `flags` (`id`, `flag`) VALUES
(1, '▄███████▀▀▀▀▀▀███████▄\r\n░▐████▀▒ЗАПУСКАЕМ▒▀██████▄\r\n░███▀▒▒▒▒▒ДЯДЮ▒▒▒▒▒▒▀█████\r\n░▐██▒▒▒▒▒▒БОГДАНА▒▒▒▒▒████▌\r\n░▐█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▌\r\n░░█▒▄▀▀▀▀▀▄▒▒▄▀▀▀▀▀▄▒▐███▌\r\n░░░▐░░░▄▄░░▌▐░░░▄▄░░▌▐███▌\r\n░▄▀▌░░░▀▀░░▌▐░░░▀▀░░▌▒▀▒█▌\r\n░▌▒▀▄░░░░▄▀▒▒▀▄░░░▄▀▒▒▄▀▒▌\r\n░▀▄▐▒▀▀▀▀▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒█\r\n░░░▀▌▒▄██▄▄▄▄████▄▒▒▒▒█▀\r\n░░░░▄██████████████▒▒▐▌\r\n░░░▀███▀▀████▀█████▀▒▌\r\n░░░░░▌▒▒▒▄▒▒▒▄▒▒▒▒▒▒▐\r\n░░░░░▌▒▒▒▒▀▀▀▒▒▒▒▒▒▒▐'),
(2, 'flag{uncl3_b0gd4n_p0luch1l_tr33t1y_d4n}'),
(3, 'FCVAR_REPLICATED'),
(4, 'FCVAR_SERVER_CAN_EXECUTE');


ALTER TABLE `flags`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `flags`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;