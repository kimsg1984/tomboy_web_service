<html>
<head>
<? include('head.html'); 
$content=explode("<!--{meta_data}", $_POST['content']);
 ?>  <!-- 한글출력과 아이폰사이즈에 맞추기 위한 해더 삽입 -->
<script src="easyEditor.js"></script> <!-- 이지에디터 스크립트 파일 호출 -->
<script>
	function chkForm(f)
	{
		var content = ed.getHtml(); //대체한 textarea에 작성한HTML값 전달
		if(content=="")
		{
			alert("내용을 적어주세요!");
			ed.focus();
			return false;
		}
		// alert(content); //값확인(디버깅)
		return true;
	}



</script>
</head>
<body>
<pre>
</pre>
	<form  action="save.php" method="POST" onsubmit="chkForm(this)">
	<input type="text" name="title" Value="<?echo $_POST['title']?>">
	<input type="hidden" name="notefile" Value="<?echo $_POST['notefile']?>">
	<input type="hidden" name="meta_data" Value="<?echo $content[1]?>">
	<textarea name="content" id="content"><?echo $content[0]?></textarea>
	<input type="submit" value="저장">
	
	<!--  -->

	 <script>
		
	 	var ed = new easyEditor("content"); //초기화 id속성값
	 	//ed.cfg.width = "250px"; 
	 	//ed.cfg.height = "300px"; 
	 	ed.cfg.border = "1px dashed red";  
	 	ed.cfg.Btn = ["undo","bold","underline","strike","ul2"];
		ed.init(); //웹에디터 삽입
	 </script>
	
	<!--  -->

	</form>
</body>
</html>