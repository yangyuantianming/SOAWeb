SOAWeb
======

接口共有4个：

###/
	主页面，就是只有一个搜索框那个
	输入：无
	输出：无

###/search
	搜索页面，需要发送搜索query
	输入GET:
		query，字符串，表示要搜索的query
	输出：
		graph，搜索结果的链接图，json格式，详见example.py。点和边的属性待定。
		searchlist，搜索结果列表，json格式，详见example.py。属性应该不会有变化。

###/api/details
	Ajax接口，用于获取某个特定词项的Wiki详细信息
	输入：
		词项id，在searchlist中获得
	输出：
		retcode，成功与否标志
		details，json格式，详见example.py和潘寅旭发的文件。

###/api/related
	Ajax接口，用于用户点击图谱中某个点后返回其附近的信息
	输入：
		词项id
	输出：
		同search页面，2个json:graph和searchlist


