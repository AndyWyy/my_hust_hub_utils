function pay(){
	document.getElementById("qr").style.background = "gray";
	document.getElementById("qr").disabled = true;
	
	var password = $('#password').val();
	if(password == ''){
		document.getElementById("qr").style.background = "#18B2E7";
		document.getElementById("qr").disabled = false;
		alert('密码不能为空');
		return;
	}
	var aid = $('#select_app').val();
	var tranamt = $('#tranamt').val();
	if(tranamt <= 0){
		document.getElementById("qr").style.background = "#18B2E7";
		document.getElementById("qr").disabled = false;
		alert('金额错误');
		return;
	}
	var server_path = $('#server_path').val();
	var account = $('#cardno').val();
	var sno = $('#sno').val();
	netaccbean['netacc'] = sno;
	var areaUrl = 'http://' + server_path + '/wechat-web/networkpay/paynetgdc.html';
	var param = 'account=' + account + '&aid=' + aid + '&acctype='+$('#acctype').val()+'&tranamt=' + yuanToFen(tranamt) 
				+ '&Abstract=缴上网费' + '&netacc=' + JSON.stringify(netaccbean) + '&pkgflag=none&pkg=&password=' + password;

	commonAjax(areaUrl, param);
	if (isOk(contentList)) {
		alert('缴费成功');
		location.reload();
	} else {
		document.getElementById("qr").style.background = "#18B2E7";
		document.getElementById("qr").disabled = false;
		alert(contentList.errmsg);
	}
}