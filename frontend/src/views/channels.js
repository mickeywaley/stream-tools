import React, { Component } from "react";

import {connect} from "react-redux";

import queryString from 'query-string';

import Header from '../components/Header'
import Footer from '../components/Footer'

import ChannelsPage from '../components/channel/ChannelsPage'

import {fetchChannels } from '../actions';
import Filters from '../components/filter/Filters';


 
import {CHANNEL_DISTRICTS} from '../constants';

import ChannelFilter from '../components/filter/ChannelFilter'

import '../stylesheets/channel.css';

const CHANNEL_DISTRICT_FILTER = CHANNEL_DISTRICTS.map(item => {
    return {
        text: item,
        value: item =='央视'?"CCTV":item
    }
});


class Channels extends Component {

    state = {
        filters: { keyword: '',
                    type:''
                },
    }

    onFilterChange = (filters) => {
        console.log(filters)
        this.setState({ filters });

        this.props.dispatch(fetchChannels(filters.keyword));
    }


    componentDidMount() {

        //console.log(this.props.location.search);
        const parsed = queryString.parse(this.props.location.search);
        //console.log(parsed.keyword);

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
                               >
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
                            <Filters onChange={this.onFilterChange}>
                                <ChannelFilter filterName="keyword" filterItems={CHANNEL_DISTRICT_FILTER} />
                            </Filters>
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
