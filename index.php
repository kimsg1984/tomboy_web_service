<html>
<head>
	 <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>Tomboy Main Page</title>
</head>

<body>

	<?php


	shell_exec('python ./mklist.py > ./notefile/list.txt');


	header("Location:./dylink.php?title=start");
           
	?>


</body>
