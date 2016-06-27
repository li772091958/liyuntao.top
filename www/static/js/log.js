AV.initialize('PsLiU3e6sAFkoOnaBRS1BThk-gzGzoHsz', 'WQ2jeDbbVWlEnAJ3iWymS4Px');
var TestObject = AV.Object.extend('Liyuntao_log');
var testObject = new TestObject();
var date = new Date();
var cip = returnCitySN.cip;
var cname = returnCitySN.cname;
var href = window.location.href;
testObject.save({
	date : date,
	cip : cip,
	cname : cname,
	href : href
},{
	success: function(object) {
		console.log('欢迎访问李云涛的个人网站！');
	}
});
