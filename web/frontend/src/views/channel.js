import React, { Component } from "react";

import Header from '../containers/Header'
import Footer from '../containers/Footer'

export default class Contact extends Component {
  render() {
    return (
      <div id="about">

       <Header />
    <div className="nav_path">

	    <div className="crumb">
	        <a href="/">首页</a><span>&gt;</span><a href="./channel.html">频道大全</a>
	    </div>
	</div>


    <div className="nav">

        <div className="navlist">
            <ul>
                <li><a href="./channel.html" className="nav_a nav_on">频道大全</a></li>
                <li><a href="./channel.html?keyword=CCTV" className="nav_a ">中央电视台</a></li>
                <li><a href="./channel.html?keyword=卫视" className="nav_a ">地方卫视台</a></li>
                <li><a href="./channel.html?keyword=港澳台" className="nav_a ">港澳台电视</a></li>
                <li><a href="./channel.html?keyword=外国" className="nav_a ">外国电视台</a></li>
                <li><a href="./channel.html?keyword=其他综合" className="nav_a ">其他综合台</a></li>
            </ul>
            <div className="search">
                <form name="search" id="search" method="get" action="./channel.html" onsubmit="return key_search();">
                    <div className="searchbox flexbox">
                        <input type="text" className="input-key" name="keyword" id="keyword" placeholder="关键字" />
                        <label><input type="submit" value="" className="btn-search" /><i className="fa fa-search" ></i></label>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <div className="container mt-15 clear">

        <div className="channel-index">
            <div className="filter clear">
                <div className="filter-title">
                    <h3>按地区查找</h3>
                </div>
                <div className="filter-list">
                    <ul>
                        <li><a href="./channel.html?keyword=央视">央视</a></li>
                        <li><a href="./channel.html?keyword=北京">北京</a></li>
                        <li><a href="./channel.html?keyword=上海">上海</a></li>
                        <li><a href="./channel.html?keyword=天津">天津</a></li>
                        <li><a href="./channel.html?keyword=重庆">重庆</a></li>
                        <li><a href="./channel.html?keyword=河北">河北</a></li>
                        <li><a href="./channel.html?keyword=山西">山西</a></li>
                        <li><a href="./channel.html?keyword=辽宁">辽宁</a></li>
                        <li><a href="./channel.html?keyword=吉林">吉林</a></li>
                        <li><a href="./channel.html?keyword=黑龙江">黑龙江</a></li>
                        <li><a href="./channel.html?keyword=江苏">江苏</a></li>
                        <li><a href="./channel.html?keyword=浙江">浙江</a></li>
                        <li><a href="./channel.html?keyword=安徽">安徽</a></li>
                        <li><a href="./channel.html?keyword=福建">福建</a></li>
                        <li><a href="./channel.html?keyword=江西">江西</a></li>
                        <li><a href="./channel.html?keyword=山东">山东</a></li>
                        <li><a href="./channel.html?keyword=河南">河南</a></li>
                        <li><a href="./channel.html?keyword=湖北">湖北</a></li>
                        <li><a href="./channel.html?keyword=湖南">湖南</a></li>
                        <li><a href="./channel.html?keyword=广东">广东</a></li>
                        <li><a href="./channel.html?keyword=海南">海南</a></li>
                        <li><a href="./channel.html?keyword=四川">四川</a></li>
                        <li><a href="./channel.html?keyword=贵州">贵州</a></li>
                        <li><a href="./channel.html?keyword=云南">云南</a></li>
                        <li><a href="./channel.html?keyword=陕西">陕西</a></li>
                        <li><a href="./channel.html?keyword=甘肃">甘肃</a></li>
                        <li><a href="./channel.html?keyword=青海">青海</a></li>
                        <li><a href="./channel.html?keyword=内蒙古">内蒙古</a></li>
                        <li><a href="./channel.html?keyword=广西">广西</a></li>
                        <li><a href="./channel.html?keyword=西藏">西藏</a></li>
                        <li><a href="./channel.html?keyword=宁夏">宁夏</a></li>
                        <li><a href="./channel.html?keyword=新疆">新疆</a></li>
                        <li><a href="./channel.html?keyword=xianggang">香港</a></li>
                        <li><a href="./channel.html?keyword=taiwan">台湾</a></li>
                        <li><a href="./channel.html?keyword=aomen">澳门</a></li>
                        <li><a href="./channel.html?keyword=korea">韩国</a></li>
                        <li><a href="./channel.html?keyword=japan">日本</a></li>
                        <li><a href="./channel.html?keyword=usa">美国</a></li>
                        <li><a href="./channel.html?keyword=england">英国</a></li>
                        <li><a href="./channel.html?keyword=northkorea">朝鲜</a></li>
                        <li><a href="./channel.html?keyword=russia">俄罗斯</a></li>
                        <li><a href="./channel.html?keyword=india">印度</a></li>
                        <li><a href="./channel.html?keyword=spain">西班牙</a></li>
                        <li><a href="./channel.html?keyword=singapore">新加坡</a></li>
                        <li><a href="./channel.html?keyword=thailand">泰国</a></li>
                        <li><a href="./channel.html?keyword=newzealand">新西兰</a></li>
                        <li><a href="./channel.html?keyword=Arab">阿拉伯</a></li>
                        <li><a href="./channel.html?keyword=Italy">意大利</a></li>
                        <li><a href="./channel.html?keyword=greece">希腊</a></li>
                        <li><a href="./channel.html?keyword=malaysia">马来西亚</a></li>
                        <li><a href="./channel.html?keyword=germany">德国</a></li>
                        <li><a href="./channel.html?keyword=france">法国</a></li>
                        <li><a href="./channel.html?keyword=vietnam">越南</a></li> -->
                    </ul>
                </div>
            </div>
            <div className="filter mt-15 clear">
                <div className="filter-title">
                    <h3>按类型查找</h3>
                </div>
                <div className="filter-list">
                    <ul>
                        <li><a href="./channel.html?keyword=卫视">卫视</a></li>
                        <li><a href="./channel.html?keyword=新闻">新闻</a></li>
                        <li><a href="./channel.html?keyword=影视">影视</a></li>
                        <li><a href="./channel.html?keyword=娱乐">娱乐</a></li>
                        <li><a href="./channel.html?keyword=体育">体育</a></li>
                        <li><a href="./channel.html?keyword=财经">财经</a></li>
                        <li><a href="./channel.html?keyword=健康">健康</a></li>
                        <li><a href="./channel.html?keyword=生活">生活</a></li>
                        <li><a href="./channel.html?keyword=儿童">儿童</a></li>
                        <li><a href="./channel.html?keyword=科教">科教</a></li>
                        <li><a href="./channel.html?keyword=军事">军事</a></li>
                        <li><a href="./channel.html?keyword=电影">电影</a></li>
                        <li><a href="./channel.html?keyword=音乐">音乐</a></li>
                        <li><a href="./channel.html?keyword=综合">综合</a></li>
                        <li><a href="./channel.html?keyword=记录">记录</a></li>
                        <li><a href="./channel.html?keyword=游戏">游戏</a></li>
                        <li><a href="./channel.html?keyword=农业">农业</a></li>
                        <li><a href="./channel.html?keyword=美食">美食</a></li>
                        <li><a href="./channel.html?keyword=探索">探索</a></li>
                        <li><a href="./channel.html?keyword=教育">教育</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div className="pannel mt-15 clear">
            <div className="row">
                <h3>频道列表</h3>
            </div>
            <div className="list-image clear">
                <ul>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="CEC汉语文化在线直播" href="http://www.freeiptv.cn/live/CECHanYu.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190226/b632ec8c329d9dde3e39e10482135f25.jpg"
                                  alt="CEC汉语文化在线直播" /></a>
                            <p className="title">CEC汉语文化</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="全国党员干部现代远程教育在线直播" href="http://www.freeiptv.cn/live/DangYuanEdu.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190226/3f3a4f630d2df5f40d05226e5f0ec913.jpg"
                                  alt="全国党员干部现代远程教育在线直播" /></a>
                            <p className="title">全国党员干部现代远程教育</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="印度ZOOM电视台在线直播" href="http://www.freeiptv.cn/live/YinDuZoom.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190226/58b7f73f5c0cc903b4ff8e9d43f36b5f.jpg"
                                  alt="印度ZOOM电视台在线直播" /></a>
                            <p className="title">印度ZOOM电视台</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="动物星球在线直播" href="http://www.freeiptv.cn/live/DongWuXingQiu.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190225/eee069ee94fa300288994e3040640b4e.jpg"
                                  alt="动物星球在线直播" /></a>
                            <p className="title">动物星球</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="流浪地球在线直播" href="http://www.freeiptv.cn/live/LiuLangDiQiu.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190211/992952c9aa3af7725eff72a0e9733482.jpg"
                                  alt="流浪地球在线直播" /></a>
                            <p className="title">流浪地球</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="Cinefil WOWOW在线直播" href="http://www.freeiptv.cn/live/CinefilWOWOW.html"><img src="./images/loading.gif"
                                  data-echo="/uploads/images/20190111/5a5d451487e46fa34cc36f709fab4347.jpg" alt="Cinefil WOWOW在线直播" /></a>
                            <p className="title">Cinefil WOWOW</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="韩国CBS电视台在线直播" href="http://www.freeiptv.cn/live/HGCBSTV.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190104/f5d9a6c0e804085ea4db5afa6b2def4d.jpg"
                                  alt="韩国CBS电视台在线直播" /></a>
                            <p className="title">韩国CBS电视台</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="CCTV老故事在线直播" href="http://www.freeiptv.cn/live/CCTVLaoGuShi.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190104/aa373c684243a56a4cf2c658e05e5055.jpg"
                                  alt="CCTV老故事在线直播" /></a>
                            <p className="title">CCTV老故事</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="ViuTV在线直播" href="http://www.freeiptv.cn/live/ViuTV.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190103/1ddc72e077ca122044173958a3991036.jpg"
                                  alt="ViuTV在线直播" /></a>
                            <p className="title">ViuTV</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="印度News X电视台在线直播" href="http://www.freeiptv.cn/live/NewsX.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190103/746eaa3a7137daf4d1c278f784cde924.jpg"
                                  alt="印度News X电视台在线直播" /></a>
                            <p className="title">印度News X电视台</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="TVB功夫台在线直播" href="http://www.freeiptv.cn/live/TVBKongFu.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190103/23ba79a90a969710f973cd5b546c84b2.jpg"
                                  alt="TVB功夫台在线直播" /></a>
                            <p className="title">TVB功夫台</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="高尔夫频道在线直播" href="http://www.freeiptv.cn/live/GDGaoErFU.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190103/7ebe3c39aa24100b9511d4625552ed38.jpg"
                                  alt="高尔夫频道在线直播" /></a>
                            <p className="title">高尔夫频道</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="朝日电视台在线直播" href="http://www.freeiptv.cn/live/TVAsahi.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190103/708412bf1ebab67d38c645dc6dd01e0d.png"
                                  alt="朝日电视台在线直播" /></a>
                            <p className="title">朝日电视台</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="新视觉高清频道在线直播" href="http://www.freeiptv.cn/live/XinShiJueHD.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190103/db9f92657cb2ffda50a97de544236caa.png"
                                  alt="新视觉高清频道在线直播" /></a>
                            <p className="title">新视觉高清频道</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="越南ANTV在线直播" href="http://www.freeiptv.cn/live/YNANTV.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190102/c381923609734a6258eba85c6eee3572.jpg"
                                  alt="越南ANTV在线直播" /></a>
                            <p className="title">越南ANTV</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="ATV越南在线直播" href="http://www.freeiptv.cn/live/ATVYN.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190101/69e8a474c01e673ebc3345e5bdd08e42.jpg"
                                  alt="ATV越南在线直播" /></a>
                            <p className="title">ATV越南</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="GongMax TV在线直播" href="http://www.freeiptv.cn/live/GongMaxTV.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190101/dfd5061ac5ef194e7b8463bb5f2aaa48.jpg"
                                  alt="GongMax TV在线直播" /></a>
                            <p className="title">GongMax TV</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="Gong TV在线直播" href="http://www.freeiptv.cn/live/GongTV.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190101/75a978380b352babd07615668ed128d9.jpg"
                                  alt="Gong TV在线直播" /></a>
                            <p className="title">Gong TV</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="日本映画Nihon Eiga TV在线直播" href="http://www.freeiptv.cn/live/NihonEigaTV.html"><img src="./images/loading.gif"
                                  data-echo="/uploads/images/20190101/3ffed15fac3a5ee60f95c55eead04837.jpg" alt="日本映画Nihon Eiga TV在线直播" /></a>
                            <p className="title">日本映画Nihon Eiga TV</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="东京电视台在线直播" href="http://www.freeiptv.cn/live/TVTOKYO.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190101/a1dce1e84103eb58d2d753ebbb1e11b6.jpg"
                                  alt="东京电视台在线直播" /></a>
                            <p className="title">东京电视台</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="法国时尚台FashionTV在线直播" href="http://www.freeiptv.cn/live/FashionTV.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190101/f6d8d77f91305a1eb159ffc5ffc5b1a7.jpg"
                                  alt="法国时尚台FashionTV在线直播" /></a>
                            <p className="title">法国时尚台FashionTV</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="韩国EBS1电视台在线直播" href="http://www.freeiptv.cn/live/EBSTV1.html"><img src="./images/loading.gif" data-echo="/uploads/images/20190101/e5ae44e963975a7106f3dd92fb9f0b62.jpg"
                                  alt="韩国EBS1电视台在线直播" /></a>
                            <p className="title">韩国EBS1电视台</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="垫江综合频道在线直播" href="http://www.freeiptv.cn/live/DianJiangZongHe.html"><img src="./images/loading.gif" data-echo="/uploads/images/20181128/d5e6f0a04a0e8d2a7df8bdbf8d216e04.jpg"
                                  alt="垫江综合频道在线直播" /></a>
                            <p className="title">垫江综合频道</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="天空新闻台SkyNews在线直播" href="http://www.freeiptv.cn/live/SkyNews.html"><img src="./images/loading.gif" data-echo="/uploads/images/20181128/4a41a5e973ef738834604e72638f1d9f.jpg"
                                  alt="天空新闻台SkyNews在线直播" /></a>
                            <p className="title">天空新闻台SkyNews</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="人间卫视在线直播" href="http://www.freeiptv.cn/live/RenJianWeiShi.html"><img src="./images/loading.gif" data-echo="/uploads/images/20181113/91926ebed1d08e43696de3872f9ae8d9.jpg"
                                  alt="人间卫视在线直播" /></a>
                            <p className="title">人间卫视</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="广州卫视在线直播" href="http://www.freeiptv.cn/live/GuangZhouWeiShi.html"><img src="./images/loading.gif" data-echo="/uploads/images/20181113/d85cd607d0710ed56fa585bf8d02d697.jpg"
                                  alt="广州卫视在线直播" /></a>
                            <p className="title">广州卫视</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="环球奇观频道在线直播" href="http://www.freeiptv.cn/live/HuanQiuQiGuan.html"><img src="./images/loading.gif" data-echo="/uploads/images/20181102/787bc59570299342d8c92243de3879e9.jpg"
                                  alt="环球奇观频道在线直播" /></a>
                            <p className="title">环球奇观频道</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="咸丰XFTV2在线直播" href="http://www.freeiptv.cn/live/XFTV2.html"><img src="./images/loading.gif" data-echo="/uploads/images/20181031/1b8b12b79decc0d16d3e6c5207c9495b.jpg"
                                  alt="咸丰XFTV2在线直播" /></a>
                            <p className="title">咸丰XFTV2</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="咸丰新闻综合频道在线直播" href="http://www.freeiptv.cn/live/XFTV1.html"><img src="./images/loading.gif" data-echo="/uploads/images/20181031/366b4966a5bd83efb6d553795948b9f0.jpg"
                                  alt="咸丰新闻综合频道在线直播" /></a>
                            <p className="title">咸丰新闻综合频道</p>
                        </div>
                    </li>
                    <li>
                        <div className="channel-item">
                            <a className="image" target="_blank" title="CHC动作电影在线直播" href="http://www.freeiptv.cn/live/CHCDongZuoDianYing.html"><img src="./images/loading.gif"
                                  data-echo="/uploads/images/20181031/dcc207da1d2149f23a8ff87cccf41f92.jpg" alt="CHC动作电影在线直播" /></a>
                            <p className="title">CHC动作电影</p>
                        </div>
                    </li>
                </ul>
            </div>
            <div className="pages clear">
                <strong>1</strong><a href="?p=2" data-ci-pagination-page="2">2</a><a href="?p=3" data-ci-pagination-page="3">3</a><a href="?p=2" data-ci-pagination-page="2" rel="next">下一页</a><a href="?p=16" data-ci-pagination-page="16">尾页</a>
            </div>
        </div>
    </div>

    <Footer />
</div>
    );
  }
}
