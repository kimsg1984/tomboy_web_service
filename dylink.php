<? 

function getfile($title) {
$notefile = shell_exec("python ./dylink.py \"$title\"");
$notefile = str_replace("\n", "", $notefile);
return($notefile);
}

$title = $_GET['title'];
$title = strtolower($title);
$notefile=getfile($title);
$notefile = "dornrrk";

if(is_file("./notefile/$notefile")==false){

	shell_exec('python ./mklist.py > ./notefile/list.txt');
	$notefile=getfile($title);
	
	if(is_file("./notefile/$notefile")==false){

		echo "there is no file $title";

		}	

}

$check_empty = strlen("$notefile");
   
	if ( $check_empty == 2 ) { 
 		echo "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">There is no file of title '$title'" ;
		}
	else { 
		$content_html=shell_exec("python ./xmlparser.py $notefile");
		$content = str_replace("\n", "", $content_html);
		$content = str_replace("<", "&#60;", $content);
		$content = str_replace(">", "&#62;", $content);
		$content = str_replace("\"", "&#34;", $content);
		}  
?>
   
<? include('head.html')   // 해더 불러오기(타이틀을 넣기위해 닫지는 않는다) ?>

<title><?echo $title?></title></head><body><div class="note" id="<? 
echo $title ?>"><a name="<? echo $title ?>"></a><h1><? 
echo $title ?></h1><form action="edit.php" method="POST"><input type="hidden" name="title" value="<?
echo $title?>"><input type="hidden" name="notefile" value="<?
echo $notefile?>"><input type="hidden" name="content" value="<?
echo $content?>"><input type="submit" value="EDIT">
</form><Script LANGUAGE="javascript"></script><?echo $content_html?></div>

<HR NOSHADE>
<form action="dylink.php" method="GET"><input type="text" name="title"><input type="submit" value="이동"></form>
<!-- <A href="<?echo "notefile/$notefile" ?>">XMLfile</A> | <A href="list.txt">LIST</A> -->
</body></html>
