	<?
	 function RandStr($len){
	$return_str = "";

	for ( $i = 0; $i < $len; $i++ ) { 
	mt_srand((double)microtime()*1000000);
	$return_str .= substr('0123456789abcdefghijklmnopqrstuvwxyz', mt_rand(0,35), 1); 
	} 
	return $return_str;
	}
	$code1 = RandStr(8) ; 
	$code2 = RandStr(4) ;
	$code3 = RandStr(4) ;
	$code4 = RandStr(4) ;
	$code5 = RandStr(12) ;
	$notefile = "0/0/$code1-$code2-$code3-$code4-$code5.note";
	// echo "$notefile<br>";
	// header("Location:./edit.php?notefile=$notefile");

	if ($save == "succeed\n"){
		
	}




	?>

	<form action="edit.php" method="POST">
		<input type="hidden" name="title" value="">
		<input type="hidden" name="notefile" value="<?echo $notefile?>">
		<input type="hidden" name="content" value="">
		<script>document.form.submit();</script>
		<?header("Location:./edit.php");?>
	</form>

	</form>
	