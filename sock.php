<?php
// where is the socket server?
$host="localhost";
$port = 8971;
// open a client connection
$sock = socket_create(AF_INET, SOCK_DGRAM, 0);
// Bind the socket to an address/port
$error = socket_bind($sock,$host, $port);
socket_connect( $sock, $host, $port );

socket_write($sock, $_POST['message'],strlen($_POST['message']));

// Close the client (child) socket

$input = socket_read($sock, 1024);
$input = trim($input);
// Close the master sockets
socket_close($sock);
echo $input;
?>