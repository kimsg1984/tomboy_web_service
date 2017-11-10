<html>
<head>
<?php

	include('head.html'); 
	function RandStr($len){
		$return_str = "";
		for ( $i = 0; $i < $len; $i++ ) { 
			mt_srand((double)microtime()*1000000);
			$return_str .= substr('0123456789abcdefghijklmnopqrstuvwxyz', mt_rand(0,35), 1); 
		} 
		return $return_str;
	}
	function mknotefile(){
		$code1 = RandStr(8) ; 
		$code2 = RandStr(4) ;
		$code3 = RandStr(4) ;
		$code4 = RandStr(4) ;
		$code5 = RandStr(12) ;
		$notefile = "0/0/$code1-$code2-$code3-$code4-$code5.note";
		return $notefile;
	}

	if(isset($_POST['notefile'])) { 
		$notefile=$_POST['notefile'];
	} else {
		$notefile=null;
	}
	$check_empty = strlen("$notefile");
   	   	
	if ( $check_empty != 0 ) { 
 		$title = $_POST['title'];
		$content=explode("<!--{meta_data}", $_POST['content']);
		}
	else { 
		
		$title = "";
		$notefile=mknotefile();
		$content="<!--{meta_data}{/meta_data}-->";
		$content=explode("<!--{meta_data}", $content);

		}  




 ?>  <!-- Insert header for matching Hangul output and iPhone size -->
<script src="easyEditor.js"></script> <!-- Calling the image editor script file -->
<script>
	function chkForm(f)
	{
		var content = ed.getHtml(); // Pass the HTML value you wrote to the alternate textarea
		if(content=="")
		{
			alert("내용을 적어주세요!");
			ed.focus();
			return false;
		}
		// alert(content); // Verifying values (debugging)
		return true;
	}



</script>
</head>
<body>
<pre>
</pre>
	<form  action="save.php" method="POST" onsubmit="chkForm(this)">
	<input type="text" name="title" Value="<?php echo $title ?>">
	<input type="hidden" name="notefile" Value="<?php echo $notefile ?>">
	<input type="hidden" name="meta_data" Value="<?php echo $content[1] ?>">
	<textarea name="content" id="content"><?php echo $content[0] ?></textarea>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="저장">
	
	<!--  -->

	 <script>
		
	 	var ed = new easyEditor("content"); // Initialization id attribute value
	 	//ed.cfg.width = "250px"; 
	 	//ed.cfg.height = "300px"; 
	 	ed.cfg.border = "1px dashed red";  
	 	ed.cfg.Btn = ["undo","bold","underline","strike","ul2"];
		ed.init(); // Insert web editor
	 </script>
	
	<!--  -->

	</form>
</body>
</html>
