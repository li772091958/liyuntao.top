$("input[name='submit']").click(function(){
	AV.initialize('PsLiU3e6sAFkoOnaBRS1BThk-gzGzoHsz', 'WQ2jeDbbVWlEnAJ3iWymS4Px');
	var TestObject = AV.Object.extend('Liyuntao_message');
	var testObject = new TestObject();
	var name = $("#Name").val();
	var email = $("#Email").val();
	var message = $("#Message").val();
	testObject.save({
		name : name,
		email : email,
		message : message,
		cip : returnCitySN.cip,
		cname : returnCitySN.cname
	},{
		success: function(object) {
			alert('留言成功，我会及时查看并予以回复！');
		}
	});
})
