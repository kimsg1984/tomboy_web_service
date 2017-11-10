<html>
<head>
<?php 
include('head.html');  

if(isset($_POST['title'])) {
	$title = $_POST['title'];
	$title_tag = "<title>$title</title>";
} else { 
	$title = null;
	$title_tag = null;
}
if(isset($_POST['content'])) {
	$content = $_POST['content'];
} else {
	$content = null;
}
if(isset($_POST['meta_data'])) { 
	$meta_data = $_POST['meta_data'];
	$content_tag = "$content <!--{meta_data} $meta_data";
} else {
	$meta_data = null;
	$content_tag = null;
}
if(isset($_POST['notefile'])) { 
	$notefile = $_POST['notefile'];
} else {
	$notefile = null;
}
$time = explode(" ", microtime());
$edited_file_name = "$time[0].edited_file.txt";

$edited_file = fopen("$edited_file_name", "w");
fwrite($edited_file,  $title_tag);  
fwrite($edited_file,  $content_tag);  
fclose($edited_file); 

$result1=shell_exec("python ./htmlparser.py $edited_file_name");
$notefile_sync=shell_exec("python ./notefile_sync.py $notefile");
$save=shell_exec("python ./save.py \"$edited_file_name.xml\" $notefile_sync");

if ($save == "succeed\n"){
	shell_exec('python ./mklist.py > ./notefile/list.txt');
	unlink("$edited_file_name");
	unlink("$edited_file_name.xml");
	rename("./notefile/$notefile", "./notefile/backup/$title$edited_file_name");
	header("Location:./dylink.php?title=$title");


}


else {
	echo "title: " . $title . "<br>";
	echo "content: " . $content . "<br>";
	echo "notefile: " . $notefile . "<br>";
	echo "python ./htmlparser.py $edited_file_name -> $result1<br>";
	echo "python ./notefile_sync.py $notefile -> $notefile_sync<br><br>";
	echo "python ./save.py \"$edited_file_name.xml\" $notefile_sync -> $save<br>";
	echo '.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>error';
}


?>


  </div>


</body></html>
