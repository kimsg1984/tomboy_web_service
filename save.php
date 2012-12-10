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

$edited_file = fopen("$edited_file_name", "w");
fwrite($edited_file,  $title_tag);  
fwrite($edited_file,  $content_tag);  
fclose($edited_file); 

$result1=shell_exec("python ./htmlparser.py $edited_file_name");
$notefile_sync=shell_exec("python ./notefile_sync.py $notefile");
$save=shell_exec("python ./save.py \"$edited_file_name.xml\" $notefile_sync");

echo "python ./htmlparser.py $edited_file_name.xml $notefile_sync <br>";
echo "notefile_sync : $notefile_sync<br>";

echo "$result1<br> $notefile_sync, <br> $save";





if ($save == "succeed\n"){
header("Location:./dylink.php?title=$title");
}lstat(filename)

else {
	echo $result;
}
	
echo 'test';
// unlink("$edited_file_name");
// unlink("$edited_file_name.xml");

shell_exec('python ./mklist.py > ./notefile/list.txt');

?>


  </div>


</body></html>

