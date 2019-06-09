import React, { Component } from "react";

import {connect} from "react-redux";

import queryString from 'query-string';

import Header from '../components/Header'
import Footer from '../components/Footer'

import ChannelsPage from '../components/channel/ChannelsPage'

import {fetchChannels } from '../actions';
import Filters from '../components/filter/Filters';


 
import {CHANNEL_DISTRICTS, CHANNEL_TYPES} from '../constants';

import ChannelFilter from '../components/filter/ChannelFilter'

import '../stylesheets/channel.css';

const CHANNEL_DISTRICT_FILTER = CHANNEL_DISTRICTS.map(item => {
    return {
        text: item,
        value: item =='央视'?"CCTV":item
    }
});


const CHANNEL_TYPE_FILTER = CHANNEL_TYPES.map(item => {
    return {
        text: item,
        value: item
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

        this.props.dispatch(fetchChannels(filters));
    }


    componentDidMount() {

        console.log(this.props.location.search);
        const params = queryString.parse(this.props.location.search);
        console.log(params);

        this.props.dispatch(fetchChannels(params));
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

                            <Filters onChange={this.onFilterChange}>
                                <ChannelFilter filterName="type" filterItems={CHANNEL_TYPE_FILTER} />
                            </Filters>


                        </div>
                    </div>
                    <div className="pannel mt-15 clear">
                        <div className="row">
                            <h3>频道列表</h3>
                        </div>

                        <ChannelsPage channels={ this.props.channels}  />



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
