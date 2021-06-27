function billingFunction(){
	checkBox = document.getElementById('same');
	if (checkBox.checked == true){
		document.getElementById('billingName').value = document.getElementById('shippingName').value;
		document.getElementById('billingZip').value = document.getElementById('shippingZip').value;
	}
	else{
		document.getElementById('billingName').value = '';
		document.getElementById('billingZip').value = '';
	}
}