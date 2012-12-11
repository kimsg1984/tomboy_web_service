<html>
<head>
<? include('head.html');  

// title, notefile, content, meta_data
$title = $_POST['title'];
$title_tag = "<title>$title</title>";
$content = $_POST['content']; $meta_data = $_POST['meta_data'];
$content_tag = "$content <!--{meta_data} $meta_data";
$notefile = $_POST['notefile'];
$time = explode(" ", microtime());
$edited_file_name = "$time[0].edited_file.txt";
// $edited_file_name = "$title.edited_file.txt";

echo "title     : $title<br>";
echo "content  : $content<br>";
echo "notefile : $notefile<br>";


$edited_file = fopen("$edited_file_name", "w");
fwrite($edited_file,  $title_tag);  
fwrite($edited_file,  $content_tag);  
fclose($edited_file); 

$result1=shell_exec("python ./htmlparser.py $edited_file_name");
$notefile_sync=shell_exec("python ./notefile_sync.py $notefile");
$save=shell_exec("python ./save.py \"$edited_file_name.xml\" $notefile_sync");

echo "python ./htmlparser.py $edited_file_name -> $result1<br>";
echo "python ./notefile_sync.py $notefile -> $notefile_sync<br><br>";
echo "python ./save.py \"$edited_file_name.xml\" $notefile_sync -> $save";

if ($save == "succeed\n"){
	shell_exec('python ./mklist.py > ./notefile/list.txt');
	unlink("$edited_file_name");
	unlink("$edited_file_name.xml");
	// shell_exec("mv ./notefile/$notefile ./notefile/backup/$title$edited_file_name");
	// echo "mv ./notefile/$notefile ./notefile/backup/$title.$edited_file_name";
	// header("Location:./dylink.php?title=$title");


}


else {
	echo 'error';
}
	

?>


  </div>


</body></html>

