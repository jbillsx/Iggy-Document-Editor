<?php
// where is the socket server?
$host="localhost";
$port = 8971;
// open a client connection
$sock = socket_create(AF_INET, SOCK_DGRAM, 0);
// Bind the socket to an address/port
$error = socket_bind($sock,$host, $port);
socket_connect( $sock, $host, $port );

socket_write($sock,"BLIP:NUMS:".$_POST['Docid']);

// Close the client (child) socket

$input = socket_read($sock, 1024);
$input = (int)$input;
$input++;
for($i=1;$i<=$input;$i++)
{
socket_write($sock,"BLIP:LIST:".$_POST['Docid']);
echo socket_read($sock, 1024).":";
}
// Close the master sockets
socket_close($sock);
?>