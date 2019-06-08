import React, { Component } from "react";
import queryString from 'query-string';

import Header from '../components/Header'
import Footer from '../components/Footer'

import ChannelsPage from '../components/channel/ChannelsPage'

import {fetchChannels } from '../actions';


import '../stylesheets/channel.css'
import {connect} from "react-redux";




class Channels extends Component {

    componentDidMount() {

        //console.log(this.props.location.search);
        const parsed = queryString.parse(this.props.location.search);
        console.log(parsed.keyword);

        this.props.dispatch(fetchChannels(parsed.keyword));
    }


    render() {
        return (
            <div id="channel">
                <Header />
                <div className="nav_path">
                    <div className="crumb">
                        <a href="/">首页</a><span>></span><a href="./channel">频道大全</a>
                    </div>
                </div>
                <div className="nav">
                    <div className="navlist">
                        <ul>
                            <li>
                                <a href="./channels" className="nav_a nav_on">频道大全</a>
                            </li>
                            <li>
                                <a href="./channels?keyword=CCTV" className="nav_a ">中央电视台</a>
                            </li>
                            <li>
                                <a href="./channels?keyword=卫视" className="nav_a ">地方卫视台</a>
                            </li>
                            <li>
                                <a href="./channels?keyword=港澳台" className="nav_a ">港澳台电视</a>
                            </li>
                            <li>
                                <a href="./channels?keyword=外国" className="nav_a ">外国电视台</a>
                            </li>
                            <li>
                                <a href="./channels?keyword=其他综合" className="nav_a ">其他综合台</a>
                            </li>
                        </ul>
                        <div className="search">
                            <form name="search"
                                id="search"
                                method="get"
                                action="./channel"
                                onSubmit="return key_search();">
                                <div className="searchbox flexbox">
                                    <input type="text"
                                        className="input-key"
                                        name="keyword"
                                        id="keyword"
                                        placeholder="关键字" />
                                    <label>
                                        <input type="submit" value="" className="btn-search" /><i className="fa fa-search"></i>
                                    </label>
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
                                    <li>
                                        <a href="./channels?keyword=CCTV">央视</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=北京">北京</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=上海">上海</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=天津">天津</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=重庆">重庆</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=河北">河北</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=山西">山西</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=辽宁">辽宁</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=吉林">吉林</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=黑龙江">黑龙江</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=江苏">江苏</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=浙江">浙江</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=安徽">安徽</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=福建">福建</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=江西">江西</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=山东">山东</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=河南">河南</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=湖北">湖北</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=湖南">湖南</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=广东">广东</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=海南">海南</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=四川">四川</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=贵州">贵州</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=云南">云南</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=陕西">陕西</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=甘肃">甘肃</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=青海">青海</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=内蒙古">内蒙古</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=广西">广西</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=西藏">西藏</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=宁夏">宁夏</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=新疆">新疆</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=xianggang">香港</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=taiwan">台湾</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=aomen">澳门</a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div className="filter mt-15 clear">
                            <div className="filter-title">
                                <h3>按类型查找</h3>
                            </div>
                            <div className="filter-list">
                                <ul>
                                    <li>
                                        <a href="./channels?keyword=卫视">卫视</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=新闻">新闻</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=影视">影视</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=娱乐">娱乐</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=体育">体育</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=财经">财经</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=健康">健康</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=生活">生活</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=儿童">儿童</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=科教">科教</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=军事">军事</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=电影">电影</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=音乐">音乐</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=综合">综合</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=记录">记录</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=游戏">游戏</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=农业">农业</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=美食">美食</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=探索">探索</a>
                                    </li>
                                    <li>
                                        <a href="./channels?keyword=教育">教育</a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div className="pannel mt-15 clear">
                        <div className="row">
                            <h3>频道列表</h3>
                        </div>

                        <ChannelsPage channels={ this.props.channels }  />


                        <div className="pages clear">
                            <strong>1</strong><a href="?p=2" data-ci-pagination-page="2">2</a><a href="?p=3" data-ci-pagination-page="3">3</a><a href="?p=2" data-ci-pagination-page="2"
                                rel="next">下一页</a><a href="?p=16" data-ci-pagination-page="16">尾页</a>
                        </div>
                    </div>
                </div>
                <Footer />
            </div>
            );
    }
}



function mapStateToProps(state) {
    const {channels, isLoading, error} = state.channels;
    return {
        channels,
        isLoading,
        error
    };
}

export default connect(mapStateToProps)(Channels);
