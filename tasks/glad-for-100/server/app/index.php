<?php
if (!isset($_SERVER['PHP_AUTH_USER'])) {
    header('WWW-Authenticate: Basic realm="Pensionniy Fond Rossii"');
    header('HTTP/1.0 401 Unauthorized');
    die('Access Denied');
} else {
    if($_SERVER['PHP_AUTH_USER'] == 'denis_petrov' && $_SERVER['PHP_AUTH_PW'] == 'yavaleratururururu'){
		if($_COOKIE["stas"] == 'opredelenno_ne_stas'){
			die('flag{gl4d_t00_s33_y0u_4g41n}');
		} else {
			die('Access Denied');
		}
	} else {
		die('Access Denied');
	}
}
?>